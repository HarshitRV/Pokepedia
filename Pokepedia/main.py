import discord 
import random
import asyncio
import os
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='++')
bot.remove_command('help')

#----------------------------------------------------------------ON READY EVENT--------------------------------------------------------------
@bot.event
async def on_ready():
  print("Entered in Poke World as {0.user}".format(bot))
async def ch_presence():
  await bot.wait_until_ready()

  statuses = ["Gaining Knowledge", f"on {len(bot.guilds)} servers | ++help", "Dev : WOLVERINE911/Lucitor","Gotta Catch ’Em All!","Support Server : pbRtbJX5Sf"]
  while not bot.is_closed():
    status = random.choice(statuses)
    await bot.change_presence(activity=discord.Game(name=status))
    await asyncio.sleep(15)
bot.loop.create_task(ch_presence())

#----------------------------------------------------------------HELP Command------------------------------------------------------------------
@commands.command(aliases=['help','h'])
async def halp(ctx):
  embed=discord.Embed(
    title='Help\n-------------------------',
    description='Join our [support server](https://discord.gg/pbRtbJX5Sf)\nChekout [github repository](https://github.com/lucifer00911/Pokepedia)\nInvite [Pokepedia](https://discord.com/oauth2/authorize?client_id=804665852221325342&permissions=379968&scope=bot)\nVote us on [top.gg](https://top.gg/bot/804665852221325342/vote)\n-------------------------',
    color=0xff00ff
  )
  embed.add_field(name='Prefix',
  value='++',inline=False)
  embed.add_field(name='Commands',
  value='bug\ndark\ndragon\nelectric\nfairy\nfighting\nfire\nflying\nghost\ngrass\nground\nice\nnormal\npoison\npsychic\nrock\nsteel\nwater',inline=False)
  embed.set_footer(text='Use ++invite to invite the bot')
  embed.add_field(name='++search / ++s',value='Search Pokemon by number eg : ++s 1',inline=False)
  embed.add_field(name='++name',value='Search Pokemon images by name try : ++name pikachu',inline=False)
  embed.add_field(name='For giff lovers',value='Try ++giff',inline=False)
  embed.set_thumbnail(url="https://i.pinimg.com/originals/ce/cc/91/cecc913aee77c99b18d2043dbbd8bd72.gif")
  await ctx.send(embed=embed)

bot.add_command(halp)

#-----------------------------------------------------------------INVITE command------------------------------------------------------------------
@commands.command()
async def invite(ctx):
  embed=discord.Embed(title='Pokepedia',description='\n**Invite Link :** [Invite](https://discord.com/api/oauth2/authorize?client_id=804665852221325342&permissions=379968&scope=bot)\n**Support Server :** [Support](https://discord.gg/pbRtbJX5Sf)',
  color=0x00ffff)
  embed.set_thumbnail(url='https://media.tenor.com/images/27215c1c6dbaca5d396184e5f8f7a73f/tenor.gif')
  await ctx.send(embed=embed)
bot.add_command(invite)

#------------------------------------------------------------------ping command-------------------------------------------------------------------
@commands.command()
async def ping(ctx):
  embed=discord.Embed(title='PONG !',description=f'{round(bot.latency * 1000)}ms',color=0xF00091 )
  await ctx.send(embed=embed)
bot.add_command(ping)

#------------------------------------------------------------------NORMAL TYPE--------------------------------------------------------------------

@commands.command()
async def normal(ctx):
    embed=discord.Embed(
      title='Normal Type',
      description='**Weak Against** : Rock, Ghost, Steel \n**Resistant To**: Ghost \n**Vulnerable To**: Fighting',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://pa1.narvii.com/5708/3511f39bb779ae788144cd1cad1bb1361fc5261c_128.gif")
    await ctx.send(embed=embed)
bot.add_command(normal)

#----------------------------------------------------------------FIGHTING TYPE--------------------------------------------------------------------

@commands.command()
async def fighting(ctx):
    embed=discord.Embed(
      title='Fighting Type',
      description='**Strong Against**: Normal, Rock, Steel, Ice, Dark\n**Weak Against** : Flying, Poison, Psychic, Bug, Ghost, Fairy \n**Resistant To**: Rock, Bug, Dark\n**Vulnerable To**:Flying, Psychic, Fairy',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/808989014069346304/448484.gif")
    await ctx.send(embed=embed)
bot.add_command(fighting)

#----------------------------------------------------------------FLYING TYPE----------------------------------------------------------------------

@commands.command()
async def flying(ctx):
  embed=discord.Embed(
      title='Flying Type',
      description='**Strong Against**: Fighting, Bug, Grass\n**Weak Against** : Rock, Steel, Electric \n**Resistant To**: Fighting, Ground, Bug, Grass\n**Vulnerable To**:Rock, Electric, Ice',
      color=0xffd700
    )
  embed.set_thumbnail(url="https://graphics.tppcrpg.net/xy/shiny/398M.gif")
  await ctx.send(embed=embed)
bot.add_command(flying)

#----------------------------------------------------------------POISON TYPE----------------------------------------------------------------------

@commands.command()
async def poison(ctx):
    embed=discord.Embed(
      title='Poison Type',
      description='**Strong Against**: Grass, Fairy\n**Weak Against** : Poison, Ground, Rock, Ghost, Steel\n**Resistant To**:Fighting, Poison, Grass, Fairy\n**Vulnerable To**:Ground, Psychic',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805749181485678632/848488.gif")
    await ctx.send(embed=embed)
bot.add_command(poison)

#-----------------------------------------------------------------GROUND TYPE---------------------------------------------------------------------

@commands.command()
async def ground(ctx):
    embed=discord.Embed(
      title='Ground Type',
      description='**Poison, Rock, Steel, Fire, Electric\n**Weak Against** : Flying, Bug, Grass \n**Resistant To**: Poison, Rock, Electric\n**Vulnerable To**:Water, Grass, Ice',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805116049430675486/1111.gif")
    await ctx.send(embed=embed)
bot.add_command(ground)

#-----------------------------------------------------------------ROCK TYPE------------------------------------------------------------------------

@commands.command()
async def rock(ctx):
    embed=discord.Embed(
      title='Rock Type',
      description='**Strong Against**: Flying, Bug, Fire, Ice\n**Weak Against** : Fighting, Ground, Steel\n**Resistant To**: Normal, Flying, Poison, Fire\n**Vulnerable To**:Fighting, Ground, Steel, Water, Grass',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805116673707081759/11112.gif")
    await ctx.send(embed=embed)
bot.add_command(rock)

#------------------------------------------------------------------BUGG TYPE----------------------------------------------------------------------

@commands.command()
async def bug(ctx):
    embed=discord.Embed(
      title='Bug Type',
      description='**Strong Against**: Grass, Psychic, Dark\n**Weak Against** : Fighting, Flying, Poison, Ghost, Steel, Fire, Fairy\n**Resistant To**: Fighting, Ground, Grass\n**Vulnerable To**:Fighting, Ground, Grass',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805748308839891004/984889.gif")
    await ctx.send(embed=embed)
bot.add_command(bug)

#------------------------------------------------------------------GHOST TYPE----------------------------------------------------------------------

@commands.command()
async def ghost(ctx):
    embed=discord.Embed(
      title='Ghost Type',
      description='**Strong Against**: Ghost, Psychic\n**Weak Against** : Normal, Dark\n**Resistant To**:Normal, Fighting, Poison, Bug\n**Vulnerable To**:Ghost, Dark',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805125156338139166/4848.gif")
    await ctx.send(embed=embed)
bot.add_command(ghost)

#------------------------------------------------------------------STEEL TYPE----------------------------------------------------------------------

@commands.command()
async def steel(ctx):
    embed=discord.Embed(
      title='Steel Type',
      description='**Strong Against**:Rock, Ice, Fairy\n**Weak Against** : Steel, Fire, Water, Electric\n**Resistant To**: Normal, Flying, Poison, Rock, Bug, Steel, Grass, Psychic, Ice, Dragon, Fairy\n**Vulnerable To**:Fighting, Ground, Fire',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://media.giphy.com/media/ZBexIRI4raU0YIruAW/giphy.gif")
    await ctx.send(embed=embed)
bot.add_command(steel)

#------------------------------------------------------------------FIRE TYPE----------------------------------------------------------------------

@commands.command()
async def fire(ctx):
    embed=discord.Embed(
      title='Fire Type',
      description='**Strong Against**:Bug, Steel, Grass, Ice\n**Weak Against** : Rock, Fire, Water, Dragon\n**Resistant To**: Bug, Steel, Fire, Grass, Ice\n**Vulnerable To**:Ground, Rock, Water',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805126023417954324/154848.gif")
    await ctx.send(embed=embed)
bot.add_command(fire)

#------------------------------------------------------------------WATER TYPE----------------------------------------------------------------------

@commands.command()
async def water(ctx):
    embed=discord.Embed(
      title='Water Type',
      description='**Strong Against**: Ground, Rock, Fire\n**Weak Against** : Water, Grass, Dragon\n**Resistant To**:Steel, Fire, Water, Ice\n**Vulnerable To**:Grass, Electric',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805118376816017418/45545.gif")
    await ctx.send(embed=embed)
bot.add_command(water)

#------------------------------------------------------------------GRASS TYPE----------------------------------------------------------------------

@commands.command()
async def grass(ctx):
    embed=discord.Embed(
      title='Grass Type',
      description='**Strong Against**: Ground, Rock, Water\n**Weak Against** : Flying, Poison, Bug, Steel, Fire, Grass, Dragon\n**Resistant To**: Ground, Water, Grass, Electric\n**Vulnerable To**:Flying, Poison, Bug, Fire, Ice',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://i.gifer.com/4o45.gif")
    await ctx.send(embed=embed)
bot.add_command(grass)

#------------------------------------------------------------------ELECTRIC TYPE-------------------------------------------------------------------

@commands.command()
async def electric(ctx):
    embed=discord.Embed(
      title='Electric Type',
      description='**Strong Against**: Flying, Water\n**Weak Against** : Ground, Grass, Electric, Dragon\n**Resistant To**:Flying, Steel, Electric\n**Vulnerable To**:Ground',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://img1.picmix.com/output/stamp/normal/4/8/0/4/1604084_93e2e.gif")
    await ctx.send(embed=embed)
bot.add_command(electric)

#------------------------------------------------------------------PSYCHIC TYPE--------------------------------------------------------------------

@commands.command()
async def psychic(ctx):
    embed=discord.Embed(
      title='Psychic Type',
      description='**Strong Against**: Fighting, Poison\n**Weak Against** : Steel, Psychic, Dark\n**Resistant To**: Fighting, Psychic\n**Vulnerable To**:Bug, Ghost, Dark',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805119836689530893/65564.gif")
    await ctx.send(embed=embed)
bot.add_command(psychic)

#-----------------------------------------------------------------ICE TYPE-------------------------------------------------------------------------

@commands.command()
async def ice(ctx):
    embed=discord.Embed(
      title='Ice Type',
      description='**Strong Against**: Flying, Ground, Grass, Dragon\n**Weak Against** : Steel, Fire, Water, Ice\n**Resistant To**:Ice\n**Vulnerable To**:Fighting, Rock, Steel, Fire',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://i.gifer.com/YX4X.gif")
    await ctx.send(embed=embed)
bot.add_command(ice)

#------------------------------------------------------------------DRAGON TYPE---------------------------------------------------------------------

@commands.command()
async def dragon(ctx):
    embed=discord.Embed(
      title='Dragon Type',
      description='**Strong Against**:Dragon\n**Weak Against** : Steel, Fairy\n**Resistant To**: Fire, Water, Grass, Electric\n**Vulnerable To**:Ice, Dragon, Fairy',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://i.gifer.com/4hsh.gif")
    await ctx.send(embed=embed)
bot.add_command(dragon)

#------------------------------------------------------------------FAIRY TYPE----------------------------------------------------------------------

@commands.command()
async def fairy(ctx):
    embed=discord.Embed(
      title='Fairy Type',
      description='**Strong Against**: Fighting, Dragon, Dark\n**Weak Against** : Poison, Steel, Fire\n**Resistant To**: Fighting, Bug, Dragon, Dark\n**Vulnerable To**:Poison, Steel',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://thumbs.gfycat.com/OddBiodegradableAmphiuma-max-1mb.gif")
    await ctx.send(embed=embed)
bot.add_command(fairy)

#------------------------------------------------------------------DARK TYPE-----------------------------------------------------------------------

@commands.command()
async def dark(ctx):
    embed=discord.Embed(
      title='Dark Type',
      description='**Strong Against**: Ghost, Psychic\n**Weak Against** :Fighting, Dark, Fairy\n**Resistant To**:Ghost, Psychic, Dark\n**Vulnerable To**:Fighting, Bug, Fairy',
      color=0xffd700
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805121442869018624/65165.gif")
    await ctx.send(embed=embed)
bot.add_command(dark)

##--------------------------------------------------- SEARCH BY NUMBER COMMAND----------------------------------------------------------------------

@commands.command(aliases=['s'])
async def search(ctx,i=1):

  try:
    req = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + '{:03d}'.format(i) + '.png'
    embed=discord.Embed(title='{:03d}'.format(i),color=0xffd700)
    embed.set_image(url=req)
    embed.set_footer(text='Invite me using ++invite')
    await ctx.send(embed=embed)
  except Exception as e:

    await ctx.send("Error Occured for Pokemon " + '{:04d}'.format(i))
    print(str(e))

bot.add_command(search)

#------------------------------------------------------SEARCH BY NAME COMMAND----------------------------------------------------------------------

@commands.command(aliases=['name'])
async def sName(ctx,*,name='no'):

  try:
    req='https://img.pokemondb.net/artwork/large/'+name+'.jpg'
    embed=discord.Embed(title=name,color=0xffd700)
    embed.set_image(url=req)
    embed.set_footer(text='No Image ? Spell Check and try again !')
    await ctx.send(embed=embed)
  except Exception as e:

    await ctx.send("```Check name and Try again !```")
    print(str(e))

bot.add_command(sName)

#------------------------------------------------------------INVOKES ALL COMMANDS----------------------------------------------------------------------

@commands.command(aliases=['IO','all'])
async def call_all(ctx):
  await bug(ctx)
  await asyncio.sleep(3)
  await dark(ctx)
  await asyncio.sleep(3)
  await dragon(ctx)
  await asyncio.sleep(3)
  await electric(ctx)
  await asyncio.sleep(3)
  await fairy(ctx)
  await asyncio.sleep(3)
  await fighting(ctx)
  await asyncio.sleep(3)
  await fire(ctx)
  await asyncio.sleep(3)
  await flying(ctx)
  await asyncio.sleep(3)
  await ghost(ctx)
  await asyncio.sleep(3)
  await grass(ctx)
  await asyncio.sleep(3)
  await ground(ctx)
  await asyncio.sleep(3)
  await ice(ctx)
  await asyncio.sleep(3)
  await normal(ctx)
  await asyncio.sleep(3)
  await poison(ctx)
  await asyncio.sleep(3)
  await psychic(ctx)
  await asyncio.sleep(3)
  await rock(ctx)
  await asyncio.sleep(3)
  await steel(ctx)
  await asyncio.sleep(3)
  await water(ctx)
  await asyncio.sleep(3)
  await ctx.send("```That's All !```")
bot.add_command(call_all)

#------------------------------------------------------------------GIFF COMMAND--------==----------------------------------------------------------
@commands.command()
async def giff(ctx):
  embed=discord.Embed(
    title='Gif Commands',
    description='Try these commands on your server for some cool gifs eg : ++g mystic',
    color=0xff00ff
  )
  embed.add_field(name='Giffs [use ++g then name of gifs listed below]',value='1.Hypnosis Pika(++g hp)\n2.Mystic Logo(++g my)\n3.Valor Logo(++g va)\n4.Instinct Logo(++g in)\n5.Dancing Dragonite(++g dance)',inline=False)
  embed.set_thumbnail(url='https://i.imgur.com/OqMXWbD.jpg')
  embed.set_footer(text='Join our support server for adding custom gifs')
  await ctx.author.send(embed=embed)
  await ctx.send("``Check DM``")
bot.add_command(giff)
#-------------------------------------------------------------------GIFFS COMMAND-------------------------------------------------------------------
@commands.command(aliases=['g'])
async def giffs(ctx,*,name='empty'):
    if name=='empty':
        await ctx.send('```Give following parameters : hp , mystic , valor , in , dance```')
    if name=='hp':
        await ctx.send("https://emojis.slackmojis.com/emojis/images/1450458394/182/pikachu.gif?1450458394")
        await ctx.message.delete()
    if name=='mystic':
        await ctx.send("https://emojis.slackmojis.com/emojis/images/1469201975/673/mystic.gif?1469201975")
        await ctx.message.delete()
    if name=='dance':
        await ctx.send("https://emojis.slackmojis.com/emojis/images/1469223471/679/charmander_dancing.gif?1469223471")
        await ctx.message.delete()
    if name=='valor':
        await ctx.send("https://emojis.slackmojis.com/emojis/images/1469202036/674/valor.gif?1469202036")
        await ctx.message.delete()
    if name=='in':
        await ctx.send("https://emojis.slackmojis.com/emojis/images/1469201940/672/instinct.gif?1469201940")
        await ctx.message.delete()
bot.add_command(giffs)

#DEVLOPED BY : WOLVERINE#3940
#LINKEDIN : https://www.linkedin.com/in/harshit-kr-vishwakarma-b57b8b175/


keep_alive()  #host your bot on a local server [not mandatory]
bot.run(os.getenv('TOKEN'))  #created a .env file and save TOKEN of the bot as TOKEN=  Your Token without "" or ''
