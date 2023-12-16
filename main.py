import discord
from discord.ext import commands
from market_cog import Market

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('#'),
    intents=intents,
)


@bot.event
async def on_ready():
    print(f'Connected as {bot.user}!')
    game = discord.Activity(type=discord.ActivityType.watching, name='the Operator fight')
    await bot.change_presence(activity=game)
    with open('api_key.txt', 'r') as f:
        api_key = f.read()
    await bot.add_cog(Market(bot, api_key))


@bot.command()
@commands.is_owner()
async def shutdown(ctx: commands.Context):
    await ctx.send('Shutting down.')
    await bot.remove_cog('Market')
    await bot.close()


def main():
    made_file = False
    try:
        open('api_key.txt', 'x').close()
        print('Please put your Warframe Market API key in api_key.txt.')
        made_file = True
    except FileExistsError:
        ...
    try:
        open('bot_token.txt', 'x').close()
        print('Please put your Discord bot token in bot_token.txt.')
        made_file = True
    except FileExistsError:
        with open('bot_token.txt', 'r') as f:
            bot_token = f.read()
    if made_file:
        return
    try:
        bot.run(bot_token)
    except discord.errors.LoginFailure as login_error:
        print(login_error)


if __name__ == '__main__':
    main()
