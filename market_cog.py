# import discord
from discord.ext import commands
from warframe_market import WarframeMarket


class Market(commands.Cog):
    def __init__(self, bot, api_key):
        self.bot = bot
        self.__market = WarframeMarket(api_key)

    @commands.group()
    async def market(self, ctx: commands.Context):
        ...

    @market.command()
    async def sell(self, ctx: commands.Context, *, arg: str):
        message = await ctx.send('Processing...')
        try:
            buy_orders = self.__market.search_buy_orders(arg)
        except ValueError as e:
            await message.edit(content=e)
            return
        if len(buy_orders) == 0:
            await ctx.send('No buy orders found.')
            return
        is_mod = False
        if 'mod_rank' in list(buy_orders[0].keys()):
            is_mod = True
        clean_orders = []
        if is_mod:
            for order in buy_orders:
                clean_orders.append([order['platinum'],
                                    order['quantity'],
                                    order['mod_rank'],
                                    order['user']['ingame_name'],
                                    order['user']['status']])
            response = '```Price  Quantity Rank  Status   User\n'
            for order in clean_orders:
                response += f'{order[0]:<7}{order[1]:<9}{order[2]:<6}{order[4]:<9}{order[3]}\n'
            response += '```'
        else:
            for order in buy_orders:
                clean_orders.append([order['platinum'],
                                    order['quantity'],
                                    order['user']['ingame_name'],
                                    order['user']['status']])
            response = '```Price  Quantity Status   User\n'
            for order in clean_orders:
                response += f'{order[0]:<7}{order[1]:<9}{order[3]:<9}{order[2]}\n'
            response += '```'
        await message.edit(content=response)
