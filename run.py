import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print("ready")
    await client.change_presence(status=discord.Status.online)

@client.event
async def on_message(message):
    if message.content.startswith("%짱재"): 
        await message.channel.send("멍청이") 


client.run("ODE2ODMyODMwNjc5NDE2ODgw.YEAs2g.6lKRtOqsk6UMMWEfsTjZIwlNCc0")