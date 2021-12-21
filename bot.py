import discord

client = discord.Client()

@client.event
async def on_ready():
    print('เข้าสู่รบบ {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        await message.channel.send('Hello!')

client.run('TOKEN')
