import discord
import asyncio

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("%짱재"): 
        await message.channel.send("멍청이") 


client.run("ODE2ODMyODMwNjc5NDE2ODgw.YEAs2g.6lKRtOqsk6UMMWEfsTjZIwlNCc0")