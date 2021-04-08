import discord 
import random
import asyncio
import os
import datetime
from discord.ext import commands
from keep_alive import keep_alive
bot = commands.Bot(command_prefix='++')
bot.remove_command('help')

@bot.event
async def on_ready():
  print("Entered in Poke World as {0.user}".format(bot))
async def ch_presence():
  await bot.wait_until_ready()

  statuses = ["Gaining Knowledge",f"on {len(bot.guilds)} servers | ++help", "Invite using ++invite","Gotta Know ’Em All!","bit.ly/pokesupport"]
  while not bot.is_closed():
    status = random.choice(statuses)
    await bot.change_presence(activity=discord.Game(name=status))
    await asyncio.sleep(10)
bot.loop.create_task(ch_presence())

#HELP Commands
@commands.command(aliases=['help','h'])
async def halp(ctx):
  embed=discord.Embed(
    title='\nPokepedia Help',
    timestamp=datetime.datetime.utcnow(),
    color=0xff00ff
  )
  embed.add_field(name='Prefix',
  value='++',inline=False)
  embed.add_field(name='Commands',
  value='`bug` , `dark` , `dragon` , `electric` , `fairy` , `fighting` , `fire` , `flying` , `ghost` , `grass` , `ground` , `ice` , `normal` , `poison` , `psychic` , `rock` , `steel` , `water` \n')
  embed.add_field(name='++all',value='`Invokes all 18 commands listed above`\n',inline=False)
  embed.add_field(name='++search / ++s',value='`Search Pokemon by number eg : ++s 1`\n',inline=False)
  embed.add_field(name='++name',value='`Search Pokemon images by name try : ++name pikachu`\n',inline=False)
  embed.add_field(name='For giff lovers',value='`Try ++giff`\n',inline=False)
  embed.add_field(name='Know a random Pokemon Fact',value='`Use ++f or ++fact`',inline=False)
  embed.add_field(name='Play TicTacToe(++ttt)',value='`Play tictactoe by using command `\n`++ttt @mentionPlayer1 @mentionPlayer2`\n',inline=False)
  embed.add_field(name='Play Rock Paper Scissor(++rps)',value='`Try ++rps rock`\n',inline=False)
  embed.add_field(name='Play Magic 8 ball',value='`Try ++8ball <question>`\n',inline=False)
  embed.add_field(name='Useful Links',value='[Support Server](https://discord.gg/pbRtbJX5Sf) | [GitHub](https://github.com/lucifer00911/Pokepedia) | [Invite](https://discord.com/oauth2/authorize?client_id=804665852221325342&permissions=379968&scope=bot) | [Vote !](https://top.gg/bot/804665852221325342/vote)',inline=False)
  embed.set_thumbnail(url="https://i.pinimg.com/originals/ce/cc/91/cecc913aee77c99b18d2043dbbd8bd72.gif")
  embed.set_footer(text='\u200b')
  await ctx.send(embed=embed)

bot.add_command(halp)
#INVITE commands
@commands.command()
async def invite(ctx):
  embed=discord.Embed(title='Pokepedia',description='\n**Invite Link :** [Invite](https://discord.com/api/oauth2/authorize?client_id=804665852221325342&permissions=379968&scope=bot)\n**Support Server :** [Support](https://discord.gg/pbRtbJX5Sf)',
  color=0x00ffff)
  embed.set_thumbnail(url='https://media.tenor.com/images/27215c1c6dbaca5d396184e5f8f7a73f/tenor.gif')
  await ctx.send(embed=embed)
bot.add_command(invite)



#-------------------------------------------------------------------------------PING COMMAND-------------------------------------------------------------------------------------
@commands.command()
async def ping(ctx):
  embed=discord.Embed(title='Pokepedia',timestamp=datetime.datetime.utcnow(),description=f'Ping : `{round(bot.latency * 1000)}ms`\nPlaying on `{len(bot.guilds)}` servers',color=0xF00091 )
  embed.set_footer(text='\u200b')
  await ctx.send(embed=embed)
bot.add_command(ping)
#------------------------------------------------------------------------------NORMAL TYPE---------------------------------------------------------------------------------------
@commands.command()
async def normal(ctx):
    embed=discord.Embed(
      description='[Normal Type](https://bulbapedia.bulbagarden.net/wiki/Normal_type)\n\n**Weak Against** : Rock, Ghost, Steel \n**Resistant To**: Ghost \n**Vulnerable To**: Fighting',
      color=0x85886F
    )
    embed.set_thumbnail(url="https://i.imgur.com/PdDUKBT.gif")
    await ctx.send(embed=embed)
bot.add_command(normal)
#-----------------------------------------------------------------------------FIGHTING TYPE--------------------------------------------------------------------------------------
@commands.command(aliases=['fight'])
async def fighting(ctx):
    embed=discord.Embed(
      description='[Fighting Type](https://bulbapedia.bulbagarden.net/wiki/Fighting_type)\n\n**Strong Against**: Normal, Rock, Steel, Ice, Dark\n**Weak Against** : Flying, Poison, Psychic, Bug, Ghost, Fairy \n**Resistant To**: Rock, Bug, Dark\n**Vulnerable To**:Flying, Psychic, Fairy',
      color=0xB30000 
    )
    embed.set_thumbnail(url="https://i.imgur.com/d7yQufV.gif")
    await ctx.send(embed=embed)
bot.add_command(fighting)
#------------------------------------------------------------------------------FLYING TYPE---------------------------------------------------------------------------------------
@commands.command()
async def flying(ctx):
  embed=discord.Embed(
      description='[Flying Type](https://bulbapedia.bulbagarden.net/wiki/Flying_type)\n\n**Strong Against**: Fighting, Bug, Grass\n**Weak Against** : Rock, Steel, Electric \n**Resistant To**: Fighting, Ground, Bug, Grass\n**Vulnerable To**:Rock, Electric, Ice',
      color=0x30EED5
    )
  embed.set_thumbnail(url="https://i.imgur.com/MWjhVyj.gif")
  await ctx.send(embed=embed)
bot.add_command(flying)
#------------------------------------------------------------------------------POISON TYPE---------------------------------------------------------------------------------------
@commands.command()
async def poison(ctx):
    embed=discord.Embed(
      description='[Poison Type](https://bulbapedia.bulbagarden.net/wiki/Poison_type)\n\n**Strong Against**: Grass, Fairy\n**Weak Against** : Poison, Ground, Rock, Ghost, Steel\n**Resistant To**:Fighting, Poison, Grass, Fairy\n**Vulnerable To**:Ground, Psychic',
      color=0xE0AC25
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805749181485678632/848488.gif")
    await ctx.send(embed=embed)
bot.add_command(poison)
#-----------------------------------------------------------------------------GROUND TYPE---------------------------------------------------------------------------------------
@commands.command()
async def ground(ctx):
    embed=discord.Embed(
      description='[Ground Type](https://bulbapedia.bulbagarden.net/wiki/Ground_type)\n\n**Strong Against**:Poison, Rock, Steel, Fire, Electric\n**Weak Against** : Flying, Bug, Grass \n**Resistant To**: Poison, Rock, Electric\n**Vulnerable To**:Water, Grass, Ice',
      color=0x724805
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805116049430675486/1111.gif")
    await ctx.send(embed=embed)
bot.add_command(ground)
#-------------------------------------------------------------------------------ROCK TYPE---------------------------------------------------------------------------------------
@commands.command()
async def rock(ctx):
    embed=discord.Embed(
      description='[Rock Type](https://bulbapedia.bulbagarden.net/wiki/Rock_type)\n\n**Strong Against**: Flying, Bug, Fire, Ice\n**Weak Against** : Fighting, Ground, Steel\n**Resistant To**: Normal, Flying, Poison, Fire\n**Vulnerable To**:Fighting, Ground, Steel, Water, Grass',
      color=0x7B7262 
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805116673707081759/11112.gif")
    await ctx.send(embed=embed)
bot.add_command(rock)
#--------------------------------------------------------------------------------BUG TYPE---------------------------------------------------------------------------------------
@commands.command()
async def bug(ctx):
    embed=discord.Embed(
      description='[Bug Type](https://bulbapedia.bulbagarden.net/wiki/Bug_type)\n\n**Strong Against**: Grass, Psychic, Dark\n**Weak Against** : Fighting, Flying, Poison, Ghost, Steel, Fire, Fairy\n**Resistant To**: Fighting, Ground, Grass\n**Vulnerable To**:Fighting, Ground, Grass',
      color=0x89D306
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805748308839891004/984889.gif")
    await ctx.send(embed=embed)
bot.add_command(bug)
#-------------------------------------------------------------------------------GHOST TYPE---------------------------------------------------------------------------------------
@commands.command()
async def ghost(ctx):
    embed=discord.Embed(
      description='[Ghost Type](https://bulbapedia.bulbagarden.net/wiki/Ghost_type)\n\n**Strong Against**: Ghost, Psychic\n**Weak Against** : Normal, Dark\n**Resistant To**:Normal, Fighting, Poison, Bug\n**Vulnerable To**:Ghost, Dark',
      color=0x050621
    )
    embed.set_thumbnail(url="https://i.imgur.com/PcFJp4L.gif")
    await ctx.send(embed=embed)
bot.add_command(ghost)
#-------------------------------------------------------------------------------STEEL TYPE---------------------------------------------------------------------------------------
@commands.command()
async def steel(ctx):
    embed=discord.Embed(
      description='[Steel Type](https://bulbapedia.bulbagarden.net/wiki/Steel_type)\n\n**Strong Against**:Rock, Ice, Fairy\n**Weak Against** : Steel, Fire, Water, Electric\n**Resistant To**: Normal, Flying, Poison, Rock, Bug, Steel, Grass, Psychic, Ice, Dragon, Fairy\n**Vulnerable To**:Fighting, Ground, Fire',
      color=0xCCBFA2 
    )
    embed.set_thumbnail(url="https://media.giphy.com/media/ZBexIRI4raU0YIruAW/giphy.gif")
    await ctx.send(embed=embed)
bot.add_command(steel)
#--------------------------------------------------------------------------------FIRE TYPE---------------------------------------------------------------------------------------
@commands.command()
async def fire(ctx):
    embed=discord.Embed(
      description='[Fire Type](https://bulbapedia.bulbagarden.net/wiki/Fire_type)\n\n**Strong Against**:Bug, Steel, Grass, Ice\n**Weak Against** : Rock, Fire, Water, Dragon\n**Resistant To**: Bug, Steel, Fire, Grass, Ice\n**Vulnerable To**:Ground, Rock, Water',
      color=0xFBF600 
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805126023417954324/154848.gif")
    await ctx.send(embed=embed)
bot.add_command(fire)
#-------------------------------------------------------------------------------WATER TYPE---------------------------------------------------------------------------------------
@commands.command()
async def water(ctx):
    embed=discord.Embed(
      description='[Water Type](https://bulbapedia.bulbagarden.net/wiki/Water_type)\n\n**Strong Against**: Ground, Rock, Fire\n**Weak Against** : Water, Grass, Dragon\n**Resistant To**:Steel, Fire, Water, Ice\n**Vulnerable To**:Grass, Electric',
      color=0x02AFF3 
    )
    embed.set_thumbnail(url="https://i.imgur.com/us6XOaF.gif")
    await ctx.send(embed=embed)
bot.add_command(water)
#-------------------------------------------------------------------------------GRASS TYPE---------------------------------------------------------------------------------------
@commands.command()
async def grass(ctx):
    embed=discord.Embed(
      description='[Grass Type](https://bulbapedia.bulbagarden.net/wiki/Grass_type)\n\n**Strong Against**: Ground, Rock, Water\n**Weak Against** : Flying, Poison, Bug, Steel, Fire, Grass, Dragon\n**Resistant To**: Ground, Water, Grass, Electric\n**Vulnerable To**:Flying, Poison, Bug, Fire, Ice',
      color=0x13DE05 
    )
    embed.set_thumbnail(url="https://i.gifer.com/4o45.gif")
    await ctx.send(embed=embed)
bot.add_command(grass)
#----------------------------------------------------------------------------ELECTRIC TYPE---------------------------------------------------------------------------------------
@commands.command()
async def electric(ctx):
    embed=discord.Embed(
      description='[Electric Type](https://bulbapedia.bulbagarden.net/wiki/Electric_type)\n\n**Strong Against**: Flying, Water\n**Weak Against** : Ground, Grass, Electric, Dragon\n**Resistant To**:Flying, Steel, Electric\n**Vulnerable To**:Ground',
      color=0xEBE302
    )
    embed.set_thumbnail(url="https://img1.picmix.com/output/stamp/normal/4/8/0/4/1604084_93e2e.gif")
    await ctx.send(embed=embed)
bot.add_command(electric)
#---------------------------------------------------------------------------PSYCHIC TYPE-----------------------------------------------------------------------------------------
@commands.command()
async def psychic(ctx):
    embed=discord.Embed(
      description='[Psychic Type](https://bulbapedia.bulbagarden.net/wiki/Psychic_type)\n\n**Strong Against**: Fighting, Poison\n**Weak Against** : Steel, Psychic, Dark\n**Resistant To**: Fighting, Psychic\n**Vulnerable To**:Bug, Ghost, Dark',
      color=0xF80AF0 
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805113889418510346/805119836689530893/65564.gif")
    await ctx.send(embed=embed)
bot.add_command(psychic)
#-----------------------------------------------------------------------------ICE TYPE------------------------------------------------------------------------------------------
@commands.command()
async def ice(ctx):
    embed=discord.Embed(
      description='[Ice Type](https://bulbapedia.bulbagarden.net/wiki/Ice_type)\n\n**Strong Against**: Flying, Ground, Grass, Dragon\n**Weak Against** : Steel, Fire, Water, Ice\n**Resistant To**:Ice\n**Vulnerable To**:Fighting, Rock, Steel, Fire',
      color=0x3FADE2 
    )
    embed.set_thumbnail(url="https://i.imgur.com/PrXXz6e.gif")
    await ctx.send(embed=embed)
bot.add_command(ice)
#-----------------------------------------------------------------------------DRAGON TYPE----------------------------------------------------------------------------------------
@commands.command()
async def dragon(ctx):
    embed=discord.Embed(
      description='[Dragon Type](https://bulbapedia.bulbagarden.net/wiki/Dragon_type)\n\n**Strong Against**:Dragon\n**Weak Against** : Steel, Fairy\n**Resistant To**: Fire, Water, Grass, Electric\n**Vulnerable To**:Ice, Dragon, Fairy',
      color=0xDD350C 
    )
    embed.set_thumbnail(url="https://i.imgur.com/NK1VH5b.gif")
    await ctx.send(embed=embed)
bot.add_command(dragon)
#------------------------------------------------------------------------------FAIRY TYPE----------------------------------------------------------------------------------------
@commands.command()
async def fairy(ctx):
    embed=discord.Embed(
      description='[Fairy Type](https://bulbapedia.bulbagarden.net/wiki/Fairy_type)\n\n**Strong Against**: Fighting, Dragon, Dark\n**Weak Against** : Poison, Steel, Fire\n**Resistant To**: Fighting, Bug, Dragon, Dark\n**Vulnerable To**:Poison, Steel',
      color=0xF02A72
    )
    embed.set_thumbnail(url="https://thumbs.gfycat.com/OddBiodegradableAmphiuma-max-1mb.gif")
    await ctx.send(embed=embed)
bot.add_command(fairy)
#-----------------------------------------------------------------------------DARK TYPE------------------------------------------------------------------------------------------
@commands.command()
async def dark(ctx):
    embed=discord.Embed(
      description='[Dark Type](https://bulbapedia.bulbagarden.net/wiki/Dark_type)\n\n**Strong Against**: Ghost, Psychic\n**Weak Against** :Fighting, Dark, Fairy\n**Resistant To**:Ghost, Psychic, Dark\n**Vulnerable To**:Fighting, Bug, Fairy',
      color=0x3C3335 
    )
    embed.set_thumbnail(url="https://i.imgur.com/FtfrpoZ.gif")
    await ctx.send(embed=embed)
bot.add_command(dark)
#----------------------------------------------------------------------SEARCH POKEMON BY NUMBER----------------------------------------------------------------------------------
@commands.command(aliases=['s'])
async def search(ctx,i=1):

  try:
    req = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + '{:03d}'.format(i) + '.png'
    embed=discord.Embed(title='{:03d}'.format(i),timestamp=datetime.datetime.utcnow(),color=0xff00ff)
    embed.set_image(url=req)
    embed.set_footer(text='\u200b')
    await ctx.send(embed=embed)
  except Exception as e:

    await ctx.send("Error Occured for Pokemon " + '{:04d}'.format(i))
    print(str(e))

bot.add_command(search)
#-------------------------------------------------------------------SEARCH POKEMON BY NAME---------------------------------------------------------------------------------------
@commands.command(aliases=['name'])
async def sName(ctx,*,name='Missing argument name of the Pokemon'):

  try:
    n=name.lower()
    req='https://img.pokemondb.net/artwork/large/'+n+'.jpg'
    embed=discord.Embed(title=n,timestamp=datetime.datetime.utcnow(),color=0xff00ff)
    embed.set_image(url=req)
    embed.set_footer(text='No Image ? Spell check and try again!')
    await ctx.send(embed=embed)
  except Exception as e:

    await ctx.send("```Missing argument name of the Pokemon```")
    print(str(e))

bot.add_command(sName)
#-------------------------------------------------------------------------CALL ALL AT ONCE---------------------------------------------------------------------------------------
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
  await ctx.send("```That's All !```")
bot.add_command(call_all)

#-------------------------------------------------------------------------------------GIFF COMMAND------------------------------------------------------------------------------
@commands.command()
async def giff(ctx):
  embed=discord.Embed(
    title='Gif Commands',
    description='Try these commands on your server for some cool gifs eg : ++g my',
    color=0xff00ff
  )
  embed.add_field(name='Giffs [use ++g then name of gifs listed below]',value='1.Hypnosis Pika(++g hp)\n2.Mystic Logo(++g my)\n3.Valor Logo(++g va)\n4.Instinct Logo(++g in)\n5.Dancing Dragonite(++g dance)',inline=False)
  embed.set_thumbnail(url='https://i.imgur.com/OqMXWbD.jpg')
  embed.set_footer(text='Join our support server for adding custom gifs')
  await ctx.author.send(embed=embed)
  await ctx.send("``Check DM``")
bot.add_command(giff)
#---------------------------------------------------------------------------------GIFFS COMMAND---------------------------------------------------------------------------------
@commands.command(aliases=['g'])
async def giffs(ctx,*,name='empty'):
    if name=='empty':
        await ctx.send('```Give following parameters : hp , my , va , in , dance | Try ++g hp```')
    if name=='hp':
        await ctx.send("https://emojis.slackmojis.com/emojis/images/1450458394/182/pikachu.gif?1450458394")
        await ctx.message.delete()
    if name=='my':
        await ctx.send("https://emojis.slackmojis.com/emojis/images/1469201975/673/mystic.gif?1469201975")
        await ctx.message.delete()
    if name=='dance':
        await ctx.send("https://emojis.slackmojis.com/emojis/images/1469223471/679/charmander_dancing.gif?1469223471")
        await ctx.message.delete()
    if name=='va':
        await ctx.send("https://emojis.slackmojis.com/emojis/images/1469202036/674/valor.gif?1469202036")
        await ctx.message.delete()
    if name=='in':
        await ctx.send("https://emojis.slackmojis.com/emojis/images/1469201940/672/instinct.gif?1469201940")
        await ctx.message.delete()
bot.add_command(giffs)

#---------------------------------------------------------------------------RANDOM FACT------------------------------------------------------------------------------------------
@commands.command(aliases=['f','fact'])
async def pokeFacts(ctx):
    responses = ['Bulbasaur is the first Pokemon in the Pokedex.',
                'Rhydon is the first Pokemon ever to be created.',
                'Pikachu is a Japanese onomatopoeia for squeaking and shimmering.',
                'There are over 800 Pokemon species today and the number continues to grow.',
                'Slowbro is the only Pokemon that can devolve.',
                'Pikachu is not the original mascot for the franchise. The original mascot prior to Pikachu was Clefairy.',
                'According to a legend, Ditto was the result of an experiment in an attempt to create a copy of Mew.',
                'You could originally battle Professor Oak in Pokemon Red/Blue.',
                'Many of Nintendo’s game consoles are featured in certain versions of the mainline Pokemon games.',
                'Ninetails is based on the Japanese mythological fox that breathes fire and shapeshifts.',
                'The Kanto region is based on a real region in Japan with the same name.',
                'Victini is the only Pokemon with a dex number of 000.',
                'Wailord is lighter than the average full-grown adult.',
                'Cosmoem is based on a protostar which explains why it is so heavy for its small size.',
                'The original 151 Pokemon only made 37 types of noises.',
                'Bulbasaur is the only unevolved dual-type starter Pokemon before Gen VIII.',
                'The Sword of Justice legendary trio is based on the three musketeers.',
                'Rotom’s forms are designed by several artists. ',
                'Blastoise has the highest base Special Defense among all fully evolved starters. ',
                'Ekans is snake spelled backward.',
                'https://i.imgur.com/QQbZoU7.jpg',
                'https://i.imgur.com/I8OEfwf.jpg',
                'https://i.imgur.com/ApGoshR.jpg',
                'https://i.imgur.com/PbbC4dI.jpg']
    await ctx.send(random.choice(responses))
bot.add_command(pokeFacts)

#-------------------------------------------------------------------------------TIC TAC TOE--------------------------------------------------------------------------------------
player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@commands.command(aliases=['ttt'])
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:

      global board
      board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
      turn = ""
      gameOver = False
      count = 0

      player1 = p1
      player2 = p2

        # print the board
      line = ""
      for x in range(len(board)):
        if x == 2 or x == 5 or x == 8:
          line += " " + board[x]
          await ctx.send(line)
          line = ""
        else:

          line += " " + board[x]

        # determine who goes first
      num = random.randint(1, 2)
      if num == 1:
        turn = player1
        await ctx.send("It is <@" + str(player1.id) + ">'s turn.\n```Use ++place to mark | To quit type ++quit```")
      elif num == 2:
        turn = player2
        await ctx.send("It is <@" + str(player2.id) + ">'s turn.\n```Use ++place to mark | To quit type ++quit```")
    else:
      await ctx.send("```A game is already in progress! Quit this one by typing ++quit```")
bot.add_command(tictactoe)
@commands.command()
async def place(ctx, pos: int):
  global turn
  global player1
  global player2
  global board
  global count
  global gameOver

  if not gameOver:
  
    mark = ""
    if turn == ctx.author:

      if turn == player1:

        mark = ":regional_indicator_x:"
      elif turn == player2:
        mark = ":o2:"
      if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
        board[pos - 1] = mark
        count += 1

                # print the board
        line = ""
        for x in range(len(board)):
          if x == 2 or x == 5 or x == 8:

            line += " " + board[x]
            await ctx.send(line)
            line = ""
          else:
            line += " " + board[x]

        checkWinner(winningConditions, mark)
        print(count)
        
        if gameOver == True:
          await ctx.send(mark + " wins!")
        elif count >= 9:
          gameOver = True
          await ctx.send("```It's a tie!```")

                # switch turns
        if turn == player1:
            turn = player2
        elif turn == player2:
            turn = player1
      else:
                await ctx.send("```Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.```")
    else:
      await ctx.send("`It is not your turn.`")
  else:
    await ctx.send("```Please start a new game using the ,tictactoe command.```")


def checkWinner(winningConditions, mark):

  global gameOver
  for condition in winningConditions:
    if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
      gameOver = True
bot.add_command(place)
@tictactoe.error
async def tictactoe_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("```Please mention 2 players for this command.```")
  elif isinstance(error, commands.BadArgument):
    await ctx.send("```Please make sure to mention/ping players (ie. <@Player>).```")

@place.error
async def place_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("```Please enter a position you would like to mark. | Eg : ++place 5```")
  elif isinstance(error, commands.BadArgument):
    await ctx.send("```Please make sure to enter an integer between 1 to 9.```")

@commands.command()
async def quit(ctx):
  global gameOver
  gameOver = True
  await ctx.send("```Game Over . Thanks for playing ! ```")
bot.add_command(quit)

#--------------------------------------------------------------------------------8 BALL------------------------------------------------------------------------------------------

@commands.command(aliases=['8ball'])
async def _8ball(ctx,question='empty'):
  if question == 'empty':
    await ctx.send("```Ask a question please | ++8ball <question>```")
    return
  
  coloor=[0xff00ff,0xFC6700,0xF9FC00,0x74FC00,0x00FC16,
            0x08E1B1,0x08BEE1,0x086CE1,0x0811E1,0xB609CD ,
            0xCD09A0,0xCD097D ,0xCD0936,0xF70000]
  responses = ['As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don’t count on it.',
                 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Outlook good.',
                 'Reply hazy, try again.',
                 'Signs point to yes.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Yes.',
                 'Yes – definitely.',
                 'You may rely on it.',
                 'Are you kidding',
                 'Hell No']
  embed=discord.Embed(
  timestamp=datetime.datetime.utcnow(),
  description=random.choice(responses),
  color=random.choice(coloor)
    )
  embed.set_footer(text='\u200b')
  await ctx.send(embed=embed)
bot.add_command(_8ball)

#--------------------------------------------------------------------------ROCK PAPER SCISSOR-----------------------------------------------------------------------------------
@commands.command(aliases=['rps'])
async def RockPaperScissor(ctx,userChoice='Nothing'): 
    userWeapon=userChoice.lower()
    if userWeapon!='rock' and userWeapon!='paper' and userWeapon!='scissor' and userWeapon!='nothing':
      await ctx.send("Either choose `rock` or `paper` or `scissor`")
      return
    weapons=['rock','paper','scissor']
    randomWeapon=random.choice(weapons)
    if userWeapon=='nothing':
      await ctx.send('Required argument `rock`,`paper`,or,`scissor` is missing.\nFor example try:`++rps rock`')
    elif userWeapon=='rock' and randomWeapon=='paper':
      embed=discord.Embed(
        timestamp=datetime.datetime.utcnow(),
        description='paper beats rock . I win !',
        color=0xff00ff
      )
      embed.set_footer(text='\u200b')
      await ctx.send(embed=embed)
    elif userWeapon=='paper' and randomWeapon=='scissor':
      embed=discord.Embed(
        timestamp=datetime.datetime.utcnow(),
        description='scissor beats paper . I win !',
        color=0xff00ff
      )
      embed.set_footer(text='\u200b')
      await ctx.send(embed=embed)
    elif userWeapon=='scissor' and randomWeapon=='rock':
      embed=discord.Embed(
        timestamp=datetime.datetime.utcnow(),
        description='rock beats scissor . I win !',
        color=0xff00ff
      )
      embed.set_footer(text='\u200b')
      await ctx.send(embed=embed)
    elif userWeapon==randomWeapon:
      embed=discord.Embed(
        timestamp=datetime.datetime.utcnow(),
        description='Its a tie since I choose '+userChoice+' too :)',
        color=0xff00ff
      )
      embed.set_footer(text='\u200b')
      await ctx.send(embed=embed)
    else:
      embed=discord.Embed(
        timestamp=datetime.datetime.utcnow(),
        description='You win !',
        color=0xff00ff,
      )
      embed.set_footer(text='\u200b')
      await ctx.send(embed=embed)
bot.add_command(RockPaperScissor)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
keep_alive()
bot.run(os.getenv('TOKEN'))
