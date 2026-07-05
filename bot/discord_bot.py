#!/usr/bin/env python3
"""
L'ÉVEIL NOCTURNE — Discord Bot
Le mouvement qui refuse le gatekeeping dans l'éducation hacker.

Features:
  - Welcome message branded (L'Éveil Nocturne)
  - Serment signing (members add :i_serment: reaction)
  - Command: /serment — show the 4 commitments
  - Command: /arsenal — list the 6 tools
  - Command: /countdown — time to J-0
  - Command: /sigil — show the brand
  - Auto-react with sigil emoji to welcome

Usage:
  pip install discord.py
  export DISCORD_TOKEN="your_token"
  python3 bot.py
"""
import os
import sys
import json
import asyncio
from datetime import datetime, timezone

try:
    import discord
    from discord.ext import commands
except ImportError:
    print("Need discord.py: pip install discord.py")
    sys.exit(1)

# ════════════════════════════════════════════════════════
# BRAND
# ════════════════════════════════════════════════════════
BRAND = {
    "name": "L'ÉVEIL NOCTURNE",
    "tagline": "There is no lock.",
    "trinity": [
        "There is no lock.",
        "Du silence naît la lumière.",
        "Là où l'ignorance dort, nous allumons."
    ],
    "principles": [
        "Curiosité comme droit",
        "Outils, pas produits",
        "Méthode avant résultat",
        "Zéro hiérarchie"
    ],
    "serment": [
        ("Je ne cache pas.",
         "Tout ce que je publie est source ouverte. La connaissance qui m'a été donnée, je la donne."),
        ("Je ne détruis pas.",
         "Mon pouvoir est de comprendre, pas d'effacer. Je construis avant de critiquer."),
        ("Je ne mens pas.",
         "Je dis ce que je sais. Je dis ce que je ne sais pas. Toujours."),
        ("Je ne gates pas.",
         "Le savoir que je possède, je le partage. Sans conditions. Sans files d'attente.")
    ],
    "arsenal": [
        ("ghosteye", "Reconnaissance HLS / ONVIF / RTSP", "https://github.com/187Ghost101/ghosteye"),
        ("biobypass", "Auth bypass research", "https://github.com/187Ghost101/biobypass"),
        ("ycc365-ghost", "IoT pivot toolkit", "https://github.com/187Ghost101/ycc365-ghost"),
        ("phishcloner-ultimate", "Phishing awareness / Red Team", "https://github.com/187Ghost101/phishcloner-ultimate"),
        ("quebec-ultimate", "OSINT framework", "https://github.com/187Ghost101/quebec-ultimate"),
        ("ghost1o1-design", "Design system du mouvement", "https://github.com/187Ghost101/ghost1o1-design")
    ],
    "colors": {
        "gold": 0xf4a261,
        "accent": 0xe63946,
        "cyan": 0x00d4ff,
        "bg": 0x0a0a0f
    },
    "drop_date": datetime(2026, 7, 12, 22, 0, 0, tzinfo=timezone.utc)
}

# ════════════════════════════════════════════════════════
# BOT
# ════════════════════════════════════════════════════════
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents, help_command=None)

# ════════════════════════════════════════════════════════
# EVENTS
# ════════════════════════════════════════════════════════
@bot.event
async def on_ready():
    print(f"""
╔═══════════════════════════════════════════╗
║  🔱 L'ÉVEIL NOCTURNE — Bot Ready          ║
╠═══════════════════════════════════════════╣
║  Logged in: {bot.user.name:<30}║
║  ID: {str(bot.user.id):<35}║
║  Guilds: {len(bot.guilds):<32}║
║  Members: {sum(g.member_count or 0 for g in bot.guilds):<31}║
╚═══════════════════════════════════════════╝
    """)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="le signal · 2026.07.12"
        ),
        status=discord.Status.online
    )

@bot.event
async def on_member_join(member):
    """Welcome new members with branded message"""
    channel = None
    for ch in member.guild.text_channels:
        if "welcome" in ch.name.lower() or "général" in ch.name.lower() or "general" in ch.name.lower():
            channel = ch
            break
    if not channel:
        channel = member.guild.system_channel
    if not channel:
        return

    embed = discord.Embed(
        title="🔱 L'ÉVEIL NOCTURNE",
        description=f"Bienvenue, **{member.mention}**.",
        color=BRAND["colors"]["gold"]
    )
    embed.add_field(
        name="// Le mouvement",
        value="6 outils open-source. 1 méthodologie. 0 paywall. ∞ divergence.",
        inline=False
    )
    embed.add_field(
        name="// Trinité",
        value="\n".join([f"*{t}*" for t in BRAND["trinity"]]),
        inline=False
    )
    embed.add_field(
        name="// Pour commencer",
        value="`/serment` — Lis nos 4 engagements\n"
              "`/arsenal` — Découvre les 6 outils\n"
              "`/countdown` — Temps avant le drop",
        inline=False
    )
    embed.set_footer(text="There is no lock. · L'Éveil Nocturne 2026")
    embed.set_thumbnail(url=member.avatar.url if member.avatar else None)

    await channel.send(embed=embed)

# ════════════════════════════════════════════════════════
# COMMANDS
# ════════════════════════════════════════════════════════
@bot.command(name='serment')
async def serment(ctx):
    """Show the 4 commitments of the movement"""
    embed = discord.Embed(
        title="🔱 LE SERMENT — L'Éveil Nocturne",
        description="*Quatre engagements. Non négociables.*",
        color=BRAND["colors"]["accent"]
    )
    for i, (title, body) in enumerate(BRAND["serment"], 1):
        embed.add_field(
            name=f"{['I','II','III','IV'][i-1]}. {title}",
            value=body,
            inline=False
        )
    embed.set_footer(text="Signer le serment → github.com/187Ghost101/eveil-nocturne")
    await ctx.send(embed=embed)

@bot.command(name='arsenal')
async def arsenal(ctx):
    """Show the 6 tools of the movement"""
    embed = discord.Embed(
        title="⚔ L'ARSENAL — 6 outils, 1 méthode",
        description="*Source ouverte. Zéro paywall. Pour toujours.*",
        color=BRAND["colors"]["cyan"]
    )
    for name, desc, url in BRAND["arsenal"]:
        embed.add_field(
            name=f"`{name}`",
            value=f"{desc}\n[→ GitHub]({url})",
            inline=True
        )
    embed.set_footer(text="github.com/187Ghost101")
    await ctx.send(embed=embed)

@bot.command(name='countdown')
async def countdown(ctx):
    """Time until J-0 (the drop)"""
    now = datetime.now(timezone.utc)
    diff = BRAND["drop_date"] - now
    if diff.total_seconds() <= 0:
        await ctx.send(embed=discord.Embed(
            title="🔱 LE SIGNAL EST LANCÉ",
            description="2026.07.12 — 22:00 UTC — Le drop est en cours.",
            color=BRAND["colors"]["accent"]
        ))
        return

    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    embed = discord.Embed(
        title="⏳ LE SIGNAL APPROCHE",
        description=f"**J-0** dans `{days}j {hours}h {minutes}m {seconds}s`",
        color=BRAND["colors"]["gold"]
    )
    embed.add_field(
        name="// Cible",
        value="`2026.07.12 · 22:00 UTC`",
        inline=False
    )
    embed.add_field(
        name="// Au programme",
        value="6 outils · 1 méthodologie · ∞ divergence",
        inline=False
    )
    embed.set_footer(text="L'Éveil Nocturne · 2026")
    await ctx.send(embed=embed)

@bot.command(name='sigil')
async def sigil(ctx):
    """Show the brand sigil + manifesto link"""
    embed = discord.Embed(
        title="☾ L'ÉVEIL NOCTURNE",
        description="```\n"
                    "        ☾\n"
                    "       ◉  ← œil ouvert\n"
                    "      ╳   ← 4 chemins divergents\n"
                    "         \n"
                    "  L'ÉVEIL NOCTURNE · 2026\n"
                    "```",
        color=BRAND["colors"]["gold"]
    )
    embed.add_field(
        name="// Trinité",
        value="\n".join([f"*{t}*" for t in BRAND["trinity"]]),
        inline=False
    )
    embed.set_footer(text="Forged in the dark · ghost1o1")
    await ctx.send(embed=embed)

@bot.command(name='manifesto')
async def manifesto(ctx):
    """Show the manifesto link"""
    embed = discord.Embed(
        title="📜 LE MANIFESTE",
        description=(
            "On ne vous apprend pas à *penser*.\n"
            "On vous apprend à *obéir* à ceux qui savent.\n\n"
            "**Refusez.**\n"
            "Comprenez. Construisez. Allumez."
        ),
        color=BRAND["colors"]["gold"]
    )
    embed.add_field(
        name="// Lire",
        value="[MANIFESTO.md](https://github.com/187Ghost101/eveil-nocturne/blob/main/MANIFESTO.md)",
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command(name='aide', aliases=['help', 'h'])
async def aide(ctx):
    """Show help"""
    embed = discord.Embed(
        title="🔱 L'ÉVEIL NOCTURNE — Commandes",
        color=BRAND["colors"]["gold"]
    )
    embed.add_field(name="/serment", value="Les 4 engagements du mouvement", inline=False)
    embed.add_field(name="/arsenal", value="Les 6 outils open-source", inline=False)
    embed.add_field(name="/countdown", value="Temps avant le drop J-0", inline=False)
    embed.add_field(name="/sigil", value="Le symbole du mouvement", inline=False)
    embed.add_field(name="/manifesto", value="Lire le manifeste", inline=False)
    embed.add_field(name="/aide", value="Cette aide", inline=False)
    embed.set_footer(text="There is no lock.")
    await ctx.send(embed=embed)

# ════════════════════════════════════════════════════════
# REACTION HANDLER — track serment signers
# ════════════════════════════════════════════════════════
@bot.event
async def on_raw_reaction_add(payload):
    """Track :i_serment: reactions"""
    if payload.member and payload.member.bot:
        return
    # Custom emoji name :i_serment: or unicode 🔱 or unicode ☾
    if str(payload.emoji) in ['🔱', '☾', '◉'] and payload.channel_id:
        channel = bot.get_channel(payload.channel_id)
        if not channel:
            return
        try:
            message = await channel.fetch_message(payload.message_id)
            if message.author == bot.user:
                # React to their reaction with thank you
                await message.add_reaction('🖤')
        except:
            pass

# ════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════
if __name__ == "__main__":
    TOKEN = os.environ.get("DISCORD_TOKEN")
    if not TOKEN:
        print("Set DISCORD_TOKEN env var")
        print("Get one: https://discord.com/developers/applications")
        print("Then: export DISCORD_TOKEN='your_token_here'")
        print("Finally: python3 bot.py")
        sys.exit(1)
    bot.run(TOKEN)
