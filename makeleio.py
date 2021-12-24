#!/home/thatguy/makeleio-bot/bin/python3
from bs4 import BeautifulSoup
from requests import  get
import discord
from discord.ext import tasks
import os 
from dotenv import load_dotenv

from getDay import findDay
load_dotenv()
TOKEN = os.getenv('TOKEN')

BASE_URL="https://www.naftemporiki.gr"
URL ="https://www.naftemporiki.gr/frontpages/latest/imerisies-politikes/makeleio/full"

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
  
@tasks.loop(hours=12)
async def sendMakeleio():

    await client.wait_until_ready()
    channel = client.get_channel(int(814447007573082134))
    day = findDay()
    if day=="Saturday" or day=="Sunday":
        return 
    img_url = getImage()
    await channel.send(  img_url)

def getImage():
    res = get(URL)
    soup = BeautifulSoup(res.text,"html.parser")
    imgs = soup.find_all("img",{"id":"fullImg"})
    return BASE_URL+imgs[0]['src']
client.run(TOKEN)
