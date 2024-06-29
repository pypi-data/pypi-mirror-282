import asyncio, aiohttp, orjson
from urllib.parse import quote
from ..errors import RequestError, UnauthorizedError

class Manager:
    
    aiohttp = aiohttp
    requests = ...
    
    def __init__(self, token: str = None, session: aiohttp.ClientSession = None, isBot: bool = True, gateway = None):
        
        if session is None:
            session = aiohttp.ClientSession()
        
        self.token = token
        self.isBot = True
        self.session = session
        self.gateway = gateway
        self.generateHeaders()

        self.reason: str = ...
        
    async def close(self):
        await self.session.close()
        
        
    def generateHeaders(self, token: str = None):
        
        if token is not None:
            self.token = token
            
        self.headers = {
            'Authorization': self.token
		}
        
        return self.headers
    
    async def request(self, url: str, json: dict = None, attachments: list = None, method: str = 'get', version: int = 10, returns: type = dict, customUrl: bool = False, params: dict = {}, disableHeaders: bool = False):

        if self.session.closed:
            return None
        
        if type(url) is not str:
            url = str(url)
        
        headers = self.headers
        reason = self.reason

        data = None
        
        if "Authorization" not in headers:
            if self.token is not None:
                self.generateHeaders(self.token)
                
            else:
                disableHeaders = True

        if reason not in (..., None):
            self.headers["X-Audit-Log-Reason"] = str(reason)
            self.reason = None

        if json not in ({}, None) and (not attachments):
            headers["Content-Type"] = "application/json"
            data = orjson.dumps(json)

        if self.token is None and "Authorization" in headers:
            headers.pop("Authorization")

        if attachments:

            headers.pop("Content-Type", None)
            data = aiohttp.FormData()
            #json["attachments"] = []

            """for idx, attachment in enumerate(attachments):

                data.add_field(
                    name=f"attachments[{idx}]",
                    value=attachment._bytes,
                    content_type="application/octet-stream",
                    filename=attachment.name
                )

                json["attachments"].append({
                    "id": idx,
                    "filename": attachment.name,
                    "description": "No description provided"
                })

            data.add_field(
                name="payload_json",
                value=orjson.dumps(json).decode()
            )"""

            for idx, attachment in enumerate(attachments):

                data.add_field(
                    name=f"{idx}", 
                    value=attachment._bytes,
                    filename=attachment.name
                )
            
            for key, value in json.items():
                if value:
                    data.add_field(key, value)

            #data.add_field("attachments", orjson.dumps({"id": 0, "filename": "pfp.png", "description": "No description provided"}).decode())
        
        if disableHeaders:
            headers = {}
            
        method = method.strip().lower()
        
        if method not in ('get', 'post', 'delete', 'put', 'patch'):
            raise RequestError(None, 'Invalid method used', method)
        
        if not customUrl:
            url = f'https://discord.com/api/v{version}/' + url.removeprefix("/").removesuffix("/")
        
        kwargs = {
            
            'headers': headers,
            'params': params
            
        }

        if data:
            kwargs['data'] = data
        
        async with self.session.request(method, url, **kwargs) as response:

            self.headers.pop("X-Audit-Log-Reason", None)
            code = int(response.status)
            
            successful = True
            
            if code in (400, 401, 403, 404, 405, 429, 502, '5xx'):
                successful = False

            errdict = {}
                
            if not successful:
                
                try:
                    errdict: dict = await response.json()
                    msg = errdict.get("message")
                    
                except:
                    
                    match code:
                        
                        case 400:
                            msg = 'Bad Request'
                            
                        case 401:
                            msg = 'Unauthorized'
                            
                        case 403:
                            msg = 'Forbidden'
                            
                        case 404:
                            msg = 'Not found'
                            
                        case 405:
                            msg = 'Method not allowed'
                            
                        case 429:
                            msg = 'You are being rate limited'
                            
                        case 502:
                            msg = 'Gateway unavailable'
                            
                        case '5xx':
                            msg = 'Discord Error'
                            
                        case _:
                            msg = 'Unknown Error'
                            
                if code == 429:
                    
                    slowdown = int(errdict.get('retry_after', 10))
                    #print("Slowdown! Time:", slowdown)
                    await asyncio.sleep(slowdown)
                    return await self.request(url, json, attachments, method, version, returns, customUrl, params, disableHeaders)
                
                elif code == 401:
                    raise UnauthorizedError(errdict)
                    
                else:
                    
                    if msg is not None:
                        raise RequestError(code, msg, method, errdict)
                    
                    else:
                        raise RequestError(code, f"Unknown error: {code}")
                
                
            
            if isinstance(returns, str):
                returns = returns.lower()

            data = await response.read()
            
            if returns in ('raw', 'bytes', 'default', bytes):
                return data
            
            elif returns in ('json', 'dict', 'dictionary', dict):
                try:
                    return orjson.loads(data)
                except:
                    #print(f"Failed to decode: {data.decode()}")
                    return
            
            elif returns in ('content', 'str', 'string', str):
                return data.decode()
            
            elif returns in ('code', 'status', 'statuscode', int):
                return response.status
            
            elif returns in ('none', 'null', 'empty', None):
                return None
            
            elif returns in ('result', 'success', 'successfull', bool):
                return True
            
            else:
                raise RequestError(0, 'Bad request')
        
    async def get(self, url: str, json: dict = None, attachments: list = None, version: int = 10, returns: type = dict, customUrl: bool = False, params: dict = {}, disableHeaders: bool = False): return await self.request(url, json, attachments, 'get', version, returns, customUrl, params, disableHeaders)
    async def post(self, url: str, json: dict = None, attachments: list = None, version: int = 10, returns: type = dict, customUrl: bool = False, params: dict = {}, disableHeaders: bool = False): return await self.request(url, json, attachments, 'post', version, returns, customUrl, params, disableHeaders)
    async def delete(self, url: str, json: dict = None, attachments: list = None, version: int = 10, returns: type = dict, customUrl: bool = False, params: dict = {}, disableHeaders: bool = False): return await self.request(url, json, attachments, 'delete', version, returns, customUrl, params, disableHeaders)
    async def put(self, url: str, json: dict = None, attachments: list = None, version: int = 10, returns: type = dict, customUrl: bool = False, params: dict = {}, disableHeaders: bool = False): return await self.request(url, json, attachments, 'put', version, returns, customUrl, params, disableHeaders)
    async def patch(self, url: str, json: dict = None, attachments: list = None, version: int = 10, returns: type = dict, customUrl: bool = False, params: dict = {}, disableHeaders: bool = False): return await self.request(url, json, attachments, 'patch', version, returns, customUrl, params, disableHeaders)

    async def loadMessages(self, channel: int, limit: int = 1000) -> list[dict]:

        params = {
            "limit": limit
        }
        
        url = f'channels/{channel}/messages'
        return await self.get(url, params=params)
        
    async def loadMessage(self, channel: int, message: int) -> dict | None:
        
        url = f'channels/{channel}/messages/{message}'
        
        try:
            return await self.get(url)
            
        except:
            return await self.loadMessage2(channel, message)
    
    async def loadMessage2(self, channel: int, message: int) -> dict | None:
        
        messages = await self.loadMessages(channel)
        
        for log in messages:
            
            id = int(log.get('id'))
            
            if int(message) == id:
                return log
            
			
    async def sendMessage(self, channel: int, content: str, reference: int = None, embeds: list = [], attachments: list = [], components: list = []) -> dict:
        
        if not isinstance(content, str) and content is not None:
            content = str(content)
        
        if ( content is None or content.strip() == '' ) and ( not embeds and not attachments and not components ):
            content = '** **'
        
        url = f'channels/{channel}/messages'
        
        data = {'content': content, 'allowed_mentions': None}
        
        if reference is not None:
            data['message_reference'] = {'message_id': reference}
        
        if embeds:
            
            jsonEmbeds: list[dict] = []
            
            for embed in embeds:
                jsonEmbeds.append(await embed._toJson())
                
            data['embeds'] = jsonEmbeds
            
        if components:
            data['components'] = components
            
        return await self.post(url, data, attachments)
    
    async def loadUser(self, id: int):
        url = f'users/{id}'
        return await self.get(url)
        
    async def addReaction(self, channel: int, message: int, reaction: str) -> None:
        
        try:
            reaction = str(reaction)
        except:
            return None
        
        reaction = quote(reaction, safe="")
        url = f'channels/{channel}/messages/{message}/reactions/{reaction}/@me'
        return await self.put(url)
        
    async def removeReaction(self, channel: int, message: int, reaction: str) -> None:
        
        try:
            reaction = str(reaction)
        except:
            return None
        
        reaction = quote(reaction, safe="")
        url = f'channels/{channel}/messages/{message}/reactions/{reaction}/@me'
        return await self.delete(url)
        
    async def deleteMessage(self, channel: int, message: int) -> None:
        
        url = f'channels/{channel}/messages/{message}'
        return await self.delete(url)
        
    async def me(self) -> dict | None:
        
        return await self.get('users/@me')
    
    async def clientInfo(self) -> dict | None:
        
        return await self.get('oauth2/applications/@me')
    
    async def clientID(self) -> int:
        
        info = await self.clientInfo()
        return int(info.get('id'))
    
    async def editMessage(self, channel: int, message: int, content: str) -> None:
        url = f'channels/{channel}/messages/{message}'
        data = {'content': str(content)}
        return await self.patch(url, data)
    
    async def loadRoles(self, guild: int) -> dict:
        url = f"guilds/{guild}/roles"
        return await self.get(url)
    
    async def addRole(self, guild: int, user: int, role: int, reason: str = ...):
        self.reason = reason
        url = f"/guilds/{guild}/members/{user}/roles/{role}"
        await self.put(url, returns=None)
    
    async def removeRole(self, guild: int, user: int, role: int, reason: str = ...):
        url = f"/guilds/{guild}/members/{user}/roles/{role}"
        self.reason = reason
        await self.delete(url, returns=None)
    
    async def kickMember(self, guild: int, user: int):
        url = f"guilds/{guild}/members/{user}"
        await self.delete(url, returns=None)

    async def banMember(self, guild: int, user: int, deleteMessageSeconds: int = 0):
        data = {"delete_message_seconds": deleteMessageSeconds}
        url = f"guilds/{guild}/bans/{user}"
        await self.put(url, json=data, returns=None)
    
    async def createSlash(self, name: str = None, description: str = None, options: list = [], type: int = 1, guilds: list[int] = None, override: bool = True) -> dict:
        
        data = {
		   'name': name,
		   'description': description,
		   'type': 1, # Slash Command
		   'options': options
		}
        
        if not override:
            return data
        
        clientID = await self.clientID()
        
        if guilds is not None and len(guilds) > 0:
            
            try:
                guildID = guilds.pop(0)
                url = f'applications/{clientID}/guilds/{guildID}/commands'
                last = await self.post(url, data)
                last = await self.createSlash(name, description, options, type, guilds, override)
                
            except:
                return last
            
        else:
        
            url = f'applications/{clientID}/commands'
            return await self.post(url, data)
        
        return last
    
    async def slashCommands(self) -> list[dict] | None:
        
        clientID = await self.clientID()
        
        slash: list = await self.get(
            f'applications/{clientID}/commands'
        )
        
        return slash
    
    async def deleteSlash(self, id: int | str) -> None:
        
        clientID = await self.clientID()
        
        await self.delete(
            f'applications/{clientID}/commands/{id}',
            returns = None
        )
        
    async def deleteSlashCommands(self, *ids: int | str) -> None:
        '''
        Deletes the commands with the specified IDs, or all if no IDs are given.
        
        Parameters
        ----------
        ids: `int`, `str`
            A list of IDs of the Slash Commands to delete. 
        '''
        
        if len(ids) <= 0:
            slashCommands = await self.slashCommands()
            
        else:
            slashCommands = [{'id': slashid} for slashid in ids]
            
        async def delete(slashCommand):
        
            try:
                
                await self.deleteSlash(
                    id = slashCommand['id']
                )
                
            except:
                
                ...
            
        coros = []
        
        for slashCommand in slashCommands:
            
            coros.append(delete(slashCommand))
            
        await asyncio.gather(*coros)
	   
    async def interaction(self, id) -> dict:
        
        url = f'interactions/{id}'
        return await self.get(url)
    
    async def respondToInteraction(self, interaction, payload, attachments: dict = None):
        
        url = f'interactions/{interaction.interactionID}/{interaction.interactionToken}/callback'
        
        return await self.post(
            url = url,
            json = payload,
            attachments = attachments,
            returns = dict
        )
		
    async def getSettings(self) -> dict:
        
        url = 'users/@me/settings'
        return await self.get(url)
		
    async def setSettings(self, data) -> None:
        
        url = 'users/@me/settings'
        return await self.patch(url, data)
		
    async def loadChannel(self, id: int) -> dict:
        
        url = f'channels/{id}'
        return await self.get(url)
    
    async def loadChannelsFor(self, guild: int) -> list[dict]:
        
        return await self.get(
            url = f'guilds/{guild}/channels'
        )
        
    async def loadChannels(self) -> list[dict]:
        
        return await self.get(
            url = 'users/@me/channels'
        )

    async def updateChannel(self, id: int, data) -> None:
        
        url = f'channels/{id}'
        return await self.patch(
            url=url, json=data
        )

    async def setChannelName(self, id: int, name: str) -> None:
        
        data = {
            'name': name
        }
        
        await self.updateChannel(id, data)
		
    async def pinMessage(self, channel: int, id: int) -> None:
        
        url = f'channels/{channel}/pins/{id}'
        return await self.put(url)
    
    async def unpinMessage(self, channel: int, id: int) -> None:
        
        url = f'channels/{channel}/pins/{id}'
        return await self.delete(url)
    
    async def channelFor(self, user: int) -> dict:
        
        url = f'users/@me/channels'
        user = str(user)
        
        payload = {
            'recipient_id': user
        }
        
        return await self.post(url, payload)
    
    async def showTyping(self, channel: int) -> None:
        
        url = f'channels/{channel}/typing'
        return await self.post(url)
    
    async def dmRecipients(self, group: int) -> list[dict]:
        
        return await self.get(
            url = f'channels/{group}/recipients'
        )
    
    async def groupDmAddRecipient(self, group: int, user: int) -> None:
        
        return await self.put(
            url = f'channels/{group}/recipients/{user}'
        )
        
    async def groupDmRemoveRecipient(self, group: int, user: int) -> None:
        
        return await self.delete(
            url = f'channels/{group}/recipients/{user}'
        )
        
    async def createThreadFromMessage(self, channel: int, message: int, name: str, autoArchive: int = None, rateLimit: int = None) -> dict:
        
        if rateLimit < 0:
            rateLimit = 0
            
        if rateLimit > 21600:
            rateLimit = 21600
            
        if autoArchive not in (60, 1440, 4320, 10080):
            autoArchive = None
            
        payload = {
            'name': name,
            'auto_archive_duration': autoArchive,
            'rate_limit_per_user': rateLimit
        }
        
        return await self.post(
            url = f'channels/{channel}/messages/{message}/threads',
            json = payload
        )
        
    async def createThread(self, channel: int, name: str, autoArchive: int = None, rateLimit: int = None) -> dict:
        
        if rateLimit < 0:
            rateLimit = 0
            
        if rateLimit > 21600:
            rateLimit = 21600
            
        if autoArchive not in (60, 1440, 4320, 10080):
            autoArchive = None
            
        payload = {
            'name': name,
            'auto_archive_duration': autoArchive,
            'rate_limit_per_user': rateLimit
        }
        
        return await self.post(
            url = f'channels/{channel}/threads',
            json = payload
        )
        
    async def loadGuilds(self) -> list[dict]:
        
        return await self.get(
            url = 'users/@me/guilds'
        )
        
    async def loadGuild(self, id: int) -> dict:
        
        return await self.get(
            url = f'guilds/{id}'
        )
        
    async def guildChannels(self, id: int) -> list[dict]:
        
        return await self.get(
            url = f'guilds/{id}/channels'
        )
        
    async def doLogin(self, emailOrPass: str, password: str) -> str:
        
        payload = {
            
            'login': emailOrPass,
            'password': password
            
        }
        
        returns: dict = await self.post(
            
            url = 'auth/login',
            json = payload,
            disableHeaders = False
            
        )
        
        return returns.get('token')
    
    async def loadMember(self, guild: int, id: int) -> dict | None:

        return await self.get(
            f"guilds/{guild}/members/{id}"
        )

    async def loadMembersPartial(self, guild: int, count: int = 1000, after: int = 0) -> list[dict]:

        params = {
            "limit": count,
            "after": after
        }

        return await self.get(
            f"guilds/{guild}/members",
            params = params,
            returns = "json"
        )
    
    async def loadMembers(self, guild: int):

        finished = False
        members: list[dict] = []
        highest: int = 0

        while not finished:

            try:
                
                page = await self.loadMembersPartial(guild, after=highest)

                if len(page) > 0:
                    highest = page[-1].get("user", {}).get("id", 0)
                    members.extend(page)

                else:
                    finished = True

            except:

                finished = True

        return members
    
    @staticmethod
    async def login(login: str, password: str):

        async with aiohttp.ClientSession() as session:
            manager = Manager(session=session)
            return await manager.doLogin(login, password)