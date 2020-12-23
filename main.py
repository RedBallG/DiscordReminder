from discord.ext import commands
import discord
import os, time
import asyncio
from random import randint
import datetime

#Main Code
bot = commands.Bot(command_prefix='!',description="RedBall's Reminder Bot")
bot.remove_command('help')


yellow = 0xeee657
red = 0xff0000
green = 0x32cd32
purple = 0x6a0dad


def has_role():
    async def predicate(ctx): 
        if not ctx.guild:
            return True

        bot_user_role_name = "Bot User"  
        bot_user = discord.utils.get(ctx.author.roles, name=bot_user_role_name)
        if bot_user in ctx.author.roles or ctx.author.id in [301926219786616832]:
            return True
        else:
            embed = discord.Embed(color=red, title=f'You do not have the "Bot User" role!')
            embed.set_footer(text='Bot made RedBall#7604')
            await ctx.send(embed=embed)
            return False
    return commands.check(predicate)

@bot.event
async def on_ready():
    #os.system("cls")
    print("I'm In!")
    await bot.change_presence(activity=discord.Game(name='Reminding!!'))

@bot.command()
async def ping(ctx):
    embed = discord.Embed(color=green, title='Pong! {0}'.format(round(bot.latency, 1)))
    embed.set_footer(text='Bot made RedBall#7604')
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(color=green)
    embed.add_field(name='!remind ROLE MESSAGE', value='This command will dm everyone in the server with the role you mentioned with your desired message. When running the message, you must type the role name with correct capitalization. Do NOT mention the role but just type the role name. After you type your message.', inline=False)
    embed.set_footer(text='Bot made RedBall#7604')
    await ctx.send(embed=embed)

@bot.command()
@has_role()
async def remind(ctx, roletomsg, *msg):
    start = True
    message = ""
    for char in msg:
        if start:
            message = char
            start = False
        else:
            message = message + " " + char
    print(message)
    role = discord.utils.get(ctx.guild.roles, name=roletomsg)
    if role is None:
        embed = discord.Embed(color=red, title=f'There is no "{roletomsg}" role on this server!')
        embed.set_footer(text='Bot made RedBall#7604')
        await ctx.send(embed=embed)
        return
    empty = True
    for member in ctx.guild.members:
        if role in member.roles:
            #await bot.say("{0.name}: {0.id}".format(member))
            print("{0.name}: {0.id}".format(member))
            try:
                try:
                    embed = discord.Embed(color=green, title=message)
                    embed.set_footer(text='Bot made RedBall#7604')
                    await member.send(embed=embed)
                except:
                    await member.send(message)
                await asyncio.sleep(1)
            except:
                pass
            empty = False
    if empty:
        embed = discord.Embed(color=red, title=f'No one has the role, {roletomsg}')
        embed.set_footer(text='Bot made RedBall#7604')
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(color=green, title=f'Reminded everyone with {roletomsg} role!')
        embed.set_footer(text='Bot made RedBall#7604')
        await ctx.send(embed=embed)
    




#Starting Bot
token = ""

bot.run(token)