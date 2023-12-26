# import discord
from discord.ext import commands
import warframe_market
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

    @market.command()
    async def list(self, ctx: commands.Context, *, arg: str):
        arg = arg.lower().strip()
        translation_table = {
            'steel meridian': 'steel meridian',
            'steel': 'steel meridian',
            'arbiters of hexis': 'arbiters of hexis',
            'arbiters': 'arbiters of hexis',
            'hexis': 'arbiters of hexis',
            'cephalon suda': 'cephalon suda',
            'suda': 'cephalon suda',
            'the perrin sequence': 'the perrin sequence',
            'perrin sequence': 'the perrin sequence',
            'perrin': 'the perrin sequence',
            'red veil': 'red veil',
            'veil': 'red veil',
            'new loka': 'new loka',
            'loka': 'new loka',
        }
        if arg not in list(translation_table.keys()):
            await ctx.send('Invalid group name.')
            return
        else:
            arg = translation_table[arg]
        message = await ctx.send('Processing...')
        augment_orders = dict()
        faction_augments = warframe_market.faction_augments[arg]
        num = 0
        for mod in faction_augments:
            await message.edit(content=f'Processing... ({num} of {len(faction_augments)})')
            try:
                mod_parts = mod.split()
                mod_parts.pop()
                mod_no_frame = ' '.join(mod_parts)
                buy_orders = self.__market.search_buy_orders(mod_no_frame)
            except ValueError as e:
                await message.edit(content=e)
                return
            augment_orders[mod] = []
            for order in buy_orders:
                augment_orders[mod].append([order['platinum'],
                                           order['quantity'],
                                           order['mod_rank'],
                                           order['user']['ingame_name'],
                                           order['user']['status']])
            num += 1

        def weighted_price(order):
            """
            Give a clean order a higher value depending on the buyer's status.

            :param order: The entry.
            :return: The adjusted price.
            """
            if order[4] == 'ingame':
                return order[0] + 20000
            elif order[4] == 'online':
                return order[0] + 10000
            else:
                return order[0]

        faction_augments.sort(key=lambda o: weighted_price(augment_orders[o][0]), reverse=True)
        # Compile and send THE response
        response = f'```Top mods from {arg.title()}:\n'
        for i in range(min(5, len(faction_augments))):
            response += '---------------------------------------\n'
            response += f'{faction_augments[i].title()}:\n'
            response += 'Price  Quantity Rank  Status   User\n'
            for j in range(min(3, len(augment_orders[faction_augments[i]]))):
                order = augment_orders[faction_augments[i]][j]
                response += f'{order[0]:<7}{order[1]:<9}{order[2]:<6}{order[4]:<9}{order[3]}\n'
        response += '```'
        await message.edit(content=response)
