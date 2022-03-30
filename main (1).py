import discord
import time
import random
from discord.ext import commands
import pandas as pd

# Setups
client = commands.Bot(command_prefix='nerd ')

df = pd.read_excel(r"C:\Users\user\Downloads\discord-stody-bot\Elements.xlsx", sheet_name=0)
print(df)
nameList = df['Name of the Element'].tolist()
numberList = df['Atomic Number'].tolist()
symbolList = df['Symbol of the Element'].tolist()

facts = pd.read_excel(r"C:\Users\user\Downloads\discord-stody-bot\Facts.xlsx", sheet_name=0)
factList = facts['Facts'].tolist()


# Functions
def getadjvalue(value, list_1, list_2):
    index = list_1.index(value)
    list_2_value = list_2[index]
    return list_2_value


def evale(e):
    if '+' or '-' or '*' or '/' in e:
        ans = eval(e)
        return ans
    else:
        return "Please type in a valid equation with +,-,* or /"


# Events
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@commands.Cog.listener()
async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
    """A global error handler cog."""
    if isinstance(error, commands.CommandNotFound):
        return  # Return because we don't want to show an error for every command not found
    elif isinstance(error, commands.CommandOnCooldown):
        message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
    elif isinstance(error, commands.MissingPermissions):
        message = "You are missing the required permissions to run this command!"
    elif isinstance(error, commands.UserInputError):
        message = "Something about your input was wrong, please check your input and try again!"
    else:
        message = "Oh no! Something went wrong while running the command!"
    await ctx.send(message, delete_after=5)
    await ctx.message.delete(delay=5)


@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Do not check the bots messages

    elif random.randint(0, 100) <= 5:
        fact = random.choice(factList)
        await message.channel.send(fact)

    await client.process_commands(message)


# Commands
@client.command(aliases=["eval"])
async def evaluate(ctx, arg):
    if random.randint(0, 100) <= 25:
        await ctx.send(arg + " evaluates to, ")
        await ctx.send("...")
        time.sleep(0.9)
        await ctx.send(evale(arg) * random.randint(0, 50) - random.randint(0, 500) + random.randint(0, 5000))
        time.sleep(2)
        await ctx.send("oops... sent wrong answer just a second")
        time.sleep(0.1)
        await ctx.send("...")
        time.sleep(1.4)
        await ctx.send(evale(arg))
    else:
        await ctx.send(arg + " evaluates to, ")
        await ctx.send("...")
        time.sleep(0.9)
        await ctx.send(evale(arg))


@client.command()
async def info(ctx, arg):
    try:
        if arg in nameList:
            e_name = arg
            e_number = getadjvalue(arg, nameList, numberList)
            e_symbol = getadjvalue(arg, nameList, symbolList)
        elif arg in symbolList:
            e_name = getadjvalue(arg, symbolList, nameList)
            e_number = getadjvalue(arg, symbolList, numberList)
            e_symbol = arg
        elif arg.isdigit():
            arg = int(arg)
            e_name = getadjvalue(arg, numberList, nameList)
            e_number = arg
            e_symbol = getadjvalue(arg, numberList, symbolList)
        else:
            await ctx.send(
                f"Element {arg} was not found. Try to pass correct capitalization, For example Hydrogen or H")

    except ValueError:
        await ctx.send(f"Element {arg} was not found. Try to pass correct capitalization, For example Hydrogen or H")

    embed = discord.Embed(title="Information", description="For nerds", color=0x1fbff4)
    embed.add_field(name="Element Name", value=e_name, inline=True)
    embed.add_field(name="Atomic Number", value=e_number, inline=True)
    embed.add_field(name="Element Symbol", value=e_symbol, inline=True)
    await ctx.send(embed=embed)


@client.command()
async def fact(ctx, arg):
    fact = factList[int(arg)]
    await ctx.send(fact)


client.run('OTQ0NDg5MzU2NzYzMjMwMjI5.YhCWQg.ZY8tbp1Z9Imsn9QfBEsHzqMAQjc')
