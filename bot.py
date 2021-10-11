import asyncio

import discord
import valve.source.a2s

import config


client = discord.Client()





client.loop.create_task(update_player_count())
client.run(config.BOT_TOKEN)
