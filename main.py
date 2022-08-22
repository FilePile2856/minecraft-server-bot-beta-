import discord
from discord.ext import commands
from mcstatus import JavaServer
import time

app = commands.Bot(command_prefix="!")

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("서비스 시작중...")
    await app.change_presence(status=discord.Status.online, activity=game)


@app.command(name='unmute')
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="mute")
    await member.remove_roles(mutedRole)
    #await member.send(f" you have unmutedd from: - {ctx.guild.name}")
    embed = discord.Embed(title="unmute", description=f" {member.mention}",colour=discord.Colour.light_gray())
    await ctx.send(embed=embed)
@app.command(name="mute")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="mute")

    if not mutedRole:
        mutedRole = await guild.create_role(name="mute")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention}", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    #await member.send(f" you have been muted from: {guild.name} reason: {reason}")
@app.command(name='cs')
async def roll(ctx,ip):
    try:
        server = JavaServer.lookup(f"{ip}")
        status = server.status()
    except: 
        print("서버가 오프라인입니다.")
        await ctx.send("서버가 오프라인입니다.")
    else:
        embed = discord.Embed(title=f"{ip}", color=0x62c1cc)
        embed.add_field(
            name='player', value=f'{status.players.online}/{status.players.max}')
        embed.add_field(name='version', value=f'{status.version.name}')
        player_list = []
        if status.players.online == 0:
            print("no player")
        else:
            for player in status.players.sample:
                #player_list.append(f' {player.name} {{{player.id}}}')
                player_list.append(f' {player.name} ')
        embed.add_field(name='player list',
                        value=f'{player_list}', inline=False)

        
        await ctx.send(embed=embed)  
@app.command(name='vote')
async def vote(ctx,description,one,two):
    
    embed = discord.Embed(title=f"투표", color=0x62c1cc)
    embed.add_field(
        name='내용', value=f'{description}')
    embed.add_field(name=f'{one}', value=f'1️⃣클릭', inline=False)
    embed.add_field(name=f'{two}', value=f'2️⃣클릭', inline=False)
    msg = await ctx.send(embed=embed)  
    await msg.add_reaction('1️⃣')
    await msg.add_reaction('2️⃣')

@app.command(name='s')
async def roll(ctx):
    try:
        server = JavaServer.lookup("filepile.xyz")
        status = server.status()
    except: 
        print("서버가 오프라인입니다.")
        await ctx.send("서버가 오프라인입니다.")
    else:
        embed = discord.Embed(title="filepile.xyz", color=0x62c1cc)
        embed.add_field(
            name='player', value=f'{status.players.online}/{status.players.max}')
        embed.add_field(name='version', value=f'{status.version.name}')
        player_list = []
        if status.players.online == 0:
            print("no player")
        else:
            for player in status.players.sample:
                #player_list.append(f' {player.name} {{{player.id}}}')
                player_list.append(f' {player.name} ')
        embed.add_field(name='player list',
                        value=f'{player_list}', inline=False)
        
        await ctx.send(embed=embed)  

app.run('Nzc4NTU3NTI1NzEyMDQ0MDQy.GbPDKM.aBQr78E13c7PJiNwemQpBhOVRIUnNTvjweG35A')
