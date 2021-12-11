

from IPython.core.display import clear_output
from prettytable import PrettyTable
from IPython.display import display
from pandas import json_normalize
from urllib import parse, request
from discord.ext import commands
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


vbot = commands.Bot(command_prefix='*', description="Datos vrios Chile informaciones")

@vbot.command()
async def cripto(contexto):
    embed=discord.Embed(title="Valor Criptos", description="Valor criptomonedas")
    embed.add_field(name="Bitcoin", value="precio bit", inline=False)
    hilo = threading.Thread(target=cripto, args=(10,))
    hilo.start()   # Iniciamos la ejecución del thread,
    await contexto.send(embed=embed)
