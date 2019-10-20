import discord
from discord.ext import commands
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
import random
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
from discord.utils import get
import urllib.parse, urllib.request, re
import itertools
import copy
from collections import Counter, OrderedDict

start_time = time.time()

bot=commands.Bot(command_prefix='d!')

bot.remove_command('help')

ROLE = "muted" or "Muted"





@bot.event
async def on_ready():
    print('---------------------')
    print('The bot is ready!')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------------')
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="DynamicClan - Watching The Server"))



@bot.command()
async def help(ctx):
        embed2 = discord.Embed(
            colour=discord.Colour.red(),
            title="Commands sent to your dm/pms succesfully!",
            description="Please check your dm/pms!"
        )
        await ctx.send(embed=embed2)
        embed = discord.Embed(
                colour=discord.Colour.blue(),
                title="help",
                description="Shows this message"
        )
        embed.set_author(name="Commands", icon_url="https://cdn.discordapp.com/attachments/594372156209758226/604968187624161290/download.jpg")
        embed.add_field(name="ping", value="Pong!", inline=False)
        embed.add_field(name="ban", value="Bans a member", inline=False)
        embed.add_field(name="kick", value="Kicks a member", inline=False)
        embed.add_field(name="Dev", value="Shows who helped make this code", inline=False)
        embed.add_field(name="meme", value="Sends a meme", inline=False)
        embed.add_field(name="oof", value="Says oof", inline=False)
        embed.add_field(name="role", value="Gives a member a role still being fixed", inline=False)
        embed.add_field(name="ytsearch", value="This searches and gives results of youtube, only gives 2 results so not to spam! So please try be a little specific.", inline=False)
        embed.add_field(name="unban", value="Unbans a user! example how to use ^unban Test#3333", inline=False)
        embed.add_field(name="random", value="Sends a random word or number.", inline=False)
        embed.add_field(name="smack", value="Smacks someone.", inline=False)
        embed.add_field(name="pat", value="Pats someone.", inline=False)
        embed.add_field(name="hug", value="Hugs someone.", inline=False)
        embed.add_field(name="kiss", value="Kisses someone.", inline=False)
        embed.add_field(name="owo", value="owo someone", inline=False)
        embed.add_field(name="8ball", value="ask the bot a question", inline=False)
        embed.add_field(name="dog", value="Sends a random dog image", inline=False)
        embed.add_field(name="cat", value="Sends a random cat image", inline=False)
        embed.add_field(name="info", value="Gets user info", inline=False)
        embed.add_field(name="rate", value="Rate something", inline=False)
        embed.add_field(name="echo", value="Echos whatever you say.", inline=False)
        embed.add_field(name="purge", value="Deletes messages with an amount.", inline=False)
        embed.add_field(name="nick", value="Nicknames someone", inline=False)
        embed.add_field(name="mute", value="Mutes a member", inline=False)
        embed.add_field(name="unmute", value="UnMutes a member", inline=False)
        embed.set_footer(text="Made by Nexus")

        
        await ctx.author.send(embed=embed)


@bot.command()
async def oof(ctx):
        await ctx.send('oof')
        await ctx.message.delete()
@bot.command()
async def Og(ctx):
        await ctx.send('Thought')
        await ctx.send('you arent og enough')
        await ctx.message.delete()
@bot.command(pass_context=True)
@commands.has_role("Admin")
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.message.delete()
    await ctx.send('Ban success!')
    await ctx.send(f'{member} has been banned!')
    print(f"{member} was banned by {ctx.author.mention}!")
@bot.command(pass_context=True)
@commands.has_role("Admin")
async def kick(ctx, member : discord.Member, * , reason=None):
        await member.kick(reason=reason)
        await ctx.message.delete()
        await ctx.send('Kick success!')
        await ctx.send(f'{member} has been kicked!')
        print(f"{member} was kicked by {ctx.author.mention}!")
@bot.command()
async def Dev(ctx):
        await ctx.message.delete()
        embed = discord.Embed(
                colour=discord.Colour.red(),
                title="Developers",
                description="The developers of this bot is Nexus and Sworie"
        )
        embed.set_author(name="Admin helper", icon_url="https://cdn.discordapp.com/attachments/594372156209758226/604968187624161290/download.jpg")
        await ctx.send(embed=embed)

@bot.command()
async def ytsearch(ctx, *, search):

        query_string = urllib.parse.urlencode({
                'search_query': search
        })
        htm_content = urllib.request.urlopen(
                'http://www.youtube.com/results?' + query_string
        )
        search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
        await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
        await ctx.send('http://www.youtube.com/watch?v=' + search_results[2])
        await ctx.send('This cmd is set to 2 results only so not to spam, please be more specific if you did not get what you wanted')
@bot.command()
@commands.has_role("Admin")
async def unban(ctx, *, member):
        await ctx.message.delete()
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                        await ctx.guild.unban(user)
                        await ctx.send(f'Unbanned {member}')
                        print(f'Unbanned {member} by {ctx.author.mention}')
                        return
@bot.command()
@commands.has_role("Admin")
async def purge(ctx, amount=1000):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send("Deleted messages.")
    await asyncio.sleep(3)
    await ctx.channel.purge(limit=1)
@bot.command()
async def meme(ctx):
    memes = [
        "https://cdn.discordapp.com/attachments/471397786613579777/584150839669817344/image0.jpg",
        "https://cdn.discordapp.com/attachments/471397786613579777/584054714925187072/byemom.png",
        "https://cdn.discordapp.com/attachments/471397786613579777/584013133606027286/image0.jpg",
        "https://cdn.discordapp.com/attachments/471397786613579777/584012903749779456/2pYlD19.png",
        "https://cdn.discordapp.com/attachments/471397786613579777/583698535938129929/image0.png",
        "https://cdn.discordapp.com/attachments/471397786613579777/583486555990130688/image0.jpg",
        "https://cdn.discordapp.com/attachments/471397786613579777/583480637713940480/image0.png",
        "https://cdn.discordapp.com/attachments/471397786613579777/583474303975161857/image0.jpg",
        "https://cdn.discordapp.com/attachments/471397786613579777/583470910644682752/eyes.png",
        "https://cdn.discordapp.com/attachments/471397786613579777/583422452332494871/Screenshot_2019-05-30-10-32-10.jpg",
        "https://cdn.discordapp.com/attachments/471397786613579777/583061107359612981/image0.jpg",
        "https://cdn.discordapp.com/attachments/471397786613579777/583043410370494499/unknown.png",
        "https://cdn.discordapp.com/attachments/471397786613579777/583042920047706122/wtf.png",
        "https://cdn.discordapp.com/attachments/471397786613579777/582702902192111666/image0.jpg",
        "https://cdn.discordapp.com/attachments/471397786613579777/582704640597032990/image0.jpg",
        "https://cdn.discordapp.com/attachments/471397786613579777/582698036203880459/image0.jpg",
        "https://cdn.discordapp.com/attachments/471397786613579777/582697670825476116/image0.jpg",
        "https://cdn.discordapp.com/attachments/471397786613579777/582691116621496350/image0.jpg",
        "https://cdn.discordapp.com/attachments/471397786613579777/582467755052367872/image0.jpg",
        "https://cdn.discordapp.com/attachments/471397786613579777/582226635701354516/Untitled7.png",
        "https://cdn.discordapp.com/attachments/471397786613579777/582161702553124864/image0.jpg",
        "https://cdn.discordapp.com/attachments/471397786613579777/581168117754101761/IMG_20190523_181356.png",
        "https://cdn.discordapp.com/attachments/471397786613579777/581081119076646912/image0-21-1-2-1.png",
        "https://cdn.discordapp.com/attachments/471397786613579777/580481784802967562/image0.jpg",
        "This is what happens when you announce new things in the meme era. In early June, Nintendo announced its new Pokémon game, Sword & Shield, along with the game's new starter Pokémon and a few new game features, notably Dynamax, in which you can make your guys really, really big. The internet did what it does, memeing the shit out of the game's news. "
    ]
    await ctx.send(f"meme: {random.choice(memes)}")
@bot.command()
async def ping(ctx):
    embed = discord.Embed(
                colour=discord.Colour.green(),
                title="Pinging..."
        )
    embed.add_field(name=":ping_pong: Pong!:", value=f"Pinged **{round(bot.latency * 1000)}ms**.")
    await ctx.send(embed=embed)
@bot.command(aliases=["random"])
async def _random(ctx):
    or_value = random.randint(1, 2)
    if (or_value == 1):
        number = random.randint(1, 1000)
        await ctx.send(number)
 
    if (or_value == 2):
        words = [
            "Yes",
            "No",
            "What",
            "Value",
            "Or",
            "This",
            "Is",
            "Bad",
            "Good",
            "No",
            "Nothing",
            "None",
            "Shadows",
            "Alone",
            "World",
            "Huh",
            "File"
        ]
 
        await ctx.send(f"{random.choice(words)}")
@bot.command()
async def smack(ctx, *, user: discord.Member):
    who_smacked = ctx.message.author
    await ctx.send(f"{who_smacked.mention} has smacked {user.mention}!")
    gifs = [
        "https://tenor.com/search/dumb-gifs",
        "https://tenor.com/search/cute-gifs",
        "https://tenor.com/view/naruto-anime-wink-smack-gif-12465573",
        "https://tenor.com/view/naru-anime-barakamon-gif-7480906",
        "https://tenor.com/search/akatsuki-no-yona-gifs",
        
    ]
    await ctx.send(f"{random.choice(gifs)}")
@bot.command()
async def hug(ctx, *, user: discord.Member):
    who_hugged = ctx.message.author
    await ctx.send(f"{who_hugged.mention} has hugged {user.mention}!")
    gifs = [
        "https://tenor.com/view/anime-hug-sweet-love-gif-14246498",
        "https://tenor.com/view/anime-bed-bedtime-sleep-night-gif-12375072",
        "https://tenor.com/view/anime-hug-gif-9200935",
        "https://tenor.com/view/anime-jump-small-gif-11098589",
        "https://tenor.com/view/hug-anime-gif-4898650",
        "https://tenor.com/view/cute-anime-hug-love-come-here-gif-7864716",
        "https://tenor.com/view/hug-anime-gif-11074788",
        "https://tenor.com/search/hug-gifs",
        "https://tenor.com/view/chiya-urara-meirochou-anime-saku-gif-8995974",
        "https://tenor.com/view/mika-mikaela-hyakuya-owari-no-gif-7419864",
        "https://tenor.com/view/hug-cry-sad-anime-tackle-gif-5634582",
        "https://tenor.com/view/anime-cute-sweet-hug-gif-12668677",
        "https://tenor.com/view/hug-loli-cute-cat-neko-gif-5210972"
    ]
    await ctx.send(f"{random.choice(gifs)}")
@bot.command()
async def pat(ctx, *, user: discord.Member):
    who_patted = ctx.message.author
    await ctx.send(f"{who_patted.mention} has patted {user.mention}!")
    gifs = [
        "https://media1.tenor.com/images/8c1a53522a74129607b870910ac288f9/tenor.gif?itemid=7220650",
        "https://media1.tenor.com/images/e01e09d8e27c7247314b3dd611f47007/tenor.gif?itemid=13912621",
        "https://media1.tenor.com/images/88ff65d668f92f6d953dbffcbed2be5f/tenor.gif?itemid=4953911",
        "https://media1.tenor.com/images/63ccd3a45ec323ac5b199317b7cb3128/tenor.gif?itemid=12290276",
        "https://media1.tenor.com/images/3fc9d04c3aab73f5ce1ffdca2b87d894/tenor.gif?itemid=11573062",
        "https://media1.tenor.com/images/a661b668b4757d1ccfde34feb6deb188/tenor.gif?itemid=5709072",
        "https://media1.tenor.com/images/88ff65d668f92f6d953dbffcbed2be5f/tenor.gif?itemid=4953911"
    ]
 
    await ctx.send(f"{random.choice(gifs)}")
 
@bot.command()
async def owo(ctx, *, user: discord.Member):
    who_owoed = ctx.message.author
    await ctx.send(f"{who_owoed.mention} has owoed {user.mention}!")
    gifs = [
        "https://media1.tenor.com/images/089876f278721ed7aba4fa8328f1e167/tenor.gif?itemid=14123081",
        "https://media1.tenor.com/images/23fed1630256743167f2190e4fb52a37/tenor.gif?itemid=13311620",
        "https://media1.tenor.com/images/f5bc4d03d3c78d585508945daead8a7e/tenor.gif?itemid=13261583"
    ]
 
    await ctx.send(f"{random.choice(gifs)}")
@bot.command()
async def dog(ctx):
    gifs = [
        "https://media1.tenor.com/images/3c1073e2391a972945a17a402d67b2cb/tenor.gif?itemid=10095569",
        "https://media1.tenor.com/images/e00c5b2fc80ee6d77172e8173f002136/tenor.gif?itemid=12144452",
        "https://media.tenor.com/images/6c2cda3d364bb30bada456deae08e792/tenor.gif",
        "https://media.tenor.com/images/1e0efe30b6bcde14a7181b2786c59c2d/tenor.gif",
        "https://media.tenor.com/images/01f60261bf0a236e55979757b818c6dd/tenor.gif",
        "https://media1.tenor.com/images/2ca84ade7c98f11b4df82654b1ac081d/tenor.gif?itemid=5079887",
        "https://media.tenor.com/images/f88fab433db9351e75ddafa06933ff16/tenor.gif"
    ]
    await ctx.send(f"{random.choice(gifs)}")
@bot.command()
async def cat(ctx):
    gifs = [
        "https://media1.tenor.com/images/9730e751d3d952aa9bd62a5ae4c9e9dc/tenor.gif?itemid=5756839",
        "https://media.tenor.com/images/75b3c8eca95d917c650cd574b91db7f7/tenor.gif",
        "https://media.tenor.com/images/2b9f9c14f25c4b3bbdb2ffa7b821b920/tenor.gif",
        "https://media.tenor.com/images/0799eab3543505117564825efcc03ef3/tenor.gif",
        "https://media.tenor.com/images/034a09d2088b3cb947d3764d6886d767/tenor.gif",
        "https://media.tenor.com/images/656f964efaabc3a5c91d452d109b5a55/tenor.gif",
        "https://media.tenor.com/images/bb33cc1eaafa266ac1092ecff7c1c85d/tenor.gif"
    ]
    await ctx.send(f"{random.choice(gifs)}")
@bot.command()
async def rate(ctx):
    number = random.randint(0, 10)
    await ctx.send(f"I would rate it {number}/10.")
@bot.command()
async def embed(ctx, *args):
    output = ''
    for word in args:
        output += word
        output += ' '
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name=ctx.message.author)
    embed.add_field(name='Embed', value=output)
    embed.set_footer(text='Time:')
    
    await ctx.send(embed=embed)
    await ctx.message.delete()
@bot.command()
async def invite(ctx):
    embed = discord.Embed(
        colour = discord.Colour.purple()
    )
    embed.set_author(name="Here you go, enjoy!")
    embed.add_field(name="Invite link", value="http://bit.ly/Adminhelper")
    await ctx.send(embed=embed)
@bot.command()
async def echo(ctx, *args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await ctx.send(output)
    await ctx.message.delete()
@bot.command()
async def status(ctx, *args):
    if ctx.message.author.id == 441212840410611722 or ctx.message.author.id == 394227514786185217 or ctx.message.author.id == 456678423625072683:
        output = ''
        for word in args:
            output += word
            output += ' '
            await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=output))
@bot.command(pass_context = True)
async def staff(ctx):

    if not ctx.message.author.server_permissions.administrator:
        await ctx.send("permission denied")
    else:
        await ctx.send('permission granted')
@bot.command()
@commands.has_role("Admin")
async def poll(ctx, *args):

    if not ctx.message.author.server_permissions.administrator:
        await ctx.send("permission denied")
    else:
        question = ''
    for word in args:
        question += word
        question += ' '
    await ctx.channel.purge(limit=1)
    await ctx.send("@everyone")
    embed = discord.Embed(
        colour = discord.Colour.purple()
    )
    embed.set_author(name="Poll")
    embed.add_field(name="Question", value=question, inline=False)
    embed.set_footer(text="👍 for Yes, 👎 for No.")
    await ctx.send(embed=embed)
@bot.command()
@commands.has_role("Admin")
async def nick(ctx, user: discord.Member, nickname):
    embed = discord.Embed()
    embed.set_author(name=f"Changed {user}s NickName")
    await user.edit(nick=nickname)
    await ctx.send(embed=embed)
@bot.command()
async def gen(ctx):
    accs = [
        "acc here",
        "acc here",
        "acc here",
        "acc here",
        "acc here",
        "acc here"
    ]

    await ctx.send(f"{random.choice(accs)}")
@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
    if ctx.message.author.id == 441212840410611722:
        role = get(member.guild.roles, name="Muted")
        await member.add_roles(role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await ctx.send(embed=embed)
    else:
       embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
       await ctx.send(embed=embed)
@bot.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
    if ctx.message.author.id == 441212840410611722:
        role = get(member.guild.roles, name="Muted")
        await member.remove_roles(role)
        embed=discord.Embed(title="User UnMuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await ctx.send(embed=embed)
    else:
       embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
       await ctx.send(embed=embed)
@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely',
                 'You may rely on it',
                 'As I see it, yes.',
                 'Most likely',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    embed = discord.Embed(
        colour = discord.Colour.purple()
    )
    embed.set_author(name=' 8 Ball')
    embed.add_field(name=f'Question: {question}', value=f':8ball: Answer: {random.choice(responses)}')
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def uptime(ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed=discord.Embed(title="Uptime", description=text, color=ctx.message.author.top_role.colour)
        await ctx.send(embed=embed)
@bot.command()
async def info(ctx, user: discord.Member):
    if not user:
        user = ctx.message.author
    roles = [role.name.replace("@", "@") for role in user.roles]
    voice_channel = user.voice
    if voice_channel is not None:
        voice_channel = voice_channel.channel.name
    else:
        voice_channel = "Not in a voice channel."
    embed = discord.Embed(
        colour = discord.Colour.red()
    )
   
    embed.set_author(name=f"{user}'s info")
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Bot", value=user.bot, inline=True)
    embed.add_field(name="Voice channel", value=voice_channel, inline=True)
    embed.add_field(name="Joined", value=user.joined_at, inline=True)
    embed.add_field(name="Created", value=user.created_at, inline=True)
    embed.add_field(name="Highest role", value=user.top_role, inline=True)
    embed.add_field(name="Roles", value=roles, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
@bot.command()
async def avatar(ctx, user: discord.Member):
        if user is None:
            user = ctx.author
        embed = discord.Embed(title="Avatar",
                            color = discord.Color.blue())
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)
@bot.command()
async def serverinfo(ctx):
        guild = ctx.guild
        person_count = len([member for member in guild.members if not member.bot])
        bot_count = len([member for member in guild.members if member.bot])
        msg = "ID: " + str(guild.id) + "\nCreated on: " + str(guild.created_at) + "\nRegion: " + str(guild.region) + "\nMember count: " + str(len(guild.members)) + "\nHumans: " + str(person_count) + "\nBots: " + str(bot_count) + "\nOwner: " + str(guild.owner) + "\n"
        embed = discord.Embed(description=msg,
                            color=discord.Color.green())
        embed.title = guild.name
        if guild.icon_url:
            embed.set_thumbnail(url=guild.icon_url)
        await ctx.send(embed=embed)
@bot.command()
async def nsfwtest(ctx):
    if ctx.channel.is_nsfw():
        await ctx.send("This channel is marked nsfw!")
    else:
        await ctx.send("This channel is not marked nsfw!")
@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(title="What this is for?", description="Just a little info about this bot", color=0xeee657)
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    embed.add_field(name="Invite link", value="https://discordapp.com/api/oauth2/authorize?client_id=634884520067203092&permissions=8&scope=bot")
    embed.add_field(name="Dev of this bot", value="The dev of this bot is Nexus")
    embed.add_field(name="Wanna know someone who is super important to Nexus?", value="His name is Nexus means everything to my owner")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def test(ctx):
    guild = ctx.guild
    await guild.create_role(name="Test")
    return
@bot.command(pass_context=True)
async def roles(ctx):
    await ctx.send("Making roles...")
    guild = ctx.guild
    await guild.create_role(name="Owner")
    await guild.create_role(name="Co-Owner")
    await guild.create_role(name="Developer")
    await guild.create_role(name="Head-Admin")
    await guild.create_role(name="Senior-Admin")
    await guild.create_role(name="Admin")
    await guild.create_role(name="Junior-Admin")
    await guild.create_role(name="Discord-Manager")
    await guild.create_role(name="Senior-Mod")
    await guild.create_role(name="Mod")
    await guild.create_role(name="Junior-Mod")
    await guild.create_role(name="Helper")
    await guild.create_role(name="Bots")
    await guild.create_role(name="Guest")
    await ctx.send("Done!")
    return
@bot.command(pass_context=True)
async def delrolestest(ctx):
    await ctx.send("Deleting roles...")
    guild = ctx.guild
    await guild.delete_role(name="Owner")
    await guild.delete_role(name="Co-Owner")
    await guild.delete_role(name="Developer")
    await guild.delete_role(name="Head-Admin")
    await guild.delete_role(name="Senior-Admin")
    await guild.delete_role(name="Admin")
    await guild.delete_role(name="Junior-Admin")
    await guild.delete_role(name="Discord-Manager")
    await guild.delete_role(name="Senior-Mod")
    await guild.delete_role(name="Mod")
    await guild.delete_role(name="Junior-Mod")
    await guild.delete_role(name="Helper")
    await guild.delete_role(name="Bots")
    await guild.delete_role(name="Guest")
    await ctx.send("Done!")
    return
@bot.command(pass_context=True)
async def delroletest(ctx, *,role_name):
  role = discord.utils.get(ctx.message.server.roles, name=role_name)
  if role:
    try:
      await ctx.guild.delete_role(ctx.message.server, role)
      await ctx.send("The role {} has been deleted!".format(role.name))
    except discord.Forbidden:
      await ctx.send("Missing Permissions to delete this role!")
  else:
    await ctx.send("The role doesn't exist!")

bot.run("NjM0ODg0NTIwMDY3MjAzMDky.XapAYw.KgX8JoJaKB2K78BvyI1umGB2zIY")