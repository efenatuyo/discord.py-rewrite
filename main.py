import aiohttp
import asyncio
import logging
from typing import Any, Callable

MISSING = object()

CoroFunc = Callable[..., Any]

logging.basicConfig(level=logging.INFO)

class Bot:
    def __init__(self, token: str):
        async def check_token(token):
            self.is_valid = await self.is_valid_token(token)
            if not self.is_valid:
                raise ValueError("Invalid bot token")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(check_token(token))
        self.token = token
        self.extra_events = {}
    
    def run(self):
        self.add_listener(on_ready, name="on_ready")
        for coro in self.extra_events["on_ready"]:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(coro())
    def add_listener(self, func: CoroFunc, /, name: str = MISSING) -> None:
        """The non decorator alternative to :meth:`.listen`.
        ... same as before ...

        """
        name = func.__name__ if name is MISSING else name

        if not asyncio.iscoroutinefunction(func):
            raise TypeError('Listeners must be coroutines')

        if name in self.extra_events:
            self.extra_events[name].append(func)
        else:
            self.extra_events[name] = [func]

    def remove_listener(self, func: CoroFunc, /, name: str = MISSING) -> None:
        """Removes a listener from the pool of listeners.
        ... same as before ...
        """

    def event(self, name: str = MISSING) -> Callable[[CoroFunc], CoroFunc]:
        """A decorator that registers an event to listen to.
        ... same as before ...
        """

        def decorator(func: CoroFunc) -> CoroFunc:
            self.add_listener(func, name)
            return func

        return decorator
    async def is_valid_token(self, token: str) -> bool:
        headers = {
            "Authorization": f"Bot {token}",
        }
        url = "https://discord.com/api/users/@me"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 401:
                    return False
                elif response.status != 200:
                    response_data = await response.json()
                    error_message = response_data.get("message", "Unknown error")
                    raise ValueError(f"Failed to validate token: {error_message}")
                else:
                    return True
    
    async def create_text_channel(self, guild_id: str, name: str, **kwargs):

     url = f"https://discord.com/api/guilds/{guild_id}/channels"
     headers = {
        "Authorization": f"Bot {self.token}",
        "Content-Type": "application/json"
     }
     data = {
        "name": name,
        "type": 0
     }
     data.update(kwargs)
     async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            response_data = await response.json()
            if response.status != 201:
                error_message = response_data.get("message", "Unknown error")
                raise ValueError(f"Failed to create text channel: {error_message}")
            return response_data
    
    async def create_voice_channel(self, guild_id: str, name: str, **kwargs):

     url = f"https://discord.com/api/guilds/{guild_id}/channels"
     headers = {
        "Authorization": f"Bot {self.token}",
        "Content-Type": "application/json"
     }
     data = {
        "name": name,
        "type": 2
     }
     data.update(kwargs)
     async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            response_data = await response.json()
            if response.status != 200:
                error_message = response_data.get("message", "Unknown error")
                raise ValueError(f"Failed to create voice channel: {error_message}")
            return response_data
    
    async def edit_channel(self, channel_id: str, **kwargs):

     url = f"https://discord.com/api/channels/{channel_id}"
     headers = {
        "Authorization": f"Bot {self.token}",
        "Content-Type": "application/json"
     }
     data = {
     }
     data.update(kwargs)
     async with aiohttp.ClientSession() as session:
        async with session.patch(url, headers=headers, json=data) as response:
            response_data = await response.json()
            if response.status != 201:
                error_message = response_data.get("message", "Unknown error")
                raise ValueError(f"Failed to edit channel: {error_message}")
            return response_data
    
    async def delete_channel(self, channel_id: str, **kwargs):

     url = f"https://discord.com/api/channels/{channel_id}"
     headers = {
        "Authorization": f"Bot {self.token}",
        "Content-Type": "application/json"
     }
     data = {
     }
     data.update(kwargs)
     async with aiohttp.ClientSession() as session:
        async with session.delete(url, headers=headers, json=data) as response:
            response_data = await response.json()
            if response.status != 200:
                error_message = response_data.get("message", "Unknown error")
                raise ValueError(f"Failed to edit channel: {error_message}")
            return response_data
        
    async def create_role(self, guild_id: str, name: str, **kwargs):

     url = f"https://discord.com/api/guilds/{guild_id}/roles"
     headers = {
        "Authorization": f"Bot {self.token}",
        "Content-Type": "application/json"
     }
     data = {
        "name": name
     }
     data.update(kwargs)
     async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            response_data = await response.json()
            if response.status != 201:
                error_message = response_data.get("message", "Unknown error")
                raise ValueError(f"Failed to create role: {error_message}")
            return response_data    
    
    async def edit_role(self, guild_id: str, role_id: str, **kwargs):

     url = f"https://discord.com/api/guilds/{guild_id}/roles/{role_id}"
     headers = {
        "Authorization": f"Bot {self.token}",
        "Content-Type": "application/json"
     }
     data = {
     }
     data.update(kwargs)
     async with aiohttp.ClientSession() as session:
        async with session.patch(url, headers=headers, json=data) as response:
            response_data = await response.json()
            if response.status != 200:
                error_message = response_data.get("message", "Unknown error")
                raise ValueError(f"Failed to edit role: {error_message}")
            return response_data    
    

    



bot = Bot("MTA3NDMyNjExNzQ5MTY4NzQ1NA")

async def on_ready():
    # await bot.create_text_channel(guild_id="1060259221771399168", name="test")
    # await bot.create_voice_channel(guild_id="1060259221771399168", name="test")
    # await bot.edit_channel(channel_id="1074332653702094870", name="test")
    # await bot.delete_channel(channel_id="1074332653702094870")
    # await bot.create_role(guild_id="1060259221771399168", name="test")
    # await bot.edit_role(guild_id = "1060259221771399168", role_id="1074351240357629982", name="test")
    print("we ran")
    
bot.run()
