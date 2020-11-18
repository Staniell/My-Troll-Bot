import discord
from discord.ext import commands
import random

print(discord.__version__)


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    game = discord.Game("Summertime Saga")
    await bot.change_presence(status=discord.Status.online, activity=game)

    existing_channels = []

    for server in bot.guilds:
        if server.name == 'Bot test':
            for channel in server.channels:
                existing_channels.append(channel.name)
            if "message-of-the-day" not in existing_channels:
                await server.create_text_channel("message of the day")
                print("Created one now!")
            break

    print(f"\n{bot.user} has logged in")

    '''@tasks.loop(hours=24)
    async def my_loop():
        pass


    my_loop.start()'''

@bot.command(name="rps") #Rock Paper Scissors
async def rps(ctx):
    botChoice = ["Scissors","Paper","Rock"]
    await ctx.channel.send("Rock, Paper, Scissors")

    msg = await bot.wait_for('message',check=lambda msg: msg.content == "Paper" or msg.content == "Rock" or msg.content == "Scissors")

    if random.choice(botChoice) == "Scissors" and msg.content == "Rock":
        await ctx.channel.send(f"My choice = Scissors!\nYours = Rock\nYou win {msg.author.name}.")
    elif random.choice(botChoice) == "Scissors" and msg.content == "Paper":
        await ctx.channel.send(f"My choice = Scissors!\nYours = Paper\nYou lose {msg.author.name}.")
    elif random.choice(botChoice) == "Scissors" and msg.content == "Scissors":
        await ctx.channel.send(f"My choice = Scissors!\nYours = Scissors\nDRAW")

    elif random.choice(botChoice) == "Paper" and msg.content == "Rock":
        await ctx.channel.send(f"It's Paper! You lose {msg.author.name}")
    elif random.choice(botChoice) == "Paper" and msg.content == "Paper":
        await ctx.channel.send(f"It's Paper! DRAW")
    elif random.choice(botChoice) == "Paper" and msg.content == "Scissors":
        await ctx.channel.send(f"It's Paper! You win {msg.author.name}")

    elif random.choice(botChoice) == "Rock" and msg.content == "Rock":
        await ctx.channel.send(f"It's Rock! DRAW")
    elif random.choice(botChoice) == "Rock" and msg.content == "Paper":
        await ctx.channel.send(f"It's Rock! You win {msg.author.name}")
    elif random.choice(botChoice) == "Rock" and msg.content == "Scissors":
        await ctx.channel.send(f"It's Rock! You lose {msg.author.name}")


@bot.command(name="dmall") # Direct Message all membeers
async def dmAll(ctx):
    if ctx.message.author.id == 268714614215278602:
        userx = []
        for member in ctx.guild.members:
            if not member.bot:
                print(member.name)
                user = bot.get_user(member.id)
                userx.append(user)
        try:
            for i in range(10):  # Message one by one sequentially
                for j in range(len(userx)):
                    await userx[j].send(ctx.message.content[6:])
        except:
            print("Blocked or a bot")


@bot.command(name="msg")  # Send a message to channel :)
async def add(ctx, *args):
    for channel in ctx.guild.channels:
        if channel.name == "general":
            await channel.send(f'{" ".join(args)}')


@bot.command(name="dm")  # Private message
async def dm(ctx, *args):
    user = bot.get_user(727781198188773406)
    await user.send(f'{" ".join(args)}')


@bot.command(name="p")  # p for trolling as rythm
async def p(ctx):
    diss = ["Play it on youtube, fucker", "ayoko nga", "bahala ka dyan", "SorrY, Server is CurrentlY doWn"]
    await ctx.send(f"{random.choice(diss)} {ctx.message.author.mention}")


@bot.command(name="summon")  # troll command
async def p(ctx):
    await ctx.send(f"Fuck off {ctx.message.author.mention}! Im sleeping, Bitch!")


@bot.command(name="clear")  # Clear the hidden messages
async def clear(ctx):
    bot.my_count = []


bot.my_count = []


@bot.command(name="show")  # Show hidden messages
async def show(ctx):
    for i in bot.my_count:
        await ctx.send(i)


@bot.command(name="hide")  # Hide message
async def hide(ctx):
    bot.my_count.append(f'{ctx.message.author.name}: {ctx.message.content[6:]}')
    await ctx.message.delete()


@bot.event
async def on_message_delete(message):  # When someone deletes a message except me :)
    if message.author.id != 268714614215278602:
        await message.channel.send(f"Why did u delete '{message.content}'? {message.author.mention}")
    '''
    embedx = discord.Embed(title = "Deleted Message", description = message.content, color=0x00ff00)
    embedx.add_field(name=f"So, why did u delete it? {message.author}",value="Hmmm.....",inline=False)
    await message.channel.send(embed=embedx)
    '''


@bot.event
async def on_message(message):
    if not message.author.bot:
        try:
            words = {"ligma": "ligma dick", "what": "what's ligma?",
                     "luck": "everything's unfair",
                     "lost": 'good for u',
                     "mom": "I had her last night",
                     "sigh": "??", "hell": "That's where I live",
                     "idiot": "stfu",
                     "fuck": "fuck you too",
                     "shit": "shithead",
                     "please": "no",
                     "gay": "no u",
                     "who": "ur mom"}

            sentences = {"i give up": "good for u",
                         "whats the date today?": "Idk",
                         "fav president?": "donald trump",
                         "fav food?": "bat",
                         'fav place?': 'ur moms ass',
                         'where u from?':"wuhan",
                         "print hello world": 'error 404'}

            messagecheck = message.content.split()

            for messages in messagecheck:
                if messages.lower() in words:
                    await message.channel.send(f'{words[messages]} {message.author.mention}')
                    print(message.author)
                    return

            for i in sentences:
                if i == message.content.lower():
                    await message.channel.send(f'{sentences[i]} {message.author.mention}')

        except:
            print("Error has occured")
            pass

    await bot.process_commands(message)

bot.run(TOKEN)
