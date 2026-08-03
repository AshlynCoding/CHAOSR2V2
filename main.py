import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
open("Discord.log", "w").close()

handler = logging.FileHandler(filename='Discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
# change secret role to the role u wanna give- or smtn.
secret_role = "bottestrole"
emoji = '👍'
emoji1 = '👎'
mc = 'guild.member_count'
team = ["DumMxttcding", "RhysGxxcding", "ballscratcher"]  # my lovlies that helped <3


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"We Are Ready To Go, {bot.user.name}")
# change the welcome message accordlingly
@bot.event
async def on_member_join(member):
    try:
        await member.send(f"Welcome to the server,  you cunt, {member.name}! Thanks for joining Now Stay")
    except discord.Forbidden:
        print(f"Could not DM {member.name}. They might have DMs closed.")


# add your owns swears or forbidden words ig?
BAD_WORDS = ["****", "****", "****", "****", "****", "****","****"]

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    lowered = message.content.lower()

    for word in BAD_WORDS:
        if word in lowered:
            await message.delete()
            await message.channel.send(f"{message.author.mention} - Don't say that")
            return  # stop processing after deleting

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    end_time = asyncio.get_event_loop().time() + 6  # 5 seconds from now

    while asyncio.get_event_loop().time() < end_time:
        await ctx.send(f"Pong! Latency is {bot.latency * 1000:.2f}ms")
        await asyncio.sleep(1)  # send once per second

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.mention}!")


@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} is now assigned to {secret_role}")
    else:
        await ctx.send("Role doesn't exist")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} is bannished from {secret_role}")
    else:
        await ctx.send("Role doesn't exist")

@bot.command()
async def status(ctx, *, text):
    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=text
        )
    )
    await ctx.send(f"Now watching: {text} (DND)")


@bot.command()
@commands.has_role(secret_role)
async def secret(ctx):
    await ctx.send("YEEE BOII YOU A SECRETT MEMBYY")
    await ctx.send("https://images-ext-1.discordapp.net/external/BGFn7kJxzDZqy-nFbTNsfQLGzHy3Ag9_BtEOzjzDMKc/https/media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjB6c2Y2ZHQzaHFvdWI0cTNnbms5eWV6aHkzeGp6NnZ4ODRyMHBvbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gXXFrjHFJIMoqKr8UT/giphy.gif")


@secret.error
async def secret_error(ctx, error):
    await ctx.send ("we have encountered an error please try again later, Or read our F&Q/Help Under Error 404 ")

@bot.command()
async def gif1(ctx):
    await ctx.send("https://tenor.com/view/cat-girl-head-pat-headpat-anime-gif-15491115994804690187")



@bot.command()
async def img1(ctx):


    await ctx.send("https://cdn.discordapp.com/attachments/1533572933434216508/1533572955928400145/sams2022-382.jpg?ex=6a70fa9d&is=6a6fa91d&hm=89224e4130cc2e7d0a6706c636371f1a2709d1df47474f28cff00af3fa16fc9f&")

@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"you said {msg}")

@bot.command()
async def reply(ctx):
    await ctx.reply("this is a reply")

@bot.command()
async def poll(ctx, *, msg):
    await ctx.send(f"{ctx.author.mention} asks {msg}")
    await ctx.message.add_reaction('👍')

@bot.command()
async def WAI(ctx):
    count = sum(1 for m in ctx.guild.members if not m.bot)
    await ctx.send(f"You are in {ctx.guild.name} with {count} Goys")

@bot.command()
async def CLANKER(ctx):
    clank = sum(1 for member in ctx.guild.members if member.bot)
    await ctx.send(f"You are in {ctx.guild.name} with {clank} clankers.")

@bot.command()
async def WYM(ctx):
    await ctx.send(f"your mother is {', '.join(team)}")

@bot.command()
async def help(ctx):
    await ctx.send(
        "ping\n"
        "hello\n"
        "assign\n"
        "remove\n"
        "status\n"
        "secret\n"
        "gif1\n"
        "img1\n"
        "dm\n"
        "reply\n"
        "poll\n"
        "WAI\n"
        "CLANKER\n"
        "WYM\n"
        "help"
    )


bot.run(token, log_handler=handler, log_level=logging.DEBUG)


# CREDITS
# discord.py team
# Ashlyn (DumMxtt)
# Rhys (RhysGxx)
# Stephen(Ballscratcher)
# Tech With Tim (Tutorial guy who helped me do most of this)
