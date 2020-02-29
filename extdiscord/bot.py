import os
import asyncio
import threading
from discord.ext import commands


TOKEN = os.environ.get("DISCORD_TOKEN")
print(TOKEN)


class DiscordClientWrapper:
    def __init__(self):
        self._loop = asyncio.new_event_loop()
        self._core = commands.Bot(loop=self._loop, command_prefix='$')

    def run(self, token):
        self._core.run(token)
    async def start(self, token):
        await self._core.start(token)

    def latency(self) -> float:
        return self._core.latency

    @property
    def discord_client(self):
        return self._core

    @property
    def discord_loop(self):
        return self._loop


_inst = DiscordClientWrapper()

bot = _inst._core

bot.remove_command('help')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("try")


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'load {extension} done')
    print(f'load {extension} done')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'unload {extension} done')
    print(f'unload {extension} done')


@bot.command()
async def reload(ctx, extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'reload {extension} done')
    except Exception as e:
        print(f"{extension} cannot be loaded:")
        raise e


for filename in os.listdir('./extdiscord/cogs'):
    if filename == "__init__.py":
        continue
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'extdiscord.cogs.{filename[:-3]}')
        except Exception as e:
            print(f"{filename} cannot be loaded:")
            raise e


def run_server():
    # Obtained from https://github.com/Rapptz/discord.py/issues/710#issuecomment-395609297
    thread = threading.Thread(target=_inst.discord_loop.run_until_complete, args=(_inst.start(TOKEN),))
    thread.start()

