import asyncpg
from discord import channel
from discord.ext import tasks, commands
from IPython.core.display import clear_output
from prettytable import PrettyTable
from IPython.display import display
from pandas import json_normalize
from urllib import parse, request
from io import BytesIO
import pandas as pd
import threading
import requests
import datetime
import discord
import base64
import folium
import json
import time
import bs4
import re
import discord
from discord.ext import tasks


pt = PrettyTable()
vbot = commands.Bot(command_prefix='*', description="Datos vrios Chile informaciones")




@vbot.event #creacion de eventos
async def on_ready():
    print('. . . O N  L I N E . . . ')











@vbot.command()
async def mmm(contexto):
    embed=discord.Embed(title="Sismos", description="muestra sismos", color=0xda0000)
    embed.set_thumbnail(url="https://n9.cl/yqsvw")
    embed.fields
    embed.set_footer(text="aca")
    await contexto.send(embed)

    




@vbot.command()
async def sismos(contexto):
    cabezeras= []
    fuente_dat = ('http://www.sismologia.cl/ultimos_sismos.html')
    page = requests.get(fuente_dat)
    sopa = bs4.BeautifulSoup(page.text, 'lxml')
    tabla = sopa.find('table')

    for i in tabla.find_all('th'):
        title = i.text.strip()
        cabezeras.append(title)
    df = pd.DataFrame(columns = cabezeras )

    for filas in tabla.find_all('tr')[1:]:
        info = filas.find_all('td')
        filas_info = [td.text.strip() for td in info]
        length = len(df)
        df.loc[length] = filas_info
    sis = df.head(3)
    print(sis)
   
    embed=discord.Embed(title="Sismos", description="muestra sismos", color=0xda0000)
    embed.set_thumbnail(url="https://n9.cl/yqsvw")
    embed.fields(df)
    embed.set_footer(text="aca")
    await contexto.send(df.head(3))






@vbot.command()
async def cripto(contexto):
    embed=discord.Embed(title="Valor Criptos", description="Valor criptomonedas")
    embed.add_field(name="Bitcoin", value="precio bit", inline=False)
    hilo = threading.Thread(target=cripto, args=(10,))
    hilo.start()   # Iniciamos la ejecución del thread,
    await contexto.send(embed=embed)







@vbot.command()
async def sis(contexto):
    cabezeras= []
    fuente_dat = ('http://www.sismologia.cl/ultimos_sismos.html')
    page = requests.get(fuente_dat)
    sopa = bs4.BeautifulSoup(page.text, 'lxml')
    tabla = sopa.find('table')

    for i in tabla.find_all('th'):
        title = i.text.strip()
        cabezeras.append(title)
    df = pd.DataFrame(columns = cabezeras )
  

    for filas in tabla.find_all('tr')[1:]:
        info = filas.find_all('td')
        filas_info = [td.text.strip() for td in info]
        length = len(df)
        df.loc[length] = filas_info
    sis = df.head(3)

    print(sis)
    mag = ([["Magnitud"]])
    
    
    embed=discord.Embed(title="Sismos", description="muestra sismos", color=0xda0000)
    embed.add_field(name="DATOS", value=f"{(mag)}", inline=True)
    embed.set_thumbnail(url="https://n9.cl/yqsvw")
    embed.set_footer(text="aca")
    await contexto.send(embed=embed)
    df["Profundidad [Km]"]
 






@vbot.command()
async def farma(contexto):

    """ resp = requests.get('https://farmanet.minsal.cl/index.php/ws/getLocalesTurnos')
    txt = resp.json()
    df = pd.DataFrame(txt)
    farma = df.head(50)[["localidad_nombre", "local_nombre", "local_direccion"]]
    print(farma)
    embed=discord.Embed(title="Farmacias de Turno", description="texto", color=0x06ff10)
    embed.add_field(name="Farmacias", value=(df), inline=False) """


    resp = requests.get('https://farmanet.minsal.cl/index.php/ws/getLocalesTurnos')
    txt = resp.json()
    df = pd.DataFrame(txt)
    """ df.to_csv('farma.csv') """
    farma = df.head(70)[["localidad_nombre", "local_nombre", "local_direccion"]]
    sp = df.iloc[80, [5,6,8,11]] # representa [filas,columnas]
    print(sp)

    


@vbot.command()
async def dolar(contexto):
    url = 'https://www.prensadigital.cl/cual-es-el-valor-dolar-en-chile-para-hoy-30-de-noviembre.html'
    pagina = requests.get(url)
    sopa = bs4(pagina.content, 'html.parser')

    dolars = sopa.find_all('div', class_='vlr')
    print(dolars)
    dlr = list()

    ctd = 0 #inicializamos contador en 0

    for i in dolars: #iterar para obtener solo los textos 
        if ctd < 1: #si ctd en menos a 20 insrtruccion para guardar primeros 20 registros
            dlr.append(i.text) #agregar a la lista nombrelista.append
        else:
            break   
    ctd += 1
    #print(dlr, len(dlr))

    embed = discord.Embed(title=" V A L O R   D O L A R " , timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embed.add_field(name="Un dolar es igual a: ", value=f"{(dlr)}")
    #await contexto.send(dlr)
    await contexto.send(embed=embed)
    await contexto.send(embed=dlr)





@vbot.command()
async def status(contexto):
    embed = discord.Embed(title=f"{contexto.guild.name}", description="DATA SCIENCE AND FACTS BOT", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())


    embed.add_field(name="Primera vez en linea", value=f"{contexto.guild.created_at}")
    embed.add_field(name="Propietario", value=f"{contexto.guild.owner}")
    embed.add_field(name="Server Region", value=f"{contexto.guild.region}")
    embed.add_field(name="Server ID", value=f"{contexto.guild.id}")
    embed.set_thumbnail(url="https://n9.cl/frz34")
    await contexto.send(embed=embed)


@tasks.loop(seconds=10)
async def auto_send():
    channel = await vbot.fetch_channel('755941137369268274')
    await channel.send('texto de prueba')








class Mcstats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.channel = self.bot.get_channel(755941137369268274)
        self.message = await self.channel.fetch_message(1)
        self.task.start()
        
    
    @tasks.loop(minutes=1)
    async def task(self):
        #retrieving data and creating embed
        await self.message.edit(embed=your_embed) #editing message

    client = discord.Client()

    @tasks.loop(seconds = 10) # repeat after every 10 seconds
    async def myLoop():
        print("hola mundo")
    myLoop.start()















vbot.run('Nzg3ODgyNjkxODM1MzMwNjQx.X9ba7w.rHC_wfJlVsWLsCYjUZfSN8tB_Zg')

