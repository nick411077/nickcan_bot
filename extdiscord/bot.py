import os
import pymongo
import threading
from discord.ext import commands


TOKEN = 'NjAzNzI0NDkwNDg0MDg4ODQy.XeFGlw.I4lYwnLykI3DY9bRzCBQ2eQFDig'
print(TOKEN)

bot = commands.Bot(command_prefix='%')

bot.remove_command('help')


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
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'extdiscord.cogs.{filename[:-3]}')
        except Exception as e:
            print(f"{filename} cannot be loaded:")
            raise e


async def start():
    await bot.start(TOKEN)


def run_it_forever(loop):
    loop.run_forever()


def run_server():
    thread = threading.Thread(target=bot.run(TOKEN))
    thread.start()

