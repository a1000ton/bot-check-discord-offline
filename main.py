# Mandar mensagem todo dia 6 da manha (BR) "Checando vagabundos on-line : )"
# Vai pingar todos online com a mensagem: "Vagabundo ${nome} esta online kkkkkk vai dormir"
# "Parece que {nome} tá sem trabalhar hein kkkkkkk"
# "Hmmm... estranho... achei que ${nome} dormia cedo, parece que é vagabundo!!"


# https://discord.com/api/oauth2/authorize?client_id=993631057230430360&permissions=2048&scope=bot


import os
import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents, chunk_guilds_at_startup=False)

bot_key = os.environ['bot_key']

@client.event
async def on_ready():
  print('Hora de checar vagabundos rs {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('vagabot$check'):
    await message.channel.send('Checando vagabundos on-line : )')
    
    currentUsersOnline = await check_online_members()

    await message.channel.send('Lista dos vagabundos on-line: ')
    
    membersOnlineMention = ", ".join(currentUsersOnline)
    
    await message.channel.send(membersOnlineMention)
    await message.channel.send('Vão dormir porra kkkkkk')

async def check_online_members():
  currentUsersOnline = []
  
  for guild in client.guilds:
    for member in guild.members:
      if not member.bot:
        currentUsersOnline.append(member.mention)
      
  return currentUsersOnline
      

client.run(bot_key)
