
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

@vbot.command() #crear comando bpt
async def maps(contexto): #devolevr valor simple 
    m = folium.Map(location=[-21.13, -68.61])
    await contexto.send(m) #valor a agrega