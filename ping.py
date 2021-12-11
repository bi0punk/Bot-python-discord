
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
async def ping(contexto):
    """ await contexto.send('Pong! {0}'.format(round(vbot.latency, 1))) """
    await contexto.send(f'My ping is {vbot.latency}!')
