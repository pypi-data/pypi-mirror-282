from .__core__.gateway import Gateway, Utils, Manager, User, Channel, Message, Guild, Snowflake, Signal, Role, Member, aiohttp
from . import Activity, Playing, Watching, Listening, Streaming, StatusError
from .errors import UnauthorizedError, RegisterError, UnregisterError, ReregisterError
from .commands import __createSlashCommand__, __createEvent__, textCommand, SlashCommand, TextCommand, Registrable, Event
from .tasks import __createTask__, __createLoop__, NameLike, TimeLike, Iterable, Task, Loop
from .configs import UserConfiguration, BaseConfiguration, userConfig

import asyncio, time, sys, orjson as json, inspect, os, datetime, traceback, webbrowser

from importlib.util import spec_from_file_location, module_from_spec
from os.path import isfile, split, join
from os import listdir

from threading import Thread

class NoTimeout: ...

class Anyone: ...
class Anything: ...
class Any: ...
class Unknown: ...

class PhoneNumber: ...
class Email: ...
class UserLogin: ...
class Password: ...
class String: ...

globalBot = None


class Observer(Thread):
    
    '''
    Looks and notifies for changes in given files.
    '''
    
    def __init__(self, files: list[str] = [], folders: list[str] = []):
        
        super().__init__()
        
        self.running: bool = True
        
        self.files: list[str] = files
        self.times: dict[str, float] = {}
        
        self.updatedPaths: list[str] = files
        self.deletedPaths: list[str] = files
        self.areDeleted: list[str] = []
        
        self.updated: Signal = Signal(str, bool)
        self.deleted: Signal = Signal(str, bool)
        
    def addFile(self, *file: str, updated: bool = True, deleted: bool = True):
        
        files = list(file)
        self.files.extend(files)
        
        if updated:
            self.updatedPaths.extend(files)
            
        if deleted:
            self.deletedPaths.extend(files)
        
        for file in files:
            
            if file in self.areDeleted: # To avoid confusion
                self.areDeleted.remove(file)
            
            if updated:
                self.setLastUpdate(file)
        
    def removeFile(self, *file: str):
        
        files = list(file)
        
        for file in files:
            
            if file in self.files:
                self.files.remove(file)
                
            if file in self.areDeleted:
                self.areDeleted.remove(file)
                
            if file in self.updatedPaths:
                self.updatedPaths.remove(file)
                
            if file in self.deletedPaths:
                self.deletedPaths.remove(file)

    def addFolder(self, *folders: str):

        folders = [str(folder) for folder in list(folders)]
                
    def notify(self, *args):
        
        self.updated.callSync(*args)
        
    def getLastUpdate(self, path: str):
        
        try:
            
            timestamp = os.path.getmtime(path)
        
        except:
            
            timestamp = time.time()
            
        return timestamp
    
    def setLastUpdate(self, path: str):
            
        self.times[path] = self.getLastUpdate(path)
        
        
    def isUpdated(self, path: str):
        
        try:

            if self.times.get(path) < self.getLastUpdate(path):
                
                self.setLastUpdate(path)
                return True
            
            return False
        
        except:
            return False
    
    def isDeleted(self, path: str):
        
        if not os.path.exists(path):
            
            self.removeFile(path)
            return True
        
        return False
    
    def search(self, paths: list[str]):
        
        for path in paths:
            
            if path in self.updatedPaths and path not in self.areDeleted:
                
                if self.isUpdated(path):
                    self.notify(path, os.path.isfile(path))
                
    def lookForDeleted(self, paths: list[str]):
        
        for path in paths:
            
            if path in self.deletedPaths and path not in self.areDeleted:
            
                if self.isDeleted(path):
                    self.deleted.callSync(path)
                
    def run(self):
        
        while self.running:
            
            if self.files:
                self.lookForDeleted(paths=self.files)
                self.search(paths=self.files)
                
            time.sleep(1.0)
            
    def stop(self):
        
        self.running = False

class Bot:
    
    def __init__(self, prefix: str = None, prefixes: tuple | list | set = [], token: str = None):
        '''
        A Bot object representing a Discord Bot User.
        
        Parameters
        ----------
        prefix: `str`
            A prefix for all text commands. It is appended to the `prefixes` list, if provided.
            
        prefixes: `tuple`, `list`, `set`
            A tuple, list or set of multiple unique prefixes. If `prefix` is given, it will be added to the list.
        
        token: `str`
            A Discord user or bot token to connect to the gateway with. If provided, it won't be needed in `Bot.run()`.
        '''

        global globalBot

        if globalBot is None:
            globalBot = self
        
        try:
            fback = inspect.currentframe().f_back
            module = inspect.getmodule(fback)
            mpath = inspect.getsourcefile(module)
            origin = os.path.dirname(mpath)
            
        except:
            origin = None
            mpath = None
        
        self.origin: str = origin # Original path
        self.mainfile: str = mpath # Main file path

        with open(self.mainfile, "r") as f:

            lines: str = f.read()
            lines: list = lines.split("\n")

            needed = False

            try:
                if lines[0].startswith("# Last Lunarcord Execution: "):
                    needed = True
            except:
                needed = False

            if needed:

                lines.pop(0)

                if lines and lines[0] == "":
                    lines.pop(0)

            time = datetime.datetime.now().strftime("%A, %x %X")
            lines = [f"# Last Lunarcord Execution: {time}", ""] + lines
            lines = "\n".join(lines)

        with open(self.mainfile, "w") as f:
            f.write(lines)
        
        __this__ = sys.modules[__name__]
        path = inspect.getsourcefile(__this__)
        
        self.installation: str = os.path.dirname(path)
        
        # self.installation is the path of the current
        # lunarcord installation being used.
        
        #print(self.mainfile)
        #self._loadMainFile()
        
        if self.origin != self.installation:
        
            #registrables = self._loadMainFile()
            #print(registrables)
            
            ...
        
        self.startTimes = 0
        
        prefixes: list = list(prefixes)
        prefixes = [str(prefix) for prefix in prefixes]
        
        if prefix is not None:
            
            if type(prefix) is not str:
                prefix = str(prefix)
            
            prefixes.append(prefix)
            
        prefixes = Utils.removeDuplicates(prefixes)
        
        self.asyncio = asyncio
        self._gateway: Gateway = Gateway(self)
        self.prefixes: list = prefixes
        self.presence: dict = {}
        self.token: str = token

        self.voice: Channel = None
        """The voice channel this bot is currently connected in, if any."""
        
        self.pendingSlashCommands: list[SlashCommand] = []
        self.textCommands: list[TextCommand] = []
        
        #self.loadedFiles: list[str] = []
        self.loadedRecently: dict[str, float] = {}
        self.registered: dict[str, list[Registrable]] = {}
        self.folders: dict[str, list[str]] = {}
        
        self.observer = Observer()
        self.observer.start()
        self.observer.updated.connect(self._fileUpdated)
        self.observer.deleted.connect(self._fileDeleted)
        
    
    @property
    def isBot(self):
        '''
        Whether this is a bot or normal user account.
        '''
        
        return self._gateway.isBot
    
    @property
    def uptime(self):
        
        '''
        The bot's uptime. (Seconds elapsed since start)
        '''
        
        return self._gateway.uptime
        
    @property
    def mention(self):
        
        '''
        Returns a string that can be used to mention this `Bot`, for example `<@12345678>` where `12345678` is the bot's ID.
        '''
        
        return '<@' + str(self.id) + '>'
    
    @property
    def started(self):
        
        '''
        A boolean value representing whether the `Bot` is ready. This is `False` before the `onReady` event is executed, and `True` right after.
        '''
        
        return self._gateway.isReady
        
    async def start(self, token: str = None, delay: float = None, terminate: float = None, loop = None):
        '''
        Initializes the bot, connects to the gateway, and starts the running process.
        
        Parameters
        ----------
        token: `str`
            The bot's token, used to connect. If provided when the `lunarcord.Bot` object was created, this parameter is not needed.

        delay: `float`
            Wait `delay` seconds before starting the bot. By default, do not wait any additional time.
            
        terminate: `float`
            Run for `terminate` seconds, then exit the running process automatically.
            
        loop: `asyncio.AbstractEventLoop`
            The event loop to use. If not given, `asyncio.get_event_loop()` is used instead.
        '''
        
        self.startTimes += 1
        
        if delay is not None:
            await asyncio.sleep(delay)
        
        if self.startTimes > 1: # Don't create new Gateway if it's the first time starting the bot
            self._gateway = Gateway(self, self._gateway)
        
        if self.token is not None:
            token = self.token
            
        else:
            if token is None:
                raise UnauthorizedError()
            
            self.token = token
        
        self._gateway.setToken(token)
        
        existing = await self.manager.slashCommands()
        await self._updateSlashCommands(existing=existing)
                
        def terminateAfter(duration: int | float, gateway: Gateway):
            
            if duration is None:
                return None
            
            time.sleep(duration)
            gateway.stop()
            
        terminateThread = Thread(target=terminateAfter, args=(terminate, self._gateway))
        await self._gateway.start(runAfterThread=terminateThread)
        
    def run(self, token: str = None, delay: float = None, terminate: float = None):
        '''
        Initializes the bot, connects to the gateway, and starts the running process.
        
        Parameters
        ----------
        token: `str`
            The bot's token, used to connect. If provided when the `lunarcord.Bot` object was created, this parameter is not needed.

        delay: `float`
            Wait `delay` seconds before starting the bot. By default, do not wait any additional time.
            
        terminate: `float`
            Run for `terminate` seconds, then exit the process automatically.
        '''
        
        loop = None
        
        try:
            loop = asyncio.get_event_loop()
            
        except:
            loop = None
            
        if not loop:
            
            loop = asyncio.new_event_loop()
        
        loop.create_task(
            
            self.start(
                token = token,
                delay = delay,
                terminate = terminate
            )
            
        )
        
        loop.run_forever()
        
    def stop(self):
        '''
        Forcefully stops and terminates the bot's process, shutting down its connection with Discord.
        '''
        
        self._gateway.stop()
        self.observer.stop()

    @property 
    def eventloop(self):
        if not hasattr(self, '__eventloop__') or self.__eventloop__ is None:
            loop = asyncio.new_event_loop()
            loop.run_forever()
            self.__eventloop__ = loop
            return loop
        else:
            return self.__eventloop__
        
    async def _authenticate(self):
        
        try:
            bot = await self._gateway.manager.clientInfo()
        except:
            return
        
        user: dict = bot.get("bot")
        
        self.user = User(self, user)
        await self.user._proc()

        self.owner = bot.get("owner")
        self.id = self.user.id
        self.displayName = self.user.displayName
        self.username = self.user.username
        self.name = self.username

        
        if self.displayName is not None:
            self.displayName: str = self.displayName
            self.name = self.displayName
            
        if self.id:
            self.id = int(self.id)

        self.owner: User = await self.fetchUser(
            id = self.owner.get("id")
        )
        
    @property
    def manager(self):
        manager: Manager = Utils.manager(self)
        return manager
    
    @property
    def tokenPrefix(self):
        '''
        The token's prefix ("Bot" or "Bearer")
        '''
        
        return 'Bot' if self.isBot else 'Bearer'
    
    @property
    def fullToken(self):
        '''
        The full token including its prefix, eg "Bearer {Token}" or "Bot {Token}"
        '''
        
        return self.tokenPrefix + ' ' + self.token
        
    def event(self, type: int = None, **filters):
        '''
        Create an event listener. The type represents the type of event to listen for. It's not required, and if not provided, the event type will be based on your listener function's name - for example, if your function's name is "on_message", it will listen for new messages.
        
        Parameters
        ----------
        type: `int`
            The event type for the listener. Examples: `Lunarcord.ON_START`, `Lunarcord.ON_MESSAGE`...

        filters: `any`
            Additional parameters used to filter the listener's usage.
        '''
        
        def inner(func):
            name = func.__name__.lower()
            
            event = __createEvent__(
                bot = self,
                callback = func,
                name = name,
                type = type
            )
            
            return event
                
        return inner
    
    def register(self, registrable: Registrable, name: str = ...):
        '''
        Registers a new, registrable object.
        
        Parameters
        ----------
        registrable: `lunarcord.Registrable`
            The item to register. This must have _register method.
        '''
        
        item = type(registrable)
        
        if not issubclass(item, Registrable):
            raise RegisterError('notRegistrable')
        
        if not hasattr(item, '_register'):
            raise RegisterError('noAttribute')
            
        if registrable.registered:
            raise RegisterError('registered')
        
        registrable._register(self, name)
        
    def unregister(self, registrable: Registrable):
        '''
        Un-registers an already registered registrable object.
        
        Parameters
        ----------
        registrable: `lunarcord.Registrable`
            The item to register. This must have _unregister method.
        '''
        
        item = type(registrable)
        
        if not issubclass(item, Registrable):
            raise UnregisterError('notRegistrable')
        
        if not hasattr(item, '_unregister'):
            raise UnregisterError('noAttribute')
            
        if registrable not in self.registered:
            raise UnregisterError('notRegistered')
        
        registrable._unregister(self)
        
    def reregister(self, registrable: Registrable):
        '''
        Unregisters and registers again a registered object.
        
        Parameters
        ----------
        registrable: `lunarcord.Registrable`
            The item to re-register. This must have _reregister method.
        '''
        
        item = type(registrable)
        
        if not issubclass(item, Registrable):
            raise ReregisterError('notRegistrable')
        
        if not hasattr(item, '_reregister'):
            raise ReregisterError('noAttribute')
        
        '''if registrable not in self.registered:
            raise ReregisterError('notRegistered')'''
        
        registrable._reregister()
        
    
    def reset(self, textCommands: bool = True, slashCommands: bool = True, events: bool = True):
        
        if textCommands:
            self.textCommands = []
            
        if slashCommands:
            self.pendingSlashCommands = []
            
        if events:
            
            for container in ['onStartFunctions', 'onMessageFunctions', 'channelUpdateFunctions', 'typingStartedFunctions', 'presenceUpdateFunctions']:
                setattr(self._gateway, container, [])
                
                
    def addPrefix(self, *prefix: str):
        '''
        Adds one or more new `prefixes` to the bot's text command prefixes.
        If one of the prefixes already exists, the bot completely ignores it (and goes on with the next, if it exists).
        
        Parameters
        ----------
        prefix: `str`
            The prefix (or prefixes) to add to the list of all bot prefixes.
        '''
        
        prefixes = list(prefix)
        
        for prefix in prefixes:
        
            if type(prefix) is not str:
                
                try:
                    prefix = str(prefix)
                    
                except:
                    continue
                
            prefix: str = prefix.strip()
            
            if prefix in self.prefixes:
                continue
            
            self.prefixes.append(prefix)
        
        
    def removePrefix(self, *prefix: str):
        '''
        Removes one or more already existing `prefixes` from the bot's text command prefixes.
        If the prefix doesn't already exist, a `ValueError` will be raised.
        
        Parameters
        ----------
        *prefix: `str`
            The prefix(es) to remove from the list of bot prefixes.
        '''
        
        prefixes = list(prefix)
        
        for prefix in prefixes:
        
            if type(prefix) is not str:
                
                try:
                    prefix = str(prefix)
                    
                except:
                    continue
                
            prefix: str = prefix.strip()
                
            if prefix not in self.prefixes:
                raise ValueError(f'"{prefix}" not in prefixes')
                
            self.prefixes.remove(prefix)
            
    def addMentionedPrefix(self):
        
        '''
        Creates an `onMention` prefix for the bot.
        Using this will allow users to ping the bot as a prefix for text commands.
        '''
        
        self.addPrefix(self.mention)
        
    def removeMentionedPrefix(self):
        
        '''
        Deletes an already existing `onMention` prefix from this bot.
        Mention prefixes allow users to ping the bot in order to execute text commands.
        '''
        
        try:
            
            self.removePrefix(self.mention)
            
        except:
            
            raise ValueError(f'No mention prefix to remove')
            
            
    def hasPrefix(self, *prefix: str):
        '''
        Checks if the bot has any of the given prefix(es) set to it.
        
        Parameters
        ----------
        *prefix: `str`
            The prefix or prefixes to check against.
            
        Returns
        -------
        exists: `bool`
            `True` if one of the prefixes exists. `False` if none of them do.
        '''
        
        if len(prefix) == 1:
            prefixes = [prefix[0]]
            
        else:
            prefixes = list(prefix)
            
        del prefix
        
        for prefix in prefixes:
            
            if prefix in self._gateway.prefixes:
                return True
            
        return False
        
        
    
    def slashCommand(self, name: str = None, description: str = None, guilds: list[int] = None, cooldown: int | float = None):
        '''
        Create a bot slash command. If not given, the name will be taken from the function name.
        
        Parameters
        ----------
        name: `str`
            The slash command name which will be displayed on Discord. If None, it will be the decorated function's name.
            
        description: `str`
            The informative description for the slash command. If not given, it will be the callback function's docstring.
            
        guilds: `list`
            A list of guild (server) IDs that this command should be available in. If not given, it will be available everywhere.

        cooldown: `int`, `float`
            A command cooldown. This will be useful if you want to use `Interaction.cooldown`.
        '''
        
        if callable(name):
            func = name
            name = func.__name__
            description = func.__doc__
            
            slashCommand = __createSlashCommand__(
                bot = self,
                callback = func,
                name = name,
                description = description,
                guilds = guilds,
                cooldown = cooldown
            )
            
            return slashCommand
        
        def inner(func):
            
            slashCommand = __createSlashCommand__(
                bot = self,
                callback = func,
                name = name,
                description = description,
            )
                    
            return slashCommand
                
        return inner
    
    def textCommand(self, name: str = None, description: str = None, aliases: list[str] = [], cooldown: int | float = None):
        '''
        Create a bot text command. If not given, the name will be taken from the callback's name.
        
        Parameters
        ----------
        name: `str`
            The text command's name, which will cause it to be triggered. If None, it will be based on the callback function's name.
            
        description: `str`
            The informative description for the text command, shown in the auto-help (if it exists). If not given, it will be the callback function's docstring.
            
        aliases: `list[str]`
            Additional names that can also trigger the command's execution.

        cooldown: `int`, `float`
            A command cooldown. This will be useful if you want to use `Context.cooldown`.
        '''
        return textCommand(name, description, aliases, cooldown)
    
    def task(self, name: str = None, autorun: bool = True):
        
        '''
        Create a new task and start its execution in another thread. If `bot` is not provided and this is never registered from a cog or with `Bot.register()`, the task will never be ran. As long as the task is registered to some bot, the given bot will take care of it immediately.
        
        Parameters
        ----------
        activity: `callable`
            Any type of callable to be ran as this Task's main activity. This is required.
            
        name: `str`
            A name for this task. If not given, it'll be generated using the activity's name.
            
        autorun: `bool`
            If this is set to `False`, the task will not be executed by the bot automatically, but by you (eg. if the activity name is `myActivity`, then `myActivity()`)
            
        bot: `Bot`
            The bot that should take care of this task and its activity. If not given, the task can't start.
        '''
        
        def create(activity):
            
            nonlocal self, name, autorun
        
            return __createTask__(
                bot = self,
                activity = activity,
                name = name,
                autorun = autorun
            )
            
        return create
    
    def loop(self, name: NameLike[str] = None, every: TimeLike[int | float] = 1, iterable: Iterable = None):
        
        '''
        Create a new loop and start it in another thread. If `bot` is not provided and this is never registered from a cog or with `Bot.register()`, the loop will never start. As long as this loop is registered to some bot, the bot will take care of it immediately.
        
        Parameters
        ----------
        name: `NameLike`
            A name for this task. If not given, it'll be generated using the activity's name.
            
        iterable: `Iterable`
            An iterable (for example a `list`) to pass items from in every iteration. This can be useful for automatically updating the bot's activity, and not only.
            
        every: `TimeLike`
            Seconds to wait before every execution of the loop's activity.
        '''
        
        def create(activity):
            
            nonlocal name, every
        
            return __createLoop__(
                bot = self,
                activity = activity,
                name = name,
                every = every,
                iterable = iterable
            )
            
        return create
    
    def userConfig(self, **pairs):
        """Creates a new `UserConfiguration` and adds it to the bot. Useful if you don't want to create it in a seperate cog."""
        config = userConfig(pairs)
        config._register(self)
        return config
        
    def _getCommandsOf(self, path: str) -> list[Registrable]:
        
        '''
        Get all attributes of type `SlashCommand`, `TextCommand` or `Event` in the module represented by the given `path`.
        
        Parameters
        ----------
        path: `str`
            The path of the target module.
            
        Returns
        -------
        commands: `list`
            A list of all `lunarcord.SlashCommand`/`lunarcord.TextCommand`/`lunarcord.Event` objects in the module.
        '''
        
        if not isfile(path):
            path += '.py'
            
            if not isfile(path):
                return []
            
        head, tail = split(path)
        initFile = join(head, '__init__.py')
        locations = []
        
        if isfile(initFile):
            hasInit = True
            locations.append(initFile)
            
        
        moduleName = split(path)[0].replace('.py', '')
        module = Utils.module(moduleName, path, locations)

        for x in ("bot", "client"):
            
            if hasattr(module, x) and getattr(module, x) is ...:
                
                setattr(module, x, self)
        
        commands = []
        
        for name in dir(module):
            item = getattr(module, name)
            
            if issubclass(type(item), (Registrable, BaseConfiguration)):
                item.varname = name
                commands.append(item)
            
        return commands
    
    def _loadModuleFrom(self, __path: str, name = 'LunarcordModule', execute: bool = True):
        
        spec = spec_from_file_location(name, __path)
        module = module_from_spec(spec)
        
        if execute:
            spec.loader.exec_module(module)
        
        return module
    
    def _loadMainFile(self):
        
        return None
        
        time.sleep(1)
        
        module = self._loadModuleFrom(
            self.mainfile,
            name = 'LunarcordMain'
        )
        
        regs = []
            
        return regs
            
    
    def loadFile(self, path: str, exceptions: list[str] = [], ignoreExisting: bool = False):
        
        '''
        Load all slash and text commands as well as events in the module representing the given path.
        
        You can consider this some sort of "cog".
        
        Parameters
        ----------
        path: `str`
            The path of the module containing `lunarcord.SlashCommand`, `lunarcord.TextCommand` and/or `lunarcord.Event` objects.
            
        exceptions: `list[str]`
            A list of command or event names. All registrations in this file with a name contained in this list will be ignored.
            
        Returns
        -------
        commands: `tuple[list]`
            A list of all commands, events, etc... successfully added to the bot.
        '''

        try:

            from .ui import View
            
            if path not in self.registered:
                self.registered[path] = []
            
            successful = []
            commands = self._getCommandsOf(path)
            namedCommands: dict[str, Registrable] = {x.__name__: x for x in self.registered[path] if hasattr(x, "__name__")}
            
            for command in commands:
                    
                if ignoreExisting:

                    if hasattr(command, "name") and command.name in namedCommands:

                        if callable(command):

                            existing = namedCommands.get(command.__name__)
                            existingSource = Utils.functionToString(existing, imports=False)
                            source = Utils.functionToString(command, imports=False)

                            if source == existingSource:
                                continue # Continue because it already exists
                
                try:
                    if ((hasattr(command, 'name'))  and(command.name in exceptions)):
                        continue # Ignore command because it is in exceptions.
                    
                    if True: # Treat Registrables
                        self.register(command, command.varname)
                    
                    self.registered[path].append(command) # Append to the list of all registrables.
                    successful.append(command) # Append to the list of successfully added items.
                    
                except:
                    continue
        
            self.observer.addFile(path)

            return (
                [x for x in successful if isinstance(x, TextCommand)], 
                [x for x in successful if isinstance(x, SlashCommand)], 
                [x for x in successful if isinstance(x, Event)], 
                [x for x in successful if isinstance(x, View)], 
                [x for x in successful if isinstance(x, Task)], 
                [x for x in successful if isinstance(x, Loop)], 
                [x for x in successful if isinstance(x, UserConfiguration)]
            )
        
        except:
            error = Utils.exceptionError()
            print(f"[LUNARCORD] File \"{path}\" raised an exception of type {error}")

    def unloadFile(self, path: str) -> list[Registrable]:
        
        '''
        Un-load all previously loaded slash and text commands as well as events in the module representing the given path.
        
        Parameters
        ----------
        path: `str`
            The path of the module containing `lunarcord.SlashCommand`, `lunarcord.TextCommand` and/or `lunarcord.Event` objects.
        
        Returns
        -------
        commands: `tuple[list]`
            A list of all commands, events, etc... that were removed from the bot.
        '''

        from .ui import View
        
        if path not in self.registered:
            self.registered[path] = []
            
        successful = []
        
        for regist in self.registered[path]:
            
            try:
                
                gw = self._gateway

                if False: # Disabled stuff
                
                    try: self.unregister(regist)
                    except: pass # This doesnt even work I think
                
                for l in [
                    self.textCommands, 
                    gw.slashCommands, 
                    gw.onStartFunctions, 
                    gw.onMessageFunctions, 
                    gw.reactionAddFunctions, 
                    gw.channelUpdateFunctions, 
                    gw.channelCreateFunctions, 
                    gw.channelDeleteFunctions, 
                    gw.messagePinnedFunctions, 
                    gw.typingStartedFunctions, 
                    gw.typingStoppedFunctions, 
                    gw.messageDeletedFunctions, 
                    gw.messageUpdatedFunctions, 
                    gw.presenceUpdateFunctions, 
                    gw.reactionRemoveFunctions, 
                    gw.commandInvokedFunctions, 
                    gw.invalidCommandFunctions, 
                    gw.memberLeaveFunctions,
                    gw.memberJoinFunctions,
                    gw.memberUpdateFunctions, 
                    gw.commandErrorFunctions,
                    gw.commandCooldownFunctions,
                    gw.views, gw.tasks, gw.loops
                ]:
                    
                    found = False
                    
                    if regist in l:

                        found = True
                        l.remove(regist)
                        
                    if found:

                        successful.append(regist)
                        
                        try: gw.views.remove(regist)
                        except: pass

                        if hasattr(regist, "_unregister"):
                            try: regist._unregister()
                            except: pass
                
            except:
                ... # Ignore error and continue
        
        self.observer.removeFile(path)
        self.registered[path] = []

        return (
            [x for x in successful if isinstance(x, TextCommand)], 
            [x for x in successful if isinstance(x, SlashCommand)], 
            [x for x in successful if isinstance(x, Event)], 
            [x for x in successful if isinstance(x, View)], 
            [x for x in successful if isinstance(x, Task)], 
            [x for x in successful if isinstance(x, Loop)], 
            [x for x in successful if isinstance(x, UserConfiguration)]
        )
        
    
    def reloadFile(self, path: str):
        
        '''
        Re-load all previously loaded slash and text commands as well as events in the module representing the given path.
        
        Parameters
        ----------
        path: `str`
            The path of the module containing `lunarcord.SlashCommand`, `lunarcord.TextCommand` and/or `lunarcord.Event` objects.

        Returns
        -------
        commands: `tuple[list]`
            A list of all commands, events, etc... that have been successfully added to the bot.
        '''
        self.unloadFile(path)
        return self.loadFile(path, ignoreExisting=False)
    
    def unload(self):
        '''
        Un-load all previously loaded files and folders, removing all commands or `lunarcord.Registrable` objects of any subclassed type.
        '''
        
        unloaded = []
        
        for file in self.registered:
            
            commands = self.unloadFile(file)
            unloaded.extend(commands)
            
        return unloaded
    
    def reload(self) -> list[Registrable]:
        '''
        Re-load all previously loaded files and folders, updating and adding any new commands or `lunarcord.Registrable` objects of any subclassed type.
        '''
        
        reloaded = []
        
        for file in self.registered:
            
            files = self.reloadFile(file)
            reloaded.extend(files)
            
        return reloaded
                
    def loadFolder(self, directory: str, ignoreInit: bool = True, fileExceptions: list[str] = [], commandExceptions: list[str] = [], *, recursive: bool = True):
        
        '''
        Go through all the files in the given folder, and add their slash/text commands and events to the bot.
        
        This is almost the same as doing:
        
        ```
        for file in os.listdir(directory):
            path = os.path.join(directory, file)
            bot.loadFile(path)
        ```
        
        ... but with some extra additions to make your life easier.
        
        Parameters
        ----------
        directory: `str`
            The path of the folder to load commands, views and events from.
            
        ignoreInit: `bool`
            Whether to ignore the folder's `__init__.py` file, if it exists. By default, this is `True`.
            
        fileExceptions: `list[str]`
            A list of file paths. All files in this folder that have a name contained in this list will be ignored.
            
        commandExceptions: `list[str]`
            A list of command or event names. All commands/events which have a name contained in this list will be ignored.
            
        recursive: `bool`
            Whether to also load files of sub-folders of this folder. This is True, by default.
            
        Returns
        -------
        registrations: `list`
            A list of all commands, views and events that have been successfully added to the bot.
        '''
        
        def checklist(item):
            if not isinstance(item, list):
                if hasattr(item, '__iter__'): # is iterable
                    item = list(item)
                else:
                    if item is None:
                        item = []
                    else:
                        item = [item]
            return item
        
        fileExceptions = checklist(fileExceptions)
        commandExceptions = checklist(commandExceptions)
                
        if ignoreInit:
            fileExceptions.append('__init__.py')
            
        fileExceptions.append('__pycache__')
        
        commands = [] # Create empty list of successes.
        files = listdir(directory) # Get all files of the directory.
        filenames = [] # List to be used later, of all files in this folder
        
        for file in files:
            
            path = join(directory, file) # Retrieve the full path of module.
            filenames.append(path) # Make use of filenames 
            
            if (path in fileExceptions) or (file in fileExceptions):
                continue # Ignore the command, as expected.
            
            if os.path.isdir(path):
                
                if recursive:
                    
                    recursed = self.loadFolder(path, ignoreInit, fileExceptions, commandExceptions)
                    commands.extend(recursed) # Add all recursively loaded commands to the list
                
                continue
            
            try:
                successes = self.loadFile(path, commandExceptions) # Add and get all command in the file.
                commands.extend(successes) # Append all commands added to list of successfully added commands.
                
            except:
                continue # Ignore errors and continue with next file.
        
        self.observer.addFile(directory) # Adds to the observed files
        self.folders[directory] = filenames # Adds to the loaded folders
        return commands # Return all successfully added commands.
    
    def unloadFolder(self, directory: str, ignoreInit: bool = True, fileExceptions: list[str] = [], commandExceptions: list[str] = [], *, recursive: bool = True):
        
        '''
        Go through all the files in the given folder, and remove their slash/text commands and events from the bot, if they are in.
        
        This is almost the same as doing:
        
        ```
        for file in os.listdir(directory):
            path = os.path.join(directory, file)
            bot.unloadFile(path)
        ```
        
        ... but with some extra additions to make your life easier.
        
        Parameters
        ----------
        directory: `str`
            The path of the folder to unload commands, views and events from.
            
        ignoreInit: `bool`
            Whether to ignore the folder's `__init__.py` file, if it exists. By default, this is `True`.
            
        fileExceptions: `list[str]`
            A list of file paths. All files in this folder that have a name contained in this list will be ignored.
            
        commandExceptions: `list[str]`
            A list of command or event names. All commands/events which have a name contained in this list will be ignored.
            
        recursive: `bool`
            Whether to also unload files of sub-folders of this folder. This is True, by default.
            
        Returns
        -------
        registrations: `list`
            A list of all commands, views and events that have been successfully removed from the bot.
        '''
        
        # Time for some copypasting from loadFile
        
        def checklist(item):
            if not isinstance(item, list):
                if hasattr(item, '__iter__'): # is iterable
                    item = list(item)
                else:
                    if item is None:
                        item = []
                    else:
                        item = [item]
            return item
        
        fileExceptions = checklist(fileExceptions)
        commandExceptions = checklist(commandExceptions)
                
        if ignoreInit:
            fileExceptions.append('__init__.py')
        
        commands = [] # Create empty list of successes.
        files = listdir(directory) # Get all files of the directory.
        
        for file in files:
            
            path = join(directory, file) # Retrieve the full path of module.
            
            if (path in fileExceptions) or (file in fileExceptions):
                continue # Ignore the command, as expected.
            
            if os.path.isdir(path):
                
                if recursive:
                    
                    recursed = self.unloadFolder(path, ignoreInit, fileExceptions, commandExceptions)
                    commands.extend(recursed) # Add all recursively loaded commands to the list
                
                continue
            
            try:
                successes = self.unloadFile(path, commandExceptions) # Add and get all command in the file.
                commands.extend(successes) # Append all commands added to list of successfully added commands.
                
            except:
                continue # Ignore errors and continue with next file.
            
        self.observer.removeFile(directory) # Removes from observed files
        self.folders.pop(directory, None) # Removes from loaded folders
        return commands # Return all successfully removed commands.
    
    def reloadFolder(self, directory: str, ignoreInit: bool = True, fileExceptions: list[str] = [], commandExceptions: list[str] = [], *, recursive: bool = True):
        
        '''
        Go through all the files in the given folder, reloading and updating all their slash/text commands and events.
        
        This is almost the same as doing:
        
        ```
        for file in os.listdir(directory):
            path = os.path.join(directory, file)
            bot.reloadFile(path)
        ```
        
        ... but with some extra additions to make your life easier.
        
        Parameters
        ----------
        directory: `str`
            The path of the folder to load commands and events from.
            
        ignoreInit: `bool`
            Whether to ignore the folder's `__init__.py` file, if it exists. By default, this is `True`.
            
        fileExceptions: `list[str]`
            A list of file paths. All files in this folder that have a name contained in this list will be ignored.
            
        commandExceptions: `list[str]`
            A list of command or event names. All commands/events which have a name contained in this list will be ignored.
            
        recursive: `bool`
            Whether to also load files of sub-folders of this folder. This is True, by default.
            
        Returns
        -------
        registrations: `list`
            A list of all commands, views and events that have been successfully added to the bot.
        '''
        
        def checklist(item):
            if not isinstance(item, list):
                if hasattr(item, '__iter__'): # is iterable
                    item = list(item)
                else:
                    if item is None:
                        item = []
                    else:
                        item = [item]
            return item
        
        fileExceptions = checklist(fileExceptions)
        commandExceptions = checklist(commandExceptions)
                
        if ignoreInit:
            fileExceptions.append('__init__.py')
        
        commands = [] # Create empty list of successes.
        files = listdir(directory) # Get all files of the directory.
        
        for file in files:
            path = join(directory, file) # Retrieve the full path of module.
            
            if (path in fileExceptions) or (file in fileExceptions):
                continue # Ignore the command, as expected.
            
            if os.path.isdir(path):
                
                if recursive:
                    
                    recursed = self.reloadFolder(path, ignoreInit, fileExceptions, commandExceptions)
                    commands.extend(recursed) # Add all recursively loaded commands to the list
                
                continue
            
            try:
                successes = self.reloadFile(path, commandExceptions) # Add and get all command in the file.
                commands.extend(successes) # Append all commands added to list of successfully reloaded commands.
                
            except:
                continue # Ignore errors and continue with next file.
            
        return commands # Return all successfully added commands.
    
    def loadFolders(self, *folders: str):

        """
        Loads all provided folders using a for loop and `Bot.loadFolder`.
        If you want more control over the way your folders are loaded (additional parameters), you should manually use `Bot.loadFolder` for each of your folders.
        Additionally, this will ignore any errors and exceptions normally raised by `loadFolder`.

        Returns
        -------
        registrations: `list`
            A list of all commands, views and events that have been successfully added to the bot.
        """

        regist = []

        for folder in folders:

            try:
                regist.extend(
                    self.loadFolder(folder)
                )

            except:
                continue

        return regist
    
    def _fileUpdated(self, path: str):
        
        '''
        Called when an observed file or folder is updated, from the `Observer`'s `updated` signal.
        '''
        
        try:

            if Utils.isFolder(path):
                return self._folderUpdated(path)
            
            self._reloadAndCount(path)
            
        except:
            # print(f'[!] Failed to update commands of "{path}".')
            pass

    def _reloadAndCount(self, path: str, load: bool = False, delete: bool = False):

        method = self.reloadFile
        use = "Updated"
        beforepath = "in"

        if load:

            method = self.loadFile
            use = "Loaded"
            beforepath = "from"

            timestamp = self.loadedRecently.get(path)

            if timestamp and timestamp - time.time() <= 1.0:
                return

        elif delete:
            
            method = self.unloadFile
            use = "Deleted"
            beforepath = "from"

        text, slash, events, views, tasks, loops, configs = method(path)
        text, slash, events, views, tasks, loops, configs = len(text), len(slash), len(events), len(views), len(tasks), len(loops), len(configs)

        if (not load) or (delete):
            self._updateSlashCommandsSync()

        items = ""
        data = []

        for x in (

            ("text command", text),
            ("slash command", slash),
            ("event", events),
            ("view", views),
            ("task", tasks),
            ("loop", loops),
            ("config", configs)

        ):

            name, value = x

            if value > 0:
                s = Utils.ending(value)
                string = f"{value} {name}{s}"
                data.append(string)

        if data:

            useand = False
            
            if len(data) > 1:
                remains = data.pop()
                useand = True

            items = ", ".join(data)

            if useand:
                items += f" and {remains}"

        if items == "":
            items = "absolutely nothing"

        if items != "":

            try:
                path = path.replace()
                print('[LUNARCORD] {} {} {} "{}".'.format(use, items, beforepath, path))
            except:
                pass

        if load:
            self.loadedRecently[path] = time.time()

    def _folderUpdated(self, path: str):
        
        folder = self.folders.get(path, [])
        files = [join(path, file) for file in listdir(path)]
        new = [file for file in files if file not in folder]

        for x in new:

            if Utils.isFolder(x):
                if os.path.basename(x) != "__pycache__":
                    self.folders[x] = []
                    self.observer.addFile(x)
                    print(f"[LUNARCORD] Registered new subfolder of \"{path.replace("\\", "/")}\": \"{x.replace("\\", "/")}\".")
            else:
                self._reloadAndCount(x, load=True)
        
        if new:
            amount = len(new)
            s = Utils.ending(amount)
        
    def _fileDeleted(self, path: str):
        
        '''
        Called when an observed file or folder is deleted, from the `Observer`'s `deleted` signal.
        '''
        
        try:
            if path not in self.folders:
                self._reloadAndCount(path, delete=True)
            else:
                self.folders.pop(path, ...)
            
        except:
            ...
    
    def setStatus(self, type: str = None, activity: Activity = None):

        from .basetypes import Status
        
        invalidType = None

        if isinstance(type, Status):

            status: Status = type
            
            if status.activity is not None:
                
                activity = status.activity

            mobile = status.mobile if isinstance(status.mobile, bool) else False
            type = status.type
        
        if not isinstance(activity, Activity) and activity is not None:
            
            if isinstance(activity, str):
                
                found = False
                
                isact = activity.lower().startswith
                stringtypes = (('playing', Playing), ('watching', Watching), ('streaming', Streaming), ('listening to', Listening), ('listeningto', Listening), ('listening', Listening))
                
                for stringtype in stringtypes:
                    stringtype, classtype = stringtype
                    
                    if isact(stringtype):
                        
                        game: str = Utils.removeFirst(stringtype, activity)
                        activity = classtype(game.strip())
                        found = True
                        break
                    
                if not found:
                    activity = Playing(activity)
                    
        if type not in ('online', 'idle', 'dnd', 'invisible', None):
            
            if not isinstance(type, Status):
                invalidType = 1
            
        if invalidType is not None:
            raise StatusError(invalidType)
        
        if activity is not None:
            activities = [activity._toJson()]
            
        else:
            if not hasattr(self, '__activity__') or self.__activity__ is None:
                activities = []
            else:
                if isinstance(self.__activity__, list) and len(self.__activity__) < 1:
                    activities = [self.__activity__]
                else:
                    activities = [self.__activity__]
                
        if type is None:
            if not hasattr(self, '__statustype__'):
                type = 'online'
                
            else:
                type = self.__statustype__ if self.__statustype__ is not None else 'online'
            
        presence = {
            'status': type,
            'afk': False,
            'activities': activities
        }
        
        coro = self._gateway.changeStatus(
            activities=activities,
            status=type
        )
        
        self._gateway.doTask(coro)
            
        try:
            self.__activity__ = activities[0]
        except:
            ... # Leave activity as is
        self.__statustype__ = type
        self.presence = presence
        
    @property
    def activity(self):
        '''
        The bot's activity. Must be a `lunarcord.Activity` (for example `lunarcord.Activity(lunarcord.PLAYING, 'with Lunarcord')` OR a `str` such as `"Playing with Lunarcord"`).
        
        When this property is changed (`bot.activity = ...`), the bot's status will instantly be updated - if it's valid.
        '''
        
        return self.__activity__
    
    @activity.setter
    def activity(self, value):
        self.setStatus(activity=value)
        
    @activity.deleter
    def activity(self):
        self.__activity__ = None
        self.setStatus(None, None)
        
    @property
    def status(self):
        '''
        The bot's status type. It can be `lunarcord.ONLINE`, `lunarcord.DND`, `LUNARCORD.IDLE`, `lunarcord.OFFLINE` or an alias of these. It can also be a `string` (such as `"online"`, `"offline"`, `"idle"`, `"dnd"`).
        
        When this property is changed (`bot.status = ...`), the bot's status will instantly be updated - if it's valid.
        '''
        
        return self.__statustype__
    
    @status.setter
    def status(self, value):
        self.setStatus(value, None)
        
    @status.deleter
    def status(self):
        self.__statustype__ = 'online'
        self.setStatus(None, None)
        
    def getUser(self, id: int) -> User:
        
        '''
        Get and return the `User` of the corresponding `id` from the cache, if found.
        
        Parameters
        ----------
        id: `int`
            The target user's ID. Must be an integer or convertible to integer.
            
        Returns
        -------
        user: `User`
            A `lunarcord.User` object representing the target user, or `None` if not found.
        '''
        
        if type(id) is not int:
            try:
                id = int(id)
                
            except:
                return None
            
        for user in self._gateway.users:
            if user.id == id:
                return user
            
    async def fetchUser(self, id: int) -> User:
        
        '''
        Get and return the `User` of the corresponding `id` from the cache, or create it on request if not found.
        
        Parameters
        ----------
        id: `int`
            The target user's ID. Must be an integer or convertible to integer.
            
        Returns
        -------
        user: `User`
            A `lunarcord.User` object representing the target user.
        '''
        
        if type(id) is not int:
            
            try:
                id = int(id)
                
            except:
                return None
            
        found = self.getUser(id)
        
        if found is not None:
            return found
        
        try:
        
            user = await User.fromID(
                bot = self,
                user = id
            )
            
        except:
            
            user = None
            
        return user
        
    def getChannel(self, id: int) -> Channel:
        
        '''
        Get and return the `Channel` of the corresponding `id` from the cache, if found.
        
        Parameters
        ----------
        id: `int`
            The target channel's ID. Must be an integer or convertible to integer.
            
        Returns
        -------
        channel: `Channel`
            A `lunarcord.Channel` object representing the target messageable, or `None` if not found.
        '''
        
        if type(id) is not int:
            try:
                id = int(id)
                
            except:
                return None
            
        for channel in self._gateway.channels:
            if channel.id == id:
                return channel
            
    async def fetchChannel(self, id: int) -> Channel:
        
        '''
        Get and return the `Channel` of the corresponding `id` from the cache, or create it on request if not found.
        
        Parameters
        ----------
        id: `int`
            The target channel's ID. Must be an integer or convertible to integer.
            
        Returns
        -------
        channel: `Channel`
            A `lunarcord.Channel` object representing the target messageable.
        '''
        
        if type(id) is not int:
            try:
                id = int(id)
                
            except:
                return None
            
        found = self.getChannel(id)
        
        if found is not None:
            return found
        
        try:
            
            channel = await Channel.fromID(
                bot = self,
                channel = id
            )
            
        except:
            
            channel = None
        
        return channel
        
    def getMessage(self, id: int) -> Message:
        
        '''
        Get and return the `Message` of the corresponding `id` from the cache, if found.
        
        Parameters
        ----------
        id: `int`
            The target message's ID. Must be an integer or convertible to integer.
            
        Returns
        -------
        message: `Message`
            A `lunarcord.Message` object representing the target message, or `None` if not found.
        '''
        
        if type(id) is not int:
            try:
                id = int(id)
                
            except:
                return None
            
        for message in self._gateway.messages:
            if message.id == id:
                return message
            
    async def fetchMessage(self, channel: int, id: int) -> Message:
        
        '''
        Get and return the `Message` of the corresponding `id` from the cache, or create it on request if not found.
        
        Parameters
        ----------
        channel: `int`
            The channel ID in which the message is located. Must be an integer or convertible to integer.
            
        id: `int`
            The target message's ID. Must be an integer or convertible to integer.
            
        Returns
        -------
        message: `Message`
            A `lunarcord.Message` object representing the target message.
        '''
        
        if type(id) is not int:
            try:
                id = int(id)
                
            except:
                return None
            
        found = self.getMessage(id)
        
        if found is not None:
            return found
        
        try:
        
            message = await Message.fromID(
                bot = self,
                channel = channel,
                message = id
            )
            
        except:
            
            message = None
            
        return message
    
    def getGuild(self, id: int) -> Guild:
        
        '''
        Get and return the `Guild` of the corresponding `id` from the cache, if found.
        
        Parameters
        ----------
        id: `int`
            The target guild's ID. Must be an integer or convertible to integer.
            
        Returns
        -------
        guild: `Guild`
            A `lunarcord.Guild` object representing the target guild, or `None` if not found.
        '''
        
        if type(id) is not int:
            try:
                id = int(id)
                
            except:
                return None
            
        for guild in self._gateway.guilds:
            if guild.id == id:
                return guild
            
    async def fetchGuild(self, id: int) -> Guild:
        
        '''
        Get and return the `Guild` of the corresponding `id` from the cache, or create it on request if not found.
        
        Parameters
        ----------
        id: `int`
            The target Guild's ID. Must be an integer or convertible to integer.
            
        Returns
        -------
        guild: `Guild`
            A `lunarcord.Guild` object representing the target guild/server.
        '''
        
        if type(id) is not int:
            
            try:
                id = int(id)
                
            except:
                return
            
        found = self.getGuild(id)
        
        if type(found) is Guild:
            return found
        
        try:
        
            guild = await Guild.fromID(
                bot = self,
                guild = id
            )
            
        except:
            
            guild = None
            
        return guild
    
    def getRole(self, id: int) -> Role | None:
        
        '''
        Get and return the `Role` of the corresponding `id` from the cache, if found.
        
        Parameters
        ----------
        id: `int`
            The target role's ID. Must be an integer or convertible to integer.
            
        Returns
        -------
        role: `Role`
            A `lunarcord.Role` object representing the target role, or `None` if not found.
        '''
        
        if type(id) is not int:
            try:
                id = int(id)
                
            except:
                return None
            
        for role in self._gateway.roles:
            if role.id == id:
                return role
            
    def getMember(self, guild: Guild | int, id: int) -> Member | None:

        """
        Get and return the `Member` of the corresponding `id` in the given `guild` from the cache, if found.
        
        Parameters
        ----------
        guild: `Guild`, `int`
            The guild this member belongs to. Must be a guild, an integer, or a convertible to integer.
        id: `int`
            The target user's ID. Must be an integer or convertible to integer.
            
        Returns
        -------
        member: `Member`
            A `lunarcord.Member` object representing the target member, or `None` if not found.
        """

        if type(guild) is not Guild:
            guild = self.getGuild(guild)

        if guild is None:
            return
        
        try:
            id = int(id)
        except:
            return
        
        for member in guild.members:
            if member.id == id:
                return member
            
    async def fetchMember(self, guild: Guild | int, id: int) -> Member:

        """
        Get and return the `Member` of the corresponding `id` from the cache, or create it on request if not found.
        
        Parameters
        ----------
        guild: `Guild`, `int`
            The guild this member is part of. Must be a `Guild` object, an integer, or convertible to integer.

        id: `int`
            The user ID of the target member. Must be an integer or convertible to integer.
            
        Returns
        -------
        member: `Member`
            A `lunarcord.Member` object representing the requested member.
        """

        found = self.getMember(guild, id)

        if found:
            return found
        
        if type(guild) is not Guild:
            guild = await self.fetchGuild(guild)

        if not guild:
            return

        data: dict = await self._gateway.manager.loadMember(guild.id, id)

        if data is None:
            return
        
        user: dict = data.pop("user")

        return await Member._create(
            bot = self,
            user = user,
            data = data,
            guild = guild
        )

    
    def getChannelNamed(self, name: str) -> Channel:
        
        '''
        Get and return the `Channel` with the given `name` from the cache, if found.
        
        Parameters
        ----------
        name: `str`
            The target channel's name. Must be a string, or convertible to string.
            
        Returns
        -------
        channel: `Channel`
            A `lunarcord.Channel` object representing the target messageable, or `None` if not found.
        '''
        
        if type(id) is not str:
            try:
                id = str(id)
                
            except:
                return None
            
        name = name.lower()
            
        for channel in self._gateway.channels:
            if channel.name.lower() == name:
                return channel
            
    def getUserNamed(self, name: str) -> User:
        
        '''
        Get and return the `User` with the given `name` from the cache, if found.
        This works with both display name (if existing) and real username.
        
        Parameters
        ----------
        name: `str`
            The target user's name. Must be a string, or convertible to string.
            
        Returns
        -------
        channel: `User`
            A `lunarcord.User` object representing the target user, or `None` if not found.
        '''
        
        if type(id) is not str:
            try:
                id = str(id)
                
            except:
                return None
            
        name = name.lower()
            
        for user in self._gateway.users:
            if user.displayName.lower() == name or user.username.lower() == name:
                return user
            
    def getGuildNamed(self, name: str) -> Guild:
        
        '''
        Get and return the `Guild` with the given `name` from the cache, if found.
        
        Parameters
        ----------
        name: `str`
            The target guild's name. Must be a string, or convertible to string.
            
        Returns
        -------
        guild: `Guild`
            A `lunarcord.Guild` object representing the target guild, or `None` if not found.
        '''
        
        if type(name) is not str:
            try:
                name = str(name).lower()
            except:
                return None
            
        for guild in self._gateway.guilds:
            if guild.name.lower() == name:
                return guild
            
    def getRoleNamed(self, name: str) -> Role:
        
        '''
        Get and return the `Role` with the given `name` from the cache, if found.
        
        Parameters
        ----------
        name: `str`
            The target role's name. Must be a string, or convertible to string.
            
        Returns
        -------
        role: `Role`
            A `lunarcord.Role` object representing the target role, or `None` if not found.
        '''
        
        if type(name) is not str:
            try:
                name = str(name).lower()
                
            except:
                return None
            
        for role in self._gateway.roles:
            if role.name.lower() == name:
                return role
            
    def getView(self, name: str):

        """
        Gets a view with the given name. If you hadn't given your `View` a name when creating it, the variable name you used works too.

        Parameters
        ----------
        name: `str`
            The target view's custom name.

        Returns
        -------
        view: `View`, `None`
            The view that was found. Can be `None` if no view was found.
        """

        for view in self._gateway.views:
            if hasattr(view, "name"):
                if view.name == name:
                    return view
    
    async def waitForMessage(
        
        self,
        author: User | Snowflake = Anyone,
        timeout: int | float = NoTimeout
        
    ) -> Message | None:
        
        '''
        Wait until a new message is received.
        
        Parameters
        ----------
        author: `User`, `Snowflake`
            A `User` object - or an integer (or a convertible to integer) representing a Discord `Snowflake`. If this is None (or not given at all), messages by any user will be sent back.
        
        timeout: `int`, `float`
            A float or convertible to float in which time the target message should have been sent. If `None`, no timeout should be set.
            
        Returns
        -------
        message: `Message`, `None`
            A lunarcord `Message` that was received, or `None` if the timeout passed.
        '''
        
        if author == Anyone:
            author = None
            
        if timeout == NoTimeout:
            timeout = None
            
        if author is not None:
            
            if type(author) is not User:
                
                try:
                    author = await self.fetchUser(author)
                    
                except:
                    author = None
            
        if type(timeout) is not float:
            
            try:
                timeout = float(timeout)
            except:
                timeout = None
                
        def check(msg):

            nonlocal author

            if author is None:
                return True
            
            return msg.author.id == author.id
                
        return await self._gateway.waitFor(
            event="MESSAGE_CREATE",
            timeout=timeout,
            check=check,
            catch=True
        )
            
    async def _updateSlashCommands(self, existing: list[dict] = None):
        
        '''
        Update slash commands, adding pending ones and deleting any that are missing. This is a helper method and should be used only be lunarcord itself.
        '''
        
        if existing is None:
            
            existing = await self._gateway.manager.slashCommands()

        existingIDs = [int(x.get("id")) for x in existing if "id" in x]
    
        createdIDs = []
        
        for pending in self.pendingSlashCommands:
            try:
                new = await pending._toJson()
                createdIDs.append(int(new.get("id")))
            except:
                continue
        
        missingIDs = [x for x in existingIDs if x not in createdIDs]
        
        if missingIDs:
            
            await self._gateway.manager.deleteSlashCommands(*missingIDs)
        
        self.pendingSlashCommands = []
        
    def _updateSlashCommandsSync(self, existing: list[dict] = None):
        
        '''
        Same as using _updateSlashCommands, but this is no longer a coroutine function, and it also happens in a separate thread - improving speed.
        '''
        
        self._gateway.runInThread(
            
            function = self._updateSlashCommands,
            existing = existing
            
        )

    async def login(self, login: str, password: str):
        
        '''
        Login using a `login` (an `email` or a `phone number`) and the corresponding account's `password`.
        This returns the account's token (a `str`) which can later be used to run this bot.
        If the credentials are invalid or something else is wrong (eg. "New login location detected..." and such errors), the returned `token` will be `None`.
        '''
        
        try:
            return await self._gateway.manager.doLogin(login, password)
        
        except:
            return None
        
    def readJson(self, path: str, default = ...):

        """
        A helper method for easily reading `JSON` files for your bot.
        This method works ~10 times faster than the normal `json.load()`
        one as it works with the help of `ORJSON`.

        Parameters
        ----------
        path: `str`
            The path for your json file.

        default: `Any`
            The default data to return in case this failed. If the file is missing and this is provided, it will be created with this data.
        """

        try:

            try:
                fp = open(path, "rb")
            except:
                return self.writeJson(path, default)
            
            raw = fp.read()
            data = json.loads(raw)

        except:
            data = default
            
        finally:
            fp.close()

        return data
    
    def writeJson(self, path: str, data):

        """
        A helper method for easily saving `JSON` files for your bot.
        This method works ~10 times faster than the normal `json.dump()`
        one as it works with the help of `ORJSON`.

        Parameters
        ----------
        path: `str`
            The path for your json file.

        data: `Any`
            The data to be saved into the json file.
        """

        try:
            fp = open(path, "wb")
            raw = json.dumps(data)
            fp.write(raw)
            
        finally:
            fp.close()

    async def request(self, url: str, data = None):

        """
        This method exists to make your life as a coder easier.
        No more need to use additional modules for requests!
        You can use this to perform a `GET` request on any `url` with the given `data` payload.

        Parameters
        ----------
        url: `str`
            The URL to perform the request on.

        data: `Any`
            Any data to pass as the request payload.

        Returns
        -------
        returned: `bytes`, `str`, `json` or `None`
            The data returned from the other side. Can have multiple types, and could be `None` if nothing is returned.
        """

        returns: bytes = await self.manager.get(url, data, customUrl=True, returns=bytes)

        try:
            string = returns.decode()
        except:
            return returns
        
        try:
            return json.loads(string)
        except:
            return string
        
    async def cat(self) -> str | None:

        """
        If you found this method randomly, consider yourself lucky.
        This is meant to be an easter egg, but could still be useful!

        Returns
        -------
        url: `str`
            A URL leading to a random cat picture. All images provided by `thecatapi` API!
        """

        data: list[dict] = await self.request("https://api.thecatapi.com/v1/images/search")
        return data[0].get("url", None)
    
    async def europapa(self, unknown: Unknown = Unknown):

        """
        What even is this? Why is this here?
        I don't know, but Joost Klein is awesome!
        
        Just try it yourself and maybe you'll find out what all this means...
        How did you even find this function anyways?
        
        Parameters
        ----------
        unknown: `Unknown`
            Try changing this and you might find out. For now, the usage of this parameter should stay `Unknown`...

        Europe, let's come together (Euro-pa-pa, Euro-pa-pa)
        It's now or never, I love you all (Euro-pa-pa, Euro-pa-pa)

        Welkom in Europa, blijf hier tot ik doodga
        Euro-pa-pa, Euro-pa-pa

        Welkom in Europa, blijf hier tot ik doodga
        Euro-pa-pa, Euro-pa-pa

        Bezoek m'n friends in France of neem de benen naar Wenen
        Ik wil weg uit Netherlands, maar m'n paspoort is verdwenen

        Heb gelukkig geen visum nodig om bij je te zijn
        Dus neem de bus naar Polen of de trein naar Berlijn

        'k Heb geen geld voor Paris, dus gebruik m'n fantasie
        Heb je een eurootje, please? Ik zeg "merci" en "alsjeblieft"

        Ik ben echt alles kwijt, behalve de tijd
        Dus 'k ben elke dag op reis, want de wereld is van mij

        Welkom in Europa, blijf hier tot ik doodga
        Euro-pa-pa, Euro-pa-pa

        Welkom in Europa, blijf hier tot ik doodga
        Euro-pa-pa, Euro-pa-pa

        Euro-pa-pa-pa-pa-pa-pa-pa
        Euro-pa-pa-pa (hey)
        Euro-pa-pa-pa-pa-pa-pa-pa
        Eu-ro-pa (hey)

        Ich bin in Deutschland, aber ich bin so allein
        Io sono in Italia, maar toch doet het pijn

        'k Ben aan het vluchten van mezelf, roep de hele dag om help
        Ja, ik geef zelfs mensen geld, maar d'r is niemand die me helpt

        Ik hoef geen escargots, hoef geen fish-and-chips
        Hoef geen paella, no, ik weet niet eens echt wat dat is

        Zet de radio aan, ik hoor Stromae met Papaoutai
        Zal niet stoppen tot ze zeggen: "Ja, ja, dat doet 'ie goed, hé"

        Welkom in Europa, blijf hier tot ik doodga
        Euro-pa-pa, Euro-pa-pa

        Welkom in Europa, blijf hier tot ik doodga
        Euro-pa-pa, Euro-pa-pa

        Euro-pa-pa-pa-pa-pa-pa-pa
        Euro-pa-pa-pa (hey)
        Euro-pa-pa-pa-pa-pa-pa-pa
        Eu-ro-pa (hey)
        
        Jaha, hé, welkom in Europa, jonguh!
        """
        
        if unknown == Unknown:
            target = self.owner
        elif type(unknown) is User:
            target = unknown
        elif type(unknown) is int:
            target = await self.fetchUser(unknown)
        else:
            target = None

        if target is None:
            return print("[LUNARCORD] Failed to activate Joost mode.")
        
        try:
            webbrowser.open("https://www.youtube.com/watch?v=IiHFnmI8pxg", new=2)
        except:
            ...

        print("[LUNARCORD] Joost mode activated.")
        
        gifs = [

            "https://tenor.com/view/joost-klein-joost-joost-europapa-joost-klein-europapa-joost-klein-hey-gif-8063808885285976612",
            "https://tenor.com/view/europapa-joost-klein-gif-2406371744907006571",
            "https://tenor.com/view/europapa-joost-klein-gif-15870040348330019344",
            "https://tenor.com/view/joost-joost-klein-europapa-eurovision-contest-eurovision-2024-gif-10493321365734631409",
            "https://tenor.com/view/joost-joost-klein-erik-sussy-gif-18398024777456892539",
            "https://tenor.com/view/europapa-joost-klein-gif-2444755365992642313",
            "https://tenor.com/view/joost-joost-klein-europapa-joost-wave-joost-klein-wave-gif-317417478880584456",
            "https://tenor.com/view/joost-klein-jumping-rope-eurovision-esc-gif-14556300775786763513"

        ]

        try:

            self.activity = "Listening to Europapa"

            for gif in gifs:

                try:
                    await target.dm(gif)
                except:
                    await asyncio.sleep(3)
                    await target.dm(gif)

            await target.dm("https://www.youtube.com/watch?v=IiHFnmI8pxg")

        except:
            ...
        
    def __repr__(self):
        
        if hasattr(self, 'name'):
            
            return f'<Bot name={self.name}>'
        
        return f'<Bot object at {hex(id(self))}>'
    
    def __str__(self):
        
        if hasattr(self, 'name'):
            
            return self.name
        
        return f'<Bot object at {hex(id(self))}>'
    
    addPrefixes = addPrefix
    removePrefixes = removePrefix
    hasPrefixes = hasPrefix

class Application:

    def __init__(self, *, data: dict, manager):

        def _(x, y = None, z: type = None):
            found = data.pop(x,y)
            if z:
                return z(found)
            return found
        
        self.manager: BotManager = manager
        """The `BotManager` this `Application` was created from."""
        
        self.id: int = _("id", z=int)
        """The application ID for your app."""

        self.name: str = _("name")
        """The application's name."""

        self.description: str = _("description")
        """The application's description. This also shows up in the bot's About Me section."""

        self.iconHash: str = _("icon")
        """The hash string of the bot's icon."""

        self.public: bool = _("bot_public")
        """Whether this is a public bot."""

        self._user = _("bot")

        self.token: str = ...
        """The bot's token which you can later use to run it."""


class BotManager:

    """Easily manage your bots in Discord Developer Portal in Python."""

    def __init__(self, login: PhoneNumber | Email | UserLogin, password: Password | String):

        """Log in to the Discord Developer Portal as an existing discord user. This allows you to manage your bots directly from lunarcord."""

        self.login = login
        self.password = password

        self.manager = None
        self.token = None
        self.name = None

        self.eventloop = None
        self._callback = None

        self.applications = []

    def callback(self, callback):

        """Registers an on ready `Callback` to be used as soon as the `Manager` has logged in and loaded all your bots. Only one callback can be registered here."""

        if callable(callback):
            self._callback = callback
            
    async def start(self):

        await self.load()
        callback = self._callback

        if callable(callback):
            await callback()

        await self.manager.close()

        if self.eventloop:
            self.eventloop.stop()
    
    def run(self):

        loop = None
        
        try:
            loop = asyncio.get_event_loop()
        except:
            loop = None
            
        if not loop:
            loop = asyncio.new_event_loop()
        
        self.eventloop = loop
        loop.create_task(self.start())
        loop.run_forever()

    async def load(self):

        """Performs the logging-in and loads your data."""

        manager = Manager(isBot=False)

        try:
            token = await manager.doLogin(self.login, self.password)
        except Exception as e:
            print(e.error)
            token = None

        if not token:
            await manager.close()
            return print(f"[LUNARCORD] Failed to login to Discord!")
        
        self.token = token
        manager.token = token
        self.manager = manager
        manager.generateHeaders(token)

        me = await manager.me()
        display = me.get("global_name")
        username = me.get("username")

        self.name = display

        if display is None:
            self.name = username

        print(f"[LUNARCORD] Successfully logged in as \033[1m{self.name}\033[0m")
        
        try:
            applications = await manager.get("/applications/")
        except:
            return print("[LUNARCORD] Failed to load applications!")
        
        self.applications = applications
        count = len(self.applications)
        print(f"[LUNARCORD] Successfully loaded \033[1m{count}\033[0m applications")

    def _get(self, url: str, payload = None):
        return self.manager.get(url, payload)
    
    def _post(self, url: str, payload = None):
        return self.manager.post(url, payload)
            
    def _finishMfa(self, data: dict):

        mfa = data["mfa"]
        methods = mfa["methods"]
        methods = [x["type"] for x in methods]

        if "password" not in methods:
            raise Exception("Mutiple factor authentication failed")

        ticket = mfa["ticket"]

        payload = {
            "data": self.password,
            "mfa_type": "password",
            "ticket": ticket
        }

        return self._post("/mfa/finish", payload)
    
    async def resetBotToken(self, id: int) -> str:

        """Updates and returns the token for a `Bot` by its ID."""

        coro = self.manager.post(f"/applications/{id}/bot/reset")

        try:
            data = await coro
            return data["token"]
        
        except Exception as e:

            if not hasattr(e, "error"):
                raise

            try:
                await self._finishMfa(e.error)
            except:
                raise
                return print("LUNARCORD] Fetching bot token failed!")
            
            return await self.resetBotToken(id)

    async def getBotNamed(self, name: str) -> Application | None:

        """
        Gets and returns a bot with the given name
        
        Parameters
        ----------
        name: `str`
            The application's name. This is case-sensitive.

        Returns
        -------
        app: `Application`
            An application which you can get the token of with `Application.token`. This can also be `None` in the case no bot was found.
        """

        if not self.name:
            return

        found = None

        for app in self.applications:
            if app.get("name") == name:
                found = app

        if not found:
            return print(f"No bot named \033[1m{name}\033[0m was found")
        
        name = str(found.get("name"))
        print(f"[LUNARCORD] Successfully loaded bot \033[1m{name}\033[0m")
        application = Application(data=found, manager=self)
        application.token = await self.resetBotToken(application.id)

        if application.token is ...:
            return None
        
        return application
    
    async def getBot(self, id: int) -> Application | None:

        """
        Gets and returns a bot with the given application ID.
        
        Parameters
        ----------
        id: `int`
            The application's ID. This is case-sensitive.

        Returns
        -------
        app: `Application`
            An application which you can get the token of with `Application.token`. This can also be `None` in the case no bot was found.
        """

        if not self.name:
            return

        found = None

        for app in self.applications:
            if app.get("id") == id:
                found = app

        if not found:
            return print(f"No bot with ID \033[1m{id}\033[0m was found")
        
        id = str(found.get("id"))
        print(f"[LUNARCORD] Successfully loaded bot with ID \033[1m{id}\033[0m")
        application = Application(data=found, manager=self)
        application.token = await self.resetBotToken(application.id)

        if application.token is ...:
            return None
        
        return application

    async def createBot(self, name: str) -> Application:

        if not self.name:
            return

        payload = {"name": name}
        app = await self.manager.post("applications", payload)
        print(f"[LUNARCORD] Successfully created bot \033[1m{name}\033[0m")
        application = Application(data=app, manager=self)
        application.token = await self.resetBotToken(application.id)
        return application