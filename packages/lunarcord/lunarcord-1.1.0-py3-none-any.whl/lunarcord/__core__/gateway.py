import orjson as json, sys, aiohttp
from .requests import Manager
from .addons import Utils, Signal, Debugger, lunarlist, Database, Cooldown, Callable
from ..basetypes import Message, Channel, User, Interaction, Context, Reaction, Guild, Member, Invite, Snowflake, Role
from ..commands import SlashCommand
from ..ui import Button, View, SelectMenu, Modal, TextInput
import time, threading, zlib, random

debug = Debugger(
    method=1
)

debug.disable()

GUILDS = 1
GUILD_MEMBERS = 2
GUILD_MODERATION = 4
EMOJIS_AND_STICKERS = 8
GUILD_EMOJIS_AND_STICKERS = EMOJIS_AND_STICKERS
GUILD_EMOJIS = EMOJIS_AND_STICKERS
GUILD_STICKERS = EMOJIS_AND_STICKERS
GUILD_INTEGRATIONS = 16
GUILD_WEBHOOKS = 32
GUILD_INVITES = 64
GUILD_VOICE_STATES = 128
GUILD_PRESENCES = 256
GUILD_MESSAGES = 512
GUILD_REACTIONS = 1024
GUILD_MESSAGE_REACTIONS = 1024
GUILD_TYPING = 2048
GUILD_MESSAGE_TYPING = 2048
DIRECT_MESSAGES = 4096
DIRECT_MESSAGE_REACTIONS = 8192
DIRECT_MESSAGE_TYPING = 16384
MESSAGE_CONTENT = 32768
MESSAGES_CONTENT = 32768
GUILD_SCHEDULED_EVENT = 65536
AUTOMOD_CONFIGURATION = 1048576
AUTO_MOD_CONFIGURATION = 1048576
AUTO_MODERATION_CONFIGURATION = 1048576
AUTOMOD_EXECUTION = 2097152
AUTO_MOD_EXECUTION = 2097152
AUTO_MODERATION_EXECUTION = 2097152
ALL_INTENTS = 3276799
ALL = 3276799

# All opcode IDs

DISPATCH = 0
HEARTBEAT = 1
IDENTIFY = 2
PRESENCE_UPDATE = 3
VOICE_STATE_UPDATE = 4
RESUME = 6
RECONNECT = 7
REQUEST_GUILD_MEMBERS = 8
INVALID_SESSION = 9
HELLO = 10
HEARTBEAT_ACK = 11

# All opcode names

OPCODES = [
    'DISPATCH',
    'HEARTBEAT',
    'IDENTIFY',
    'PRESENCE_UPDATE',
    'VOICE_STATE_UPDATE',
    None,
    'RESUME',
    'RECONNECT',
    'REQUEST_GUILD_MEMBERS',
    'INVALID_SESSION',
    'HELLO',
    'HEARTBEAT_ACK'
]

# Relationship Types

NO_RELATIONSHIP = 0
FRIEND = 1
BLOCKED = 2
PENDING_INCOMING = 3
PENDING_OUTGOING = 4
IMPLICIT = 5

class Relationship:
    type = -1
    name = 'Base'
    
class NoRelationship(Relationship):
    type = 0
    name = 'Null'
    
class Friend(Relationship):
    type = 1
    name = 'Friend'
    
class Blocked(Relationship):
    type = 2
    name = 'Blocked'
    
class PendingIncoming(Relationship):
    type = 3
    name = 'Pending Incoming'
    
class PendingOutgoing(Relationship):
    type = 4
    name = 'Pending Outgoing'
    
class Implicit(Relationship):
    type = 5
    name = 'Implicit'
    
RELATIONSHIP_TYPES = {relationship.type: relationship.name for relationship in (NoRelationship, Friend, Blocked, PendingIncoming, PendingOutgoing, Implicit)}

class GatewaySession:
    '''
    Represents a gateway's session data.
    '''
    
    def __init__(self, gateway, data: dict, /):
        
        self.gateway: Gateway = gateway
        self.raw: dict = data
        self.type: str = data.get('session_type')
        self.id: str = data.get('session_id')
        self.resume_url: str = data.get('resume_gateway_url')
        self.client_info: dict = data.get('client_info')
        self.status: str = data.get('status')
        self.active: bool = data.get('active', False)
        self.created_at: int = data.get('created_at')
        self.activities: list[dict] = data.get('activities', [])
        
        if self.type is None:
            self.type: str = data.get('type')
            
        self.resumer: GatewayResume = GatewayResume(self)
        
    def __repr__(self):
        return f'GatewaySession(gateway={self.gateway}, data={self.raw})'
        

class GatewayResume:
    '''
    Represents data used for easily resuming the gateway connection/session.
    '''
    
    def __init__(self, session: GatewaySession, /):
        
        self.session: GatewaySession = session
        self.url: str = self.session.resume_url
        
    @property
    def gateway(self):
        return self.session.gateway
    
    @property
    def token(self):
        return self.gateway.token
        
    @property
    def sequence(self):
        return self.gateway._sequence
    
    def __repr__(self):
        return f'GatewayResume(session={self.session})'
    
    async def resume(self):
        
        if self.url is None:
            return None
        
        token = self.token
        sequence = self.sequence
        
        oldGateway = self.gateway
        
        self.session.gateway = None
        
        newGateway = Gateway(oldGateway.bot, oldGateway)
        newGateway.setToken(token)
        
        oldGateway.bot._gateway = newGateway
        await oldGateway.stopSignal.call()
        
        await newGateway.start(
            runAfterThread = oldGateway.runAfterThread,
            inThread = True
        )
        
        self.session.gateway = newGateway
        
        await self.gateway.send(
            opcode = 6,
            token = self.token,
            session_id = self.session.id,
            seq = sequence
        )
        
        self.session = None
        del oldGateway


class Intent:
    
    def __init__(self, intents, id):
        
        self.id: int = id
        self.intents: Intents = intents
    
    def enable(self):
        
        if self.id is None:
            return None
        
        self.intents.append(self.id)
        
    def disable(self):
        
        if self.id is None:
            return None
        
        self.intents.remove(self.id)
        
    def __int__(self):
        
        return self.id if self.id is not None else 0
    
    def __add__(self, other: int):
        
        if type(other) is not int:
            
            try:
                other = int(other)
                
            except:
                other = 0
                
        return int(self) + other

class Intents:
    
    def __init__(self, bot):
        
        from ..bot import Bot
        
        self.bot: Bot = bot
        
        self.__intents__: list[Intents] = []
        
        self.guilds = Intent(self, GUILDS)
        self.guildMembers = Intent(self, GUILD_MEMBERS)
        self.guildModeration = Intent(self, GUILD_MODERATION)
        self.emojisAndStickers = Intent(self, EMOJIS_AND_STICKERS)
        self.guildIntegrations = Intent(self, GUILD_INTEGRATIONS)
        self.guildWebhooks = Intent(self, GUILD_WEBHOOKS)
        self.guildInvites = Intent(self, GUILD_INVITES)
        self.guildVoiceStates = Intent(self, GUILD_VOICE_STATES)
        self.guildPresences = Intent(self, GUILD_PRESENCES)
        self.guildMessages = Intent(self, GUILD_MESSAGES)
        self.guildReactions = Intent(self, GUILD_REACTIONS)
        
    def append(self, intent: Intent):
        
        if type(intent) is not intent:
            return None
        
        if intent in self.__intents__:
            return None
        
        self.__intents__.append(intent)
        
    def remove(self, intent: Intent):
        
        if type(intent) is not intent:
            return None
        
        if intent not in self.__intents__:
            return None
        
        self.__intents__.remove(intent)
        
    def __iter__(self):
        
        return self.__intents__
    
    def toInteger(self) -> int:
        
        value = 0
        
        for x in self:
            value += x
            
        return value
    
    def __int__(self):
        
        return self.toInteger()
        

class Gateway:
    
    def __init__(self, bot, previousGateway = None):
        
        from ..bot import Bot, Loop, Task
        
        previousGateway: Gateway = previousGateway
        
        hasPrevious: bool = previousGateway is not None
        isFirst: bool = previousGateway is None
        
        self.ws: aiohttp.ClientWebSocketResponse = None
        self.bot: Bot = bot
        self.asyncio = self.bot.asyncio
        self.token: str = None
        self.gatewayUrl: str = 'wss://gateway.discord.gg/?v=9&encoding=json'
        self.isBot: bool = True
        self.origin: str = self.bot.origin
        
        self.db = Database(
            origin = self.origin
        )
        
        global asyncio
        asyncio = self.asyncio
        
        if hasPrevious: # Restore previous attributes
            
            self.httpSession: aiohttp.ClientSession = previousGateway.httpSession
            self.manager: Manager = previousGateway.manager
            
            self.relationships: lunarlist[dict] = previousGateway.relationships
            self.users: lunarlist[User] = previousGateway.users
            self.channels: lunarlist[Channel] = previousGateway.channels
            self.guilds: lunarlist[Guild] = previousGateway.guilds
            
            self.onStartFunctions: list = previousGateway.onStartFunctions
            self.onMessageFunctions: list = previousGateway.onMessageFunctions
            self.channelUpdateFunctions: list = previousGateway.channelUpdateFunctions
            self.channelDeleteFunctions: list = previousGateway.channelDeleteFunctions
            self.channelCreateFunctions: list = previousGateway.channelCreateFunctions
            self.typingStartedFunctions: list = previousGateway.typingStartedFunctions
            self.typingStoppedFunctions: list = previousGateway.typingStoppedFunctions
            self.presenceUpdateFunctions: list = previousGateway.presenceUpdateFunctions
            self.messageUpdatedFunctions: list = previousGateway.messageUpdatedFunctions
            self.messageDeletedFunctions: list = previousGateway.messageDeletedFunctions
            self.reactionAddFunctions: list = previousGateway.reactionAddFunctions
            self.reactionRemoveFunctions: list = previousGateway.reactionRemoveFunctions
            self.messagePinnedFunctions: list = previousGateway.messagePinnedFunctions
            self.memberJoinFunctions: list = previousGateway.memberJoinFunctions
            self.memberLeaveFunctions: list = previousGateway.memberLeaveFunctions
            self.memberUpdateFunctions: list = previousGateway.memberUpdateFunctions
            self.commandInvokedFunctions: list = previousGateway.commandInvokedFunctions
            self.invalidCommandFunctions: list = previousGateway.invalidCommandFunctions
            self.commandCooldownFunctions: list = previousGateway.commandCooldownFunctions
            self.commandErrorFunctions: list = previousGateway.commandErrorFunctions
            
            self.eventSignals: dict[str, list[Signal]] = previousGateway.eventSignals

            self.views: list[View] = previousGateway.views
            self.modals: list[Modal] = previousGateway.modals
            self.loops: list[Loop] = previousGateway.loops
            self.tasks: list[Task] = previousGateway.tasks

            self.voiceGateways: list[VoiceGateway] = previousGateway.voiceGateway
            
            self.isBot: bool = True
            
        else: # Create new attributes
            
            self.httpSession: aiohttp.ClientSession = aiohttp.ClientSession()
            self.manager: Manager = Manager(self.token, self.httpSession, self.isBot, self)
            
            self.relationships: lunarlist[dict] = lunarlist()
            self.users: lunarlist[User] = lunarlist()
            self.channels: lunarlist[Channel] = lunarlist()
            self.guilds: lunarlist[Guild] = lunarlist()
        
            self.onStartFunctions: list = []
            self.onMessageFunctions: list = []
            self.channelUpdateFunctions: list = []
            self.channelCreateFunctions: list = []
            self.channelDeleteFunctions: list = []
            self.typingStartedFunctions: list = []
            self.typingStoppedFunctions: list = []
            self.presenceUpdateFunctions: list = []
            self.messageUpdatedFunctions: list = []
            self.messageDeletedFunctions: list = []
            self.reactionAddFunctions: list = []
            self.reactionRemoveFunctions: list = []
            self.messagePinnedFunctions: list = []
            self.memberLeaveFunctions: list = []
            self.memberJoinFunctions: list = []
            self.memberUpdateFunctions: list = []
            self.commandInvokedFunctions: list = []
            self.invalidCommandFunctions: list = []
            self.commandCooldownFunctions: list = []
            self.commandErrorFunctions: list = []
            
            self.eventSignals: dict[str, list[Signal]] = {}
            self.futures: list[tuple] = []

            self.views: list[View] = []
            self.modals: list[Modal] = []
            self.loops: list[Loop] = []
            self.tasks: list[Task] = []
            
            for x in ('READY', 'MESSAGE_CREATE', 'INTERACTION_CREATE'):
                
                self.eventSignals[x] = []

            self.voiceGateways: list[VoiceGateway] = []
            
        if self.httpSession.closed:
            self.httpSession: aiohttp.ClientSession = aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=200))
        
        self.slashCommands: list[SlashCommand] = []
        
        self.__decompress__: zlib._Decompress = zlib.decompressobj()
        
        self._sequence: int = None
        self.heartbeatInterval: float = None
        self.last_heartbeat_ack: float = None
        self.last_heartbeat: float = None
        self.latency: float = None
        
        self.closed: bool = False
        self.resumed: bool = hasPrevious
        self.forceFullyTerminated: bool = False # If True, bot will not try to reconnect.
        self.reconnect: Signal = Signal()
        self.reconnect.connect(self.resume)
        
        try:
            self.eventLoop = asyncio.get_event_loop() # The eventloop used for asyncio stuff
        except:
            self.eventLoop = None
        
        self.isReady: bool = False
        
    @property
    def preToken(self):
        return 'Bot ' if self.isBot else ''
    
    @property
    def fullToken(self):
        return self.preToken + self.token
    
    @property
    def messages(self):
        '''
        All the messages in the bot's cache in one generator.
        '''
        
        for channel in self.channels:
            yield from channel.messages

    @property
    def roles(self):
        """
        All roles in the bot's cache, from all the different guilds the bot is in.
        """

        for guild in self.guilds:
            yield from guild.roles

    @property
    def members(self):
        """
        All members in the bot's cache, from all the guilds the bot is in.
        """

        for guild in self.guilds:
            yield from guild.members
            
    @property
    def prefixes(self) -> list[str]:
        return self.bot.prefixes
    
    @property
    def uptime(self) -> float:
        return time.time() - self.startTime
    
    async def resume(self):
        
        if not hasattr(self, 'session'):
            return None
        
        if self.forceFullyTerminated:
            return None
        
        session = self.session
        
        if session is None:
            return None
        
        resumer = session.resumer
        
        if resumer is None:
            return None
        
        await resumer.resume()
        
    def getSession(self):
        
        '''
        Gets the current `ClientSession` or creates a new one if needed.
        '''
        
        try:
            if self.httpSession is not None and not self.httpSession.closed:
                return self.httpSession
            
        except:
            
            ...
            
        return self.setSession()
        
    def setSession(self):
        
        '''
        Creates a new `ClientSession`, updates the current one and returns it.
        '''
        
        self.httpSession = aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=200), loop=self.eventLoop)
        self.manager.session = self.httpSession
        return self.httpSession
    
    async def getWs(self):
        
        '''
        Gets the current (WebSocket) or creates a new one if needed.
        '''
        
        if not hasattr(self, 'ws') or self.ws is None or self.ws.closed:
            return await self.setWs()
        
        return self.ws
    
    async def setWs(self):
        
        '''
        Creates a new `ClientWebSocketResponse` (WebSocket), returning it and updating the current one.
        '''
        
        try:
            self.ws = await self.getSession()._ws_connect(self.gatewayUrl, timeout=30, autoclose=True)
        
        except:
            self.ws = await self.setSession()._ws_connect(self.gatewayUrl, timeout=30, autoclose=True)
            
        return self.ws
    
    def _updateSavedViews(self):

        views: list[dict] = self.db.loadViews()

        for view in views:

            messages = view.get("msgs")
            nm = view.get("nm")
            last = view.get("lst")

            for model in self.views:
                if model.name == nm:
                    model.messages = messages
                    model.last = last

        
    def setToken(self, token: str):
        self.token = token
        self.manager.generateHeaders(self.fullToken)
        
    def _toJson(self, payload):
        return json.dumps(payload)
        
    async def send(self, opcode: int, replacement = None, **data):
        
        if self.closed:
            return
        
        if hasattr(self, 'ws') and self.ws:
            
            if data == {}:
                data = replacement
                
            payload = {
                'op': opcode,
                'd': data
            }
            
            payload = self._toJson(payload)
            
            try:
                
                await self.ws.send_bytes(
                    data = payload
                )
                
                return payload
                
            except:
                
                self.closed = True
                #raise ConnectionClosedError()
            
    async def receive(self, timeout: float = None):
        
        if self.closed:
            return None
        
        try:
            
            message = await self.ws.receive(timeout=timeout)
            payload = message.data
            
        except:
            self.closed = True
            return 'CLOSED'
            #raise ConnectionClosedError()
        
        if isinstance(payload, bytes):
            try:
                payload = payload.decode('utf-8')
            except:
                buffer = bytearray()
                buffer.extend(payload)
                payload = self.__decompress__.decompress(buffer)
                payload = payload.decode('utf-8')
                
        '''debug.log(
            'Received data! Raw form: %p',
            payload
        )'''
        
        if payload:

            try:
                return json.loads(payload)
            except:
                return payload
        
    async def identify(self):
        
        data = await self.send(
            
            opcode = 2,
            token = self.token,
            properties = {
                "os": sys.platform,
                "browser": "lunarcord",
                "device": "lunarcord"
            },
            
            intents = ALL,
            presence = self.bot.presence,
            large_threshold = 250
            
        )
        
    async def sendHeartbeat(self):

        #print(self._sequence)
        
        result = await self.send(
            
            opcode = 1,
            replacement = self._sequence
            
        )

        if result is not False:

            ... #print("Heartbeat sent! Gateway:", self)
        
        
    async def changeStatus(self, activities, status: str = 'online'):
        
        await self.send(
            
            opcode = 3,
            since = 0,
            activities = activities,
            status = status,
            afk = False,
            client_status = {'mobile': 'online'}
            
        )
        
    def doTask(self, *coroutines, signal: Signal = None):
        
        '''
        Start running one or more coroutines as tasks in the event loop, calling `signal` when one is finished. The signal args will be `coroutine` (the coroutine that was completed) and `result` (the coroutine's result).
        '''
        
        coroutines = list(coroutines)
        tasks: list = list()
        
        def finished(task):
            
            nonlocal tasks, coroutines, signal
            
            try:
                result = task.result()
                
            except:
                result = None
                
            try:
                idx = tasks.index(task)
            
            except:
                idx = 0
                
            try:
                coro = coroutines[idx]
                
            except:
                
                try:
                    coro = coroutines[0]
                    
                except:
                    coro = None
            
            # tasks = All scheduled tasks.
            # coroutines = The coroutines given in doTask args.
            # task = Task that was finished.
            # coro = The coroutine which was wrapped in this task.
            # signal = Signal to emit.
            # result = The task's results.
            
            if signal is not None:
                signal.callSync(coro, result)
                
        try: # Method 1
            
            tasks = []
                
            fut = asyncio.gather(*coroutines)
            
            async def gather():
                nonlocal fut
                await fut
                
            coro = gather()
            
            task = self.eventLoop.create_task(coro)
            #task.add_done_callback(finished)
            tasks.append(task)
                
            return tasks
        
        except: # Method 2
            
            tasks = []
            
            for coro in coroutines:
                
                tasks.append(
                    self.eventLoop.create_task(coro)
                )
                
            return tasks
    
    def finishTasks(self, *coroutines):
        
        '''
        Similarly to `doTask`, executes one or more coroutines. The differences are that this is done in a blocking manner and the results are returned, unlike with `Gateway.doTask`.
        '''
        
        def onFinish(coro, result):
            
            nonlocal pending, finished, returns
            
            if len(pending) <= 0:
                finished = True
                
            try:
                pending.remove(coro)
                
            except:
                ...
                
            returns.append(result)
        
        finished = False
        returns = []
        
        coroutines = list(coroutines)
        pending = coroutines.copy()
        signal = Signal(object, object)
        signal.connect(onFinish)
        
        self.doTask(*coroutines, signal=signal)
        
        while not finished: # Block until finished
            continue # ...
        
        return returns
    
    def finishTask(self, coroutine):
        
        '''
        Same as using `Gateway.finishTasks(coroutine)[0]`.
        '''
        
        coroutines: list = [coroutine]
        
        results = self.finishTasks(*coroutines)
        return results[0]
        
    def runInThread(self, function, *args, signal: Signal = None, name: str = None, **kwargs):
        
        '''
        Run a normal function or a coroutine function inside a Thread, calling `signal` upon finished.
        '''
        
        args = list(args)
            
        def run():

            nonlocal self, function, args, kwargs, signal
                        
            result = function(*args, **kwargs)
            
            if asyncio.iscoroutine(result):
                result = self.doTask(result)

            if signal is not None:
                signal.callSync(result)
            
        thread = threading.Thread(target=run, name=name)
        thread.start()
        return thread
        
        
    async def start(self, runAfterThread: threading.Thread, inThread: bool = False):
        
        try:
            self.eventLoop = asyncio.get_event_loop()
        except:
            self.eventLoop = asyncio.new_event_loop()
        
        if not self.eventLoop.is_running():
            self.eventLoop.run_forever()
        
        self.stopSignal = Signal() # A signal to stop all threads.
        self.stopSignal.connect(self.httpSession.close)
        await self.setWs()
        await self.bot._authenticate()
        self.runAfterThread = runAfterThread
        
        try:
        
            if not runAfterThread.is_alive():
                runAfterThread.start()
                
        except:
            
            ...
            
        if inThread:
            
            self.runInThread(self.gatewayLoop, self.ws, self.stopSignal)
            
        else:
            
            await self.gatewayLoop(self.ws, self.stopSignal)
        
    def stop(self, code: int = None):
        
        for task in self.tasks + self.loops:
            
            try:
                task.stop()
                
            except:
                continue
        
        self.forceFullyTerminated = True
            
        coros = []
        
        if self.ws is not None:
            
            coros.append(
                
                self.ws.close(
                    
                    *
                    [x for x in [code]
                    if x is not None]
                    
                )
                
            )
            
        if self.httpSession is not None:
            
            coros.append(
                self.httpSession.close()
            )
            
        self.doTask(*coros)
            
        if hasattr(self, 'stopSignal') and self.stopSignal:
            self.stopSignal.callSync()
            
        self.closed = True
        
    
    async def disconnect(self, reconnect: bool = False):
        
        await self.stop()
        
        if reconnect:
            await self.reconnect.call()
            
        else:
            self.forceFullyTerminated = True
        
        
    def heartbeatLoop(self, stop: Signal):
        
        sending = True
        
        def stopSending():
            
            nonlocal sending
            sending = False
            
        stop.connect(stopSending)
        secs = self.heartbeatInterval / 1000
        
        while sending:
            
            if self.last_heartbeat_ack is None or time.time() - self.last_heartbeat_ack > self.heartbeatInterval / 1000:

                tick = 0

                if self.last_heartbeat_ack:
                    tick = time.time() - self.last_heartbeat_ack
                
                self.last_heartbeat = time.time()
                coro = self.sendHeartbeat()
                asyncio.run_coroutine_threadsafe(coro, self.eventLoop)
                time.sleep(secs)
                
                
    def heartbeat(self, interval: float, stop: Signal):
        '''
        Starts the `heartbeatLoop`, which sends heartbeats to Discord every `interval` seconds.
        
        Parameters
        ----------
        interval: `float`
            The time to wait before sending a heartbeat, received from `helloMessage`.
        '''
        
        self.heartbeatInterval = interval
        return self.runInThread(self.heartbeatLoop, stop)
    
    async def gatewayLoop(self, ws: aiohttp.ClientWebSocketResponse, stop: Signal, /):
        
        if self.token:
            
            self.startTime = time.time()
            helloMessage = await self.receive()
            
            if helloMessage == 'CLOSED':
                return None
            
            interv = helloMessage.get('d').get('heartbeat_interval')
            debug.log('Hello Message Received')

            self.heartbeat(interval=interv, stop=stop)

            if not self.resumed:
                
                await self.identify()
            
            receiving = True
            
            def stopCallback():
                nonlocal receiving
                receiving = False
                
            stop.connect(stopCallback)
            
            while receiving:
                
                try:

                    event = await self.receive()

                    if event == 'CLOSED':
                        stop.callSync()
                        event = None

                    if type(event) is int:
                        
                        if event != 1000:
                            #print("Closed with error code", event)
                            pass

                        receiving = False
                        event = None

                    self.last = event

                except:
                    event = None
                    continue # This would terminate the connection, but now we just skip the iteration.
                
                if event is not None:
                    await self._handleEvent(event)
                    
            if not self.forceFullyTerminated:
                
                if not self.resumed:
                    
                    await self.reconnect.call()
                
    async def waitFor(self, event: str, timeout: float = None, check: Callable = None, catch: bool = False):
        
        '''
        Wait until the given event is dispatched. If `timeout` seconds have passed and the `event` still has not been dispatched, quits the waiting.
        '''
        
        if type(timeout) is not float:
            
            try:
                timeout = float(timeout)
            except:
                timeout = None
                
        if type(catch) is not bool:
            
            try:
                catch = bool(catch)
                
            except:
                catch = False

        if type(event) is not str:
            event = str(event)

        event = event.upper().replace(" ", "_").strip()
        
        def _check(*args):
            return True
        
        if not callable(check):
            check = _check
            
        future = self.eventLoop.create_future()
        self.futures.append((future, check, event))
        
        try:
            return await asyncio.wait_for(future, timeout)
        except asyncio.TimeoutError:
            if catch:
                return
            raise
                    
    async def _handleEvent(self, payload: dict):

        if type(payload) is not dict:
            print("What's a" + str(payload))
        
        name: str = payload.get('t')
        sequence: int = payload.get('s')
        opcode: int = payload.get('op')
        data: dict = payload.get('d')
        
        '''debug.log(
            'New Event Received! Operation Code: %p, Operation Name:  %p, Dispatch Name: %p, Resume Sequence: %p',
            opcode, OPCODES[opcode], name, sequence
        )'''

        tasks = [
            task[0:1] for task in self.futures
            if task[2].upper() == name
        ]
        
        if opcode == HEARTBEAT_ACK:

            self.last_heartbeat_ack = time.time()
            self.latency = self.last_heartbeat_ack - self.last_heartbeat

        elif opcode == VOICE_STATE_UPDATE:

            try:
                guildID = int(data.get("guild_id", 0))
            except:
                guildID = None

            try:
                channelID = int(data.get("channel_id"), 0)
            except:
                channelID = None

            if guildID is None or channelID is None:
                self.bot.voice = None

            else:

                guild = await self.bot.fetchGuild(guild)

                for channel in guild:
                    if channel.joined:
                        return
                    
                channel = self.bot.getChannel(channelID)
                self.bot.voice = channel
                channel.joined = True
            
        elif opcode == DISPATCH:
                
            if sequence is not None:
                self._sequence = sequence
                
            '''debug.log(
                'New dispatch! Name: %p, Payload: %p',
                name, data
            )'''
            
            if name == 'READY':
                handler = self._ready
                
            elif name == 'INTERACTION_CREATE':
                handler = self._handleInteraction
                
            elif name == 'MESSAGE_CREATE':
                handler = self._handleMessage
                
            elif name == 'PRESENCE_UPDATE':
                handler = self._handlePresenceUpdate
                
            elif name == 'CHANNEL_UPDATE':
                handler = self._handleChannelUpdate
                
            elif name == 'TYPING_START':
                handler = self._handleTyping
                
            elif name == 'GUILD_CREATE':
                handler = self._newGuild
                
            elif name == 'MESSAGE_UPDATE':
                handler = self._handleMessageUpdate
                
            elif name == 'MESSAGE_DELETE':
                handler = self._handleMessageDelete
                
            elif name == 'MESSAGE_REACTION_ADD':
                handler = self._handleMessageReaction

            elif name == 'MESSAGE_REACTION_REMOVE':
                handler = self._handleReactionRemove
                
            elif name == 'CHANNEL_PINS_UPDATE':
                handler = self._handlePinsUpdate
                
            elif name == 'GUILD_AUDIT_LOG_ENTRY_CREATE':
                handler = self._auditLogEntryCreate
                
            elif name == 'SESSIONS_REPLACE':
                handler = self._sessionsReplace
                
            elif name == 'CHANNEL_PINS_ACK':
                handler = self._channelPinsAck
                
            elif name == 'RESUMED':
                handler = self._resumed
                
            else:
                
                split = name.split("_")
                fixed = []

                for x in split:
                    x = x.lower()
                    x = list(x)
                    x[0] = x[0].upper()
                    x = "".join(x)
                    fixed.append(x)

                fixed = "".join(fixed)
                handlername = f"_handle{fixed}"

                try:
                    handler = getattr(self, handlername)

                except:

                    handler = None

                    debug.log(
                        'Unhandled Dispatch! Name: %p',
                        name,
                        force=False
                    )

            if handler is None:
                return
                
            returns = await handler(data)
            signals = self.eventSignals.get(name)
            
            if type(returns) is not tuple:
                returns = (returns,)
            
            if signals:
                
                coros = [
                    signal.call(*returns) for signal in signals
                ]
                
                await asyncio.gather(*coros)
                
        else:
            
            return debug.log(
                f'Unhandled Event! Opcode: %p, Name: %p',
                opcode, OPCODES[opcode]
            )
        
        for future, check in tasks:
            
            try:
                checked = bool(check(*returns))
            except:
                checked = False

            if not checked:
                continue

            length = len(returns)

            if length == 0:
                future.set_result(None)
            elif length == 1:
                future.set_result(returns[0])
            else:
                future.set_result(returns)

            try:
                self.futures.remove((future, check, name))
            except:
                ...
        
    async def _handleMessage(self, data: dict):
        
        msg = await Message._create(
            bot=self.bot,
            data=data
        )

        if msg.author is None:
            return
        
        events = [event(msg) for event in self.onMessageFunctions]
        await asyncio.gather(*events)
        
        isCommand = False

        if (not self.prefixes) and (self.bot.textCommands):
            self.bot.prefixes.append("!")
            
        for prefix in self.prefixes:
            
            if msg.content.lower().startswith(prefix.lower()):
                
                isCommand = True
                prefixUsed = prefix
                break
                
        if isCommand:
            
            content: str = Utils.removeFirst(prefixUsed, msg.content)
            content = ''.join(content).strip()
            
            called = None
            ctx = None
            
            for command in self.bot.textCommands:
                
                names = command.namesLower
                
                for name in names:
                
                    if content.lower().startswith(name):
                        
                        content: str = Utils.removeFirst(name, content)
                        content: str = content.strip()
                        args: list = content.split(' ')
                        
                        ctx = Context(
                            bot = self.bot,
                            message = msg,
                            triggerer = prefixUsed + name,
                            prefix = prefixUsed,
                            command = command
                        )
                        
                        called = command
                        break
                        
            if not called:

                ctx = Context(
                    bot = self.bot,
                    message = msg,
                    triggerer = prefixUsed + content.lower().removeprefix(prefixUsed).strip().split(" ")[-1],
                    prefix = prefixUsed,
                    command = None
                )

            if ctx:
                await ctx()
                
        return msg
            
    async def _handleInteraction(self, data: dict):
        
        interaction = Interaction(
            bot=self.bot,
            data=data
        )
        
        await interaction._proc()
        
        if interaction.type == 2:
            
            await self._handleApplicationCommand(interaction)
            
        elif interaction.type == 3:
            
            await self._handleComponentInteraction(interaction)
            
        elif interaction.type == 5:
            
            await self._handleModalInteraction(interaction)
            
        return interaction
        
    async def _handleApplicationCommand(self, interaction: Interaction):
        
        target = None
        coros = []
        
        for slashCommand in self.slashCommands:
            if str(slashCommand.id) == str(interaction.commandID):
                target = slashCommand
                break
            
        if target is not None:
            
            interaction.command = slashCommand

            cdtimer = interaction.author.getCooldown(
                name=slashCommand.name,
                type="slashcommand"
            )

            interaction.cooldown = Cooldown.construct(cdtimer)
            coros.append(slashCommand(interaction, *interaction.args))
        
        await asyncio.gather(*coros)
        
    async def _handleComponentInteraction(self, interaction: Interaction):
        
        if interaction.componentType == View.BUTTON:
            
            await self._handleButtonInteraction(interaction)
            
        elif interaction.componentType == View.STRING_SELECT:
            
            await self._handleSelectMenuInteraction(interaction)
            
    async def _handleButtonInteraction(self, interaction: Interaction):
        
        target = None
        
        for view in self.views:

            if type(view) is not View:
                continue

            if interaction.message.id not in view.messageIDs:
                continue
            
            button: Button = view.getButton(
                
                customID = interaction.customID
                
            )
            
            if button:
                
                target = button
                break
            
        if target:

            if True:
            
                await interaction.ack()
                await target(interaction)
                button.view.updateLast()

            else:

                target.view.delete()
            
    async def _handleSelectMenuInteraction(self, interaction: Interaction):
        
        target = None
        
        for view in self.views:

            if type(view) is not View:
                continue

            if interaction.message.id not in view.messageIDs:
                continue
            
            select: SelectMenu = view.getSelectMenu(
                
                customID = interaction.customID
                
            )
            
            if select:
                
                target = select
                break
                
        if target:
            
            for idx, option in enumerate(interaction.values.copy()):
                
                for targetOption in target.options:
                    
                    if targetOption.value == option:
                        
                        interaction.values[idx] = targetOption
            
            coros = [interaction.ack(), target(interaction)]
            
            for clicked in interaction.values:
                
                coros.append(clicked(interaction))
                
            await asyncio.gather(*coros)
            
    async def _handleModalInteraction(self, interaction: Interaction):
        
        target = None
        
        for modal in self.modals:
            
            if modal.customID == interaction.customID:
                
                target = modal
            
        if target:
            
            self.modals.remove(target)
            
            async def checkFilled():
                
                targetInputs: list[TextInput] = []
                
                nonlocal target, interaction
                raw = interaction.filled
                
                for filled in raw:
                    
                    comp: dict = filled.get('components')[0]
                    customID: int = comp.get('custom_id')
                    value: str = comp.get('value')
                    
                    for input in target.inputs:
                        
                        if input.customID == customID:
                            
                            targetInput = input
                            
                    if targetInput is not None:
                        
                        targetInput.value = value
                        targetInputs.append(targetInput)
                
                return targetInputs
            
            await interaction.ack()
            inputs = await checkFilled()
            
            coros = [target(interaction)]
            
            for input in inputs:
                
                coros.append(input(interaction, input.value))
                
            await asyncio.gather(*coros)
        
    async def _handlePresenceUpdate(self, data: dict):
        
        user = data.pop('user')
        
        user = await self.bot.fetchUser(
            id = user['id']
        )
        
        presence = {
            'status': data['status'],
            'activities': data['activities'],
            'mobile': 'mobile' in data['client_status']
        }
        
        await asyncio.gather(*[event(user, presence) for event in self.presenceUpdateFunctions])
        return user, presence
        
    async def _handleChannelUpdate(self, data):
        id = data['id']
        
        channel = await Channel.fromID(
            bot = self.bot,
            channel = id
        )
        
        for idx, cached in enumerate(self.channels):
            if cached.id == int(id):
                self.channels[idx] = Channel(self.bot, data)
                
        
        await asyncio.gather(*[event(channel) for event in self.channelUpdateFunctions])
        return channel
            
    async def _handleTyping(self, data: dict):
        
        coros = [
            
            self.bot.fetchUser(
                id = data['user_id']
            ),
        
            self.bot.fetchChannel(
                id = data['channel_id']
            )
            
        ]
        
        user, channel = await asyncio.gather(*coros)
        await asyncio.gather(*[event(user, channel) for event in self.typingStartedFunctions])
        return user, channel
        
    async def _handleTypingStop(self, user: User, channel: Channel):
        
        if False: # Disabled
            
            if user is not None and channel is not None:

                gathered = [
                    event(user, channel)
                    for event in self.typingStoppedFunctions
                ]
                
                await asyncio.gather(*gathered)
                
            return user, channel
            
    async def _handleMessageUpdate(self, data: dict):
        
        message = Message(self.bot, data)
        
        if message:
            
            channel = self.bot.getChannel(message.channel)
            
            if channel:
                
                old = channel.getMessage(message.id)
                
                if old:
                    
                    await message._proc()
                    message.author, message.channel = old.author, old.channel
                    
                    try:
                        message.channel.messages.replace(old, message)
                    except:
                        ...
                    
                    if message.content is not None:
                        await asyncio.gather(*[event(old, message) for event in self.messageUpdatedFunctions])
                        return message
        
    async def _handleMessageDelete(self, data: dict):
        
        id = int(data.get('id'))
        channel = int(data.get('channel_id'))
        target = await self.bot.fetchMessage(channel, id)
        
        if target:
        
            await asyncio.gather(*[event(target) for event in self.messageDeletedFunctions])
                
            if target in target.channel.messages:
                target.channel.messages.remove(target)

            for view in self.views:

                if type(view) is not View:
                    continue

                if target.id in view.messageIDs:
                    
                    try:
                        view.messages.remove(target)
                    except:
                        view.messages.remove(target.id)

                    if len(view.messages) == 0:
                        
                        view.delete() # Delete from DB

                    view.save()
                
            return target
        
    async def _handleMessageDeleteBulk(self, data: dict):

        ids = data.get("ids")
        channel = data.get("channel_id")
        coros = []

        for id in ids:
            payload = {"id": id, "channel_id": channel}
            coros.append(self._handleMessageDelete(payload))

        await asyncio.gather(*coros)
            
    async def _handleMessageReaction(self, data: dict):
        
        userID = data.get('user_id')
        messageID = data.get('message_id')
        channelID = data.get('channel_id')
        emojiData = data.get('emoji')
        
        reaction = Reaction(
            bot = self.bot,
            user = userID,
            message = messageID,
            channel = channelID,
            emoji = emojiData
        )
        
        await reaction._proc()
        
        await asyncio.gather(*[event(reaction) for event in self.reactionAddFunctions])
        return reaction
    
    async def _handleReactionRemove(self, data: dict):

        userID = data.get("user_id")
        messageID = data.get("message_id")
        channelID = data.get("channel_id")
        emoji = data.get("emoji")
        burst = data.get("burst")

        message = await self.bot.fetchMessage(
            channel = channelID,
            id = messageID
        )

        if message:

            ename = emoji.get("name")
            eid = emoji.get("id")
            found = None
            
            for reaction in message.reactions:

                if reaction.emojiName == ename or ( reaction.emojiID is not None and reaction.emojiID == eid ):

                    found = reaction

            if type(found) is Reaction:

                message.reactions.remove(found)
            
            await asyncio.gather(*[event(found) for event in self.reactionRemoveFunctions])
            
    async def _handlePinsUpdate(self, data: dict):
        
        channel: int = int(data.get('channel_id'))
        
        try:
            guild: int = int(data.get('guild_id'))
            
        except:
            guild = None # DM or Group Chat
            
        # print('PinsUpdateData', data)
        
        # How to know which MESSAGE is pinned?
        
    async def _channelPinsAck(self, data: dict):
        
        # print('ChannelPinsAck Received, Data:', data)
        
        version: int = data.get('version')
        timestamp: str = data.get('timestamp')
        channel: int = int(data.get('channel_id'))
        
        # print('Channel Pins Ack received for Channel', channel)
        
    async def _auditLogEntryCreate(self, data: dict):
            
        try:
        
            user: int = int(data.get('user_id', 0))
            target: int = int(data.get('target_id', 0))
            options: dict = data.get('options', {})
            id: int = int(data.get('id', 0))
            actionType: int = data.get('action_type', 0)
            guild: int = int(data.get('guild_id', 0))

        except:

            ...
        
    async def _sessionsReplace(self, data: list[dict]):
    
        sessions: int = len(data)
        objects: list[GatewaySession] = []
        
        for session in data:
            
            #status: str = session.get('status')
            #sessionID: str = session.get('session_id')
            object = GatewaySession(self, session)
            objects.append(object)
            
        debug.log(
            '%p Active Sessions: %p',
            sessions, objects
        )
        
    async def _newGuild(self, data: dict):
        
        isLazy = data.get('lazy')
        isNew = not isLazy

        old = self.bot.getGuild(data.get("id"))

        if old:
            self.guilds.remove(old)

        guild = await Guild._create(
            bot = self.bot,
            data = data
        )

        if isNew:
            ... # OnGuildCreateEvent
            
        return guild
    
    async def _handleGuildMemberUpdate(self, data: dict):

        userData = data.pop("user")
        guildID = data.pop("guild_id")
        guild = await self.bot.fetchGuild(guildID)

        if guild:

            member = await Member._create(
                bot = self.bot,
                user = userData,
                data = data,
                guild = guild
            )

            await asyncio.gather(*[x(member) for x in self.memberUpdateFunctions])

            return member
        
    async def _handleChannelCreate(self, data: dict):

        id = data.get("id")

        channel = await self.bot.fetchChannel(
            id = int(id)
        )

        channel.guild.channels.append(channel)
        await asyncio.gather(*[x(channel) for x in self.channelCreateFunctions])

    async def _handleChannelDelete(self, data: dict):

        id = data.get("id")

        channel = self.bot.getChannel(
            id = int(id)
        )

        if channel:

            channel.guild.channels.remove(channel)
            await asyncio.gather(*[x(channel) for x in self.channelDeleteFunctions])

    async def _handleGuildMemberAdd(self, data: dict):

        user = data.get("user")
        guild = data.get("guild_id")
        id = user.get("id")

        member = await self.bot.fetchMember(
            guild = guild,
            id = id
        )

        if member:
            
            member.guild.members.append(member)
            await asyncio.gather(*[x(member) for x in self.memberJoinFunctions])

    async def _handleGuildMemberRemove(self, data: dict):

        user = data.get("user")
        guild = data.get("guild_id")
        id = user.get("id")

        member = self.bot.getMember(
            guild = guild,
            id = id
        )

        if member:
            
            try:
                member.guild.members.remove(member)
            except:
                ...

            await asyncio.gather(*[x(member) for x in self.memberLeaveFunctions])

    async def _handleVoiceServerUpdate(self, data: dict):

        token: str = data.get("token")
        guildID: str = data.get("guild_id")
        endpoint: str = data.get("endpoint")
        guild: Guild = self.bot.getGuild(guildID)

        target = None

        for gateway in self.voiceGateways:
            if gateway.guild.id == guild.id:
                target = gateway

        if not target:
            return
        
        target.endpoint = endpoint
        target.token = token
        await target.start()

    async def _handleVoiceStateUpdate(self, data: dict):

        member: dict = data.get("member")
        user: dict = member.get("user")
        guildID: str = data.get("guild_id")
        channelID: str = data.get("channel_id")
        sessionID: int = data.get("session_id")

        model = await self.bot.fetchMember(
            guild = guildID,
            id = user.get("id")
        )

        channel = await self.bot.fetchChannel(channelID)

        if model and channel:
                
            if model.id == self.bot.id:

                self.bot.voice = channel
                voiceGateway = VoiceGateway(channel, sessionID, self)
                self.voiceGateways.append(voiceGateway)

            model.vc = channel

    async def _handleInviteCreate(self, data: dict):

        invite = Invite(self.bot, data)
    
    async def _ready(self, sessionData: dict):

        self.isReady = True
        
        self.relationships = lunarlist(*[{'user': User(self.bot, relationship.get('user')), 'type': RELATIONSHIP_TYPES.get(relationship.get('type')), 'id': relationship.get('type')} for relationship in sessionData.get('relationships')])

        for relationship in self.relationships:
            await relationship.get("user")._proc()
            self.users.append(relationship.get("user"))

        # DoLoad
        # UNNEEDED

        """
        
        try:
            guilds = await self.manager.loadGuilds()
        except:
            guilds = []

        coros = []
        
        for guild in guilds:

            async def fetch():

                try:
                    await Guild.fromID(
                        bot = self.bot,
                        guild = guild.get('id')
                    )
                
                except:
                    pass
            
            coros.append(fetch())
            
        if coros:
            
            await asyncio.gather(*coros) # Fetch guilds to cache them

        coros = []
                
        for channel in [channel for channel in self.channels if channel.recipients]:
            
            for recipient in channel.recipients:
                
                recipientID = recipient.get('id')
                
                coros.append(
                    self.bot.fetchUser(recipientID)
                )
                
        await asyncio.gather(*coros) # Fetch users to cache them

        """

        # DoLoad Finish

        self.session = GatewaySession(self, sessionData)

        await asyncio.gather(*[event(self.bot) for event in self.onStartFunctions])
            
        return self.bot
    
    async def _resumed(self, data: dict):

        if not self.resumed:
            self.resumed = True

        trace = data.get("_trace")
        string = trace[0]
        data = json.loads(string)

class VoiceGateway:

    IDENTIFY = 0
    SELECT = 1
    READY = 2
    HEARTBEAT = 3
    SESSION_DESCRIPTION = 4
    SPEAKING = 5
    HEARTBEAT_ACK = 6
    RESUME = 7
    HELLO = 8
    RESUMED = 9
    CLIENT_DISCONNECT = 13

    def __init__(self, channel: Channel, sessionID: str, parent: Gateway):

        self.ws: aiohttp.ClientWebSocketResponse = None
        self.httpSession: aiohttp.ClientSession = None
        self.nonces: list[int] = []
        self.running: bool = False
        self.closed: bool = False
        self._received = None

        self.channel: Channel = channel
        self.guild: Guild = channel.guild
        self.endpoint: str = None
        self.token: str = None
        self.sessionID: str = sessionID
        self.parent: Gateway = parent
        
        self.manager: Manager = self.parent.manager
        self.eventLoop = self.parent.eventLoop
        self.bot = self.parent.bot

    @property
    def gatewayUrl(self):
        return f"wss://{self.endpoint.partition(":")[0]}/?v=4"

    def generateNonce(self):

        while True:

            generated = random.randint(100, 10000000000000)

            if generated not in self.nonces:

                self.nonces.append(generated)
                return generated

    def send(self, opcode: int, replacement = None, **data):
        return Gateway.send(self, opcode, replacement, **data)
    
    def receive(self, timeout: float = None):
        return Gateway.receive(self, timeout)
    
    def _toJson(self, payload):
        return Gateway._toJson(self, payload)
    
    def receiveSync(self):
        
        async def task():

            try:
                data = await self.receive()
            except Exception as error:
                data = error
                
            self._received = data

        last = self._received
        self.parent.doTask(task())

        while True:
            if self._received != last:
                break

        data = self._received
        
        if isinstance(data, Exception):
            raise data
        
        return data
    
    def sendSync(self, opcode: int, replacement, **data):

        self.parent.doTask(

            self.send(
                opcode,
                replacement,
                **data
            )

        )

    def identify(self):

        return self.send(
            opcode = int(self.IDENTIFY),
            server_id = str(self.guild.id),
            user_id = str(self.bot.id),
            session_id = str(self.sessionID),
            token = str(self.token)
        )
    
    def heartbeat(self):

        return self.send(
            opcode = self.HEARTBEAT,
            replacement=1501184119561
        )

    def getSession(self):
        return Gateway.getSession(self)
    
    def setSession(self):
        return Gateway.setSession(self)
    
    async def start(self):
        
        Gateway.setSession(self)
        await Gateway.setWs(self)

        self.parent.stopSignal.connect(self.close)
        self.parent.runInThread(self.activity)

    async def close(self):

        try:
            await self.httpSession.close()
        except:
            pass

        self.running = False
        self.closed = True

        try:
            self.parent.voiceGateways.remove(self)
        except:
            ...

    async def stop(self, code: int = None):

        if code is None:
            await self.ws.close()
        else:
            await self.ws.close(code)

        await self.close()

    async def handle(self, payload: dict):

        opcode = payload.get("op")
        data = payload.get("d")

        match opcode:

            case self.HELLO:
                await self.hello(data)

            case _:
                debug.log("Unhandled Voice Event! Opcode: %p", opcode, force=True)


    async def hello(self, data: dict):

        version = data.get("v")
        interv = data.get("heartbeat_interval")

        self.parent.runInThread(
            function=self.heartbeatLoop,
            interval=interv
        )
        
    async def activity(self):

        self.running = True

        print(await self.identify())

        while self.running:
            data = await self.receive()
            
            if data:

                print("VC Data:", data)

                if type(data) is int:
                    await self.close()

                elif type(data) is dict:
                    await self.handle(data)

    async def heartbeatLoop(self, interval: float):

        interval = interval / 1000

        while self.running:

            await asyncio.sleep(interval)
            await self.heartbeat()