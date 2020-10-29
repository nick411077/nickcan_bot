import os
import sys


__all__ = ["TOKEN"]

TOKEN = os.environ.get("DISCORD_TOKEN")
if not TOKEN:
    print("Specify discord bot token as DISCORD_TOKEN in environment variables.")
    sys.exit(1)