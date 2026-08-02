import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='Discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

secret_role = "bottestrole"

@bot.event
async def on_ready():
    print(f"We Are Ready To Go, {bot.user.name}")

@bot.event
async def on_member_join(member):
    try:
        await member.send(f"Welcome to the server,  you cunt, {member.name}! Thanks for joining Now Stay")
    except discord.Forbidden:
        print(f"Could not DM {member.name}. They might have DMs closed.")

BAD_WORDS = ["shit", "fuck", "bitch", "nigger", "nigga", "niggr","nigg"]

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
@commands.has_role(secret_role)
async def secret(ctx):
    await ctx.send("YEEE BOII YOU A SECRETT MEMBYY")
    await ctx.send("https://images-ext-1.discordapp.net/external/BGFn7kJxzDZqy-nFbTNsfQLGzHy3Ag9_BtEOzjzDMKc/https/media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjB6c2Y2ZHQzaHFvdWI0cTNnbms5eWV6aHkzeGp6NnZ4ODRyMHBvbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gXXFrjHFJIMoqKr8UT/giphy.gif")


@secret.error
async def secret_error(ctx, error):
    await ctx.send ("we have encountered a error please try again later")

@bot.command()
async def gif1(ctx):
    await ctx.send("https://tenor.com/view/cat-girl-head-pat-headpat-anime-gif-15491115994804690187")



@bot.command()
async def img1(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1533572933434216508/1533572955928400145/sams2022-382.jpg?ex=6a70fa9d&is=6a6fa91d&hm=89224e4130cc2e7d0a6706c636371f1a2709d1df47474f28cff00af3fa16fc9f&")



bot.run(token, log_handler=handler, log_level=logging.DEBUG)
