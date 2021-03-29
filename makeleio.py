from dis import disco
from bs4 import BeautifulSoup
from discord import channel
from requests import  get
import discord
from discord.ext import tasks
import os 
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

BASE_URL="https://www.naftemporiki.gr"
URL = f"https://www.naftemporiki.gr/frontpages/latest/imerisies-politikes/makeleio/full"
res = get(URL)

client = discord.Client()

#Bot is ready event
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    sendMakeleio.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
  
@tasks.loop(hours=24)
async def sendMakeleio():
    await client.wait_until_ready()
    channel = client.get_channel(int(814447007573082134))
    img_url = getImage()
    await channel.send(  img_url)

def getImage():
    soup = BeautifulSoup(res.text,"html.parser")
    imgs = soup.find_all("img",{"id":"fullImg"})
    return BASE_URL+imgs[0]['src']
client.run(TOKEN)