import datetime
from discord.ext import tasks # discord extensions
import discord
import asyncio

class TutorialBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # create the background task and run it in the background
        self.my_background_task.start()
        #self.my_background_task2.start()

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return
        print('Message from {0.author}: {0.content} on channel {0.channel.name} with id {0.channel.id}'.format(message))
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!') # same as message.reply('Hello!')

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        print(payload.user_id)
        username = payload.member.name
        await self.get_channel(980597235916079136).send(username + " added reaction " + str(payload.emoji) + " to message id " + str(payload.message_id))
    #async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
    #    print(payload.user_id)
    #    guild = self.get_guild(payload.guild_id)
    #    member = guild.get_member(payload.user_id)
    #    if member is None:
    #        return
    #    username = member.name
    #    await self.system_channel.send(username + " removed reaction " + str(payload.emoji) + " to message id " + str(payload.message_id))

    async def on_member_join(self, member):
        guild = member.guild

        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
    
    async def on_message_delete(self, message):
        fmt = '{0.author} has deleted the message: {0.content}'
        await message.channel.send(fmt.format(message))


    # Tasks

    @tasks.loop(seconds=60) # task runs every 60 seconds
    async def my_background_task(self):
        channel = self.get_channel(980597235916079136) # channel ID goes here
        await channel.send(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready() # wait until the bot logs in

    #@tasks.loop(seconds=30) # task runs every 30 seconds
    #async def my_background_task2(self):
    #    channel = self.get_channel(980597235916079136) # channel ID goes here
    #    await channel.send(">" +  datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    #@my_background_task2.before_loop
    #async def before_my_task(self):
    #    await self.wait_until_ready() # wait until the bot logs in

intents = discord.Intents.default()
intents.members = True

client = TutorialBot()
client.run('')

