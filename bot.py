import discord
from discord.ext import commands
import os

# Replace with your specific Discord User ID and Bot Token
TARGET_USER_ID = 299927073345110016  
BOT_TOKEN = os.environ.get('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.moderation = True  # Required to track ban/unban events

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("Monitoring ban events...")

@bot.event
async def on_member_ban(guild: discord.Guild, user: discord.User):
    # Check if the banned user matches the targeted user ID
    if user.id == TARGET_USER_ID:
        try:
            await guild.unban(user, reason="Automated joke-ban reversal.")
            print(f"Successfully unbanned {user.name} from {guild.name}.")
        except discord.Forbidden:
            print(f"Failed to unban {user.name}: Bot lacks 'Ban Members' permission.")
        except discord.HTTPException as e:
            print(f"HTTP Error while trying to unban: {e}")

bot.run(BOT_TOKEN)
