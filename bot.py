import discord

W = 0
L = 0
G = 1

print(discord.__version__)

token = open("token.txt", "r").read() #salva token em txt

client = discord.Client() #starta o cliente

#msg de login console
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#comandos do bot
@client.event
async def on_message(message):

    global W
    global L
    global G

    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if "bot_teste" == message.content.lower(): #teste rapido
        await message.channel.send("coe rapaziada")

    if "vai fica tudo preto" == message.content.lower():
        await message.channel.send("cala boca")

    if "win++" == message.content.lower():
        W = W + 1
        await message.channel.send(f"W: {W}")

    if "lose++" == message.content.lower():
        L = L + 1
        await message.channel.send(f"L: {L}")

    if "w/l" == message.content.lower():
        await message.channel.send(f"W: {W}\nL: {L}")

    if "w/l_reset" == message.content.lower():
        W = 0
        L = 0
        await message.channel.send(f"W: {W}\nL: {L}")

    if "gostoso++" == message.content.lower():
        G = G + 1
        await message.channel.send(f"tobilo esta {G}x mais gostoso!")

    if "gostoso--" == message.content.lower():
        G = G - 1
        await message.channel.send(f"tobilo esta {G}x mais gostoso!")

    if "+" == message.content[0].lower(): #visao geral champs lolzin
        string = message.content.lower()
        string2 = string.split()
        role = string2[1]
        champ = string2[0]
        champ = champ[1:]
        await message.channel.send("https://br.op.gg/champion/" + champ + "/statistics/" + role)

    if "help_bot" == message.content.lower():
        await message.channel.send("BOT DUS GURI!!! \nDigite o nome do champ e da role certinho \nno formato +champ role \nPara me mandar de base use bot_off")

    if "bot_off" == message.content.lower(): #desligar bot
        await message.channel.send("GG WP")
        await client.close()

#    if message.author.name == "Ruff Ghanor":
#        await message.channel.send("CALA BOCA PEDRO!")

client.run(token)
