import urllib.request
import json

faction_augments = {
    'steel meridian': [
        'path of statues (atlas)',
        'tectonic fracture (atlas)',
        'ore gaze (atlas)',
        'titanic rumbler (atlas)',
        'rubble heap (atlas)',
        'fireball frenzy (ember)',
        'immolated radiance (ember)',
        'healing flame (ember)',
        'exothermic (ember)',
        'surging dash (excalibur)',
        'radiant finish (excalibur)',
        'furious javelin (excalibur)',
        'chromatic blade (excalibur)',
        'freeze force (frost)',
        'ice wave impedance (frost)',
        'chilling globe (frost)',
        'icy avalanche (frost)',
        'biting frost (frost)',
        'dread ward (garuda)',
        'blood forge (garuda)',
        'blending talons (garuda)',
        'gourmand (grendel)',
        'hearty nourishment (grendel)',
        'catapult (grendel)',
        'accumulating whipclaw (khora)',
        'venari bodyguard (khora)',
        'pilfering strangledome (khora)',
        'ballistic bullseye (mesa)',
        'staggering shield (mesa)',
        'muzzle flash (mesa)',
        'mesas waltz (mesa)',
        'pyroclastic flow (nezha)',
        'reaping chakram (nezha)',
        'safeguard (nezha)',
        'controlled slide (nezha)',
        'teeming virulence (nidus)',
        'larva burst (nidus)',
        'insatiable (nidus)',
        'abundant mutation (nidus)',
        'neutron star (nova)',
        'antimatter absorb (nova)',
        'escape velocity (nova)',
        'molecular fission (nova)',
        'smite infusion (oberon)',
        'hallowed eruption (oberon)',
        'phoenix renewal (oberon)',
        'hallowed reckoning (oberon)',
        'ironclad charge (rhino)',
        'iron shrapnel (rhino)',
        'piercing roar (rhino)',
        'reinforcing stomp (rhino)',
        'venom dose (saryn)',
        'regenerative molt (saryn)',
        'contagion cloud (saryn)',
        'revealing spores (saryn)',
        'ulfruns endurance (voruna)',
        'vampiric grasp (xaku)',
        'the relentless lost (xaku)',
    ],
    'arbiters of hexis': [
        'seeking shuriken (ash)',
        'smoke shadow (ash)',
        'fatal teleport (ash)',
        'rising storm (ash)',
        'endless lullaby (baruuk)',
        'reactive storm (baruuk)',
        'duality (equinox)',
        'calm and frenzy (equinox)',
        'peaceful provocation (equinox)',
        'energy transfer (equinox)',
        'surging dash (excalibur)',
        'radiant finish (excalibur)',
        'furious javelin (excalibur)',
        'chromatic blade (excalibur)',
        'shattered storm (gara)',
        'mending splinters (gara)',
        'spectrosiphon (gara)',
        'mach crash (gauss)',
        'thermal transfer (gauss)',
        'cathode current (gyre)',
        'tribunal (harrow)',
        'warding thurible (harrow)',
        'lasting covenant (harrow)',
        'desiccations curse (inaros)',
        'elemental sandstorm (inaros)',
        'negation swarm (inaros)',
        'rift haven (limbo)',
        'rift torrent (limbo)',
        'cataclysmic continuum (limbo)',
        'savior decoy (loki)',
        'hushed invisibility (loki)',
        'safeguard switch (loki)',
        'irradiating disarm (loki)',
        'hall of malevolence (mirage)',
        'explosive legerdemain (mirage)',
        'total eclipse (nyx)',
        'mind freak (nyx)',
        'pacifying bolts (nyx)',
        'chaos sphere (nyx)',
        'assimilate (nyx)',
        'repair dispensary (protea)',
        'shock trooper (volt)',
        'shocking speed (volt)',
        'transistor shield (volt)',
        'capacitance (volt)',
        'celestial stomp (wukong)',
        'enveloping cloud (wukong)',
        'primal rage (wukong)',
    ],
    'cephalon suda': [
        'sonic fracture (banshee)',
        'resonance (banshee)',
        'savage silence (banshee)',
        'resonating quake (banshee)',
        'afterburn (chroma)',
        'everlasting ward (chroma)',
        'vexing retaliation (chroma)',
        'guided effigy (chroma)',
        'freeze force (frost)',
        'ice wave impedance (frost)',
        'chilling globe (frost)',
        'icy avalanche (frost)',
        'biting frost (frost)',
        'balefire surge (hildryn)',
        'blazing pillage (hildryn)',
        'corroding barrage (hydroid)',
        'tidal impunity (hydroid)',
        'curative undertow (hydroid)',
        'pilfering swarm (hydroid)',
        'empowered quiver (ivara)',
        'piercing navigator (ivara)',
        'infiltrate (ivara)',
        'concentrated arrow (ivara)',
        'rift haven (limbo)',
        'rift torrent (limbo)',
        'cataclysmic continuum (limbo)',
        'hall of malevolence (mirage)',
        'explosive legerdemain (mirage)',
        'total eclipse (mirage)',
        'pyroclastic flow (nezha)',
        'reaping chakram (nezha)',
        'safeguard (nezha)',
        'controlled slide (nezha)',
        'neutron star (nova)',
        'antimatter absorb (nova)',
        'escape velocity (nova)',
        'molecular fission (nova)',
        'partitioned mallet (octavia)',
        'conductor (octavia)',
        'thrall pact (revenant)',
        'mesmer shield (revenant)',
        'blinding reave (revenant)',
        'tesla bank (vauban)',
        'repelling bastille (vauban)',
        'photon repeater (vauban)',
        'fused reservoir (wisp)',
        'critical surge (wisp)',
        'vampiric grasp (xaku)',
        'the relentless lost (xaku)',
        'merulina guardian (yareli)',
        'surging blades (yareli)',
    ],
    'the perrin sequence': [
        'sonic fracture (banshee)',
        'resonance (banshee)',
        'savage silence (banshee)',
        'resonating quake (banshee)',
        'afterburn (chroma)',
        'everlasting ward (chroma)',
        'vexing retaliation (chroma)',
        'guided effigy (chroma)',
        'mach crash (gauss)',
        'thermal transfer (gauss)',
        'cathode current (gyre)',
        'balefire surge (hildryn)',
        'blazing pillage (hildryn)',
        'desiccations curse (inaros)',
        'elemental sandstorm (inaros)',
        'negation swarm (inaros)',
        'empowered quiver (ivara)',
        'piercing navigator (ivara)',
        'infiltrate (ivara)',
        'concentrated arrow (ivara)',
        'greedy pull (mag)',
        'magnetized discharge (mag)',
        'counter pulse (mag)',
        'fracturing crush (mag)',
        'soul survivor (nekros)',
        'creeping terrify (nekros)',
        'despoil (nekros)',
        'shield of shadows (nekros)',
        'teeming virulence (nidus)',
        'larva burst (nidus)',
        'insatiable (nidus)',
        'abundant mutation (nidus)',
        'repair dispensary (protea)',
        'thrall pact (revenant)',
        'mesmer shield (revenant)',
        'blinding reave (revenant)',
        'ironclad charge (rhino)',
        'iron shrapnel (rhino)',
        'piercing roar (rhino)',
        'reinforcing stomp (rhino)',
        'pool of life (trinity)',
        'vampire leech (trinity)',
        'abating link (trinity)',
        'champions blessing (trinity)',
        'swing line (valkyr)',
        'eternal war (valkyr)',
        'prolonged paralysis (valkyr)',
        'hysterical assault (valkyr)',
        'enraged (valkyr)',
        'tesla bank (vauban)',
        'repelling bastille (vauban)',
        'photon repeater (vauban)',
    ],
    'red veil': [
        'seeking shuriken (ash)',
        'smoke shadow (ash)',
        'fatal teleport (ash)',
        'rising storm (ash)',
        'path of statues (atlas)',
        'tectonic fracture (atlas)',
        'ore gaze (atlas)',
        'titanic rumbler (atlas)',
        'rubble heap (atlas)',
        'fireball frenzy (ember)',
        'immolated radiance (ember)',
        'healing flame (ember)',
        'exothermic (ember)',
        'dread ward (garuda)',
        'blood forge (garuda)',
        'blending talons (garuda)',
        'gourmand (grendel)',
        'hearty nourishment (grendel)',
        'catapult (grendel)',
        'tribunal (harrow)',
        'warding thurible (harrow)',
        'lasting covenant (harrow)',
        'accumulating whipclaw (khora)',
        'venari bodyguard (khora)',
        'pilfering strangledome (khora)',
        'swift bite (lavos)',
        'savior decoy (loki)',
        'hushed invisibility (loki)',
        'safeguard switch (loki)',
        'irradiating disarm (loki)',
        'ballistic bullseye (mesa)',
        'staggering shield (mesa)',
        'muzzle flash (mesa)',
        'mesas waltz (mesa)',
        'soul survivor (nekros)',
        'creeping terrify (nekros)',
        'despoil (nekros)',
        'shield of shadows (nekros)',
        'venom dose (saryn)',
        'revealing spores (saryn)',
        'regenerative molt (saryn)',
        'contagion cloud (saryn)',
        'spellbound harvest (titania)',
        'beguiling lantern (titania)',
        'razorwing blitz (titania)',
        'ironclad flight (titania)',
        'shock trooper (volt)',
        'shocking speed (volt)',
        'transistor shield (volt)',
        'capacitance (volt)',
        'target fixation (zephyr)',
        'airburst rounds (zephyr)',
        'jet stream (zephyr)',
        'funnel clouds (zephyr)',
        'anchored glide (zephyr)',
    ],
    'new loka': [
        'endless lullaby (baruuk)',
        'reactive storm (baruuk)',
        'duality (equinox)',
        'calm and frenzy (equinox)',
        'peaceful provocation (equinox)',
        'energy transfer (equinox)',
        'shattered storm (gara)',
        'mending splinters (gara)',
        'spectrosiphon (gara)',
        'corroding barrage (hydroid)',
        'tidal impunity (hydroid)',
        'curative undertow (hydroid)',
        'pilfering swarm (hydroid)',
        'swift bite (lavos)',
        'greedy pull (mag)',
        'magnetized discharge (mag)',
        'counter pulse (mag)',
        'fracturing crush (mag)',
        'mind freak (nyx)',
        'pacifying bolts (nyx)',
        'chaos sphere (nyx)',
        'assimilate (nyx)',
        'smite infusion (oberon)',
        'hallowed eruption (oberon)',
        'phoenix renewal (oberon)',
        'hallowed reckoning (oberon)',
        'partitioned mallet (octavia)',
        'conductor (octavia)',
        'spellbound harvest (titania)',
        'beguiling lantern (titania)',
        'razorwing blitz (titania)',
        'ironclad flight (titania)',
        'pool of life (trinity)',
        'vampire leech (trinity)',
        'abating link (trinity)',
        'champions blessing (trinity)',
        'swing line (valkyr)',
        'eternal war (valkyr)',
        'prolonged paralysis (valkyr)',
        'hysterical assault (valkyr)',
        'enraged (valkyr)',
        'fused reservoir (wisp)',
        'critical surge (wisp)',
        'target fixation (zephyr)',
        'airburst rounds (zephyr)',
        'jet stream (zephyr)',
        'funnel clouds (zephyr)',
        'anchored glide (zephyr)',
        'celestial stomp (wukong)',
        'enveloping cloud (wukong)',
        'primal rage (wukong)',
        'merulina guardian (yareli)',
        'surging blades (yareli)',
    ],
    }


class WarframeMarket:

    def __init__(self, api_key: str):
        """
        Initialize this WarframeMarket object.

        :param apikey: The Cookie API Key to use.
        """
        self.__key = api_key

    def search_item(self, item: str, platform='pc'):
        item_id = item.lower().replace(' ', '_')
        url = f'https://api.warframe.market/v1/items/{item_id}'
        request_site = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0',
                                                            'Platform': platform})
        web_url = urllib.request.urlopen(request_site)
        resp = json.loads(web_url.read().decode(web_url.info().get_content_charset('utf-8')))
        if resp.get('error'):
            error_msg = resp['error']
            raise LookupError(error_msg)
        return resp['payload']['item']['items_in_set']

    def search_buy_orders(self, item: str, platform='pc', results=5):
        """
        Searches the Warframe Market and returns a list of the best (price) buy orders available.

        :param item: The name of the item to look for, ex. "Garuda Prime Neuroptics Blueprint"
        :param platform: The platform to look on. Can be one of ('pc', 'xbox', 'ps4', 'switch'), defaults to 'pc'
        :param results: The number of results to return, defaults to 5
        :raises LookupError: If something has gone wrong with the URL request
        :return: A list of the top buy orders available
        """
        item_id = item.lower().replace(' ', '_')
        url = f'https://api.warframe.market/v1/items/{item_id}/orders'
        request_site = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0',
                                                            'Cookie': f'JWT={self.__key}',
                                                            'Platform': platform})
        web_url = urllib.request.urlopen(request_site)
        try:
            resp = json.loads(web_url.read().decode(web_url.info().get_content_charset('utf-8')))
        except json.decoder.JSONDecodeError:
            raise ValueError('Invalid item name.')
        if resp.get('error'):
            error_msg = resp['error']
            raise LookupError(error_msg)
        buy_orders = []
        for order in resp['payload']['orders']:
            if order['order_type'] == 'buy':
                buy_orders.append(order)
        buy_orders.sort(key=lambda o: o['platinum'], reverse=True)
        best_orders = []
        # Add the best in-game buy orders to the list of best orders
        for order in buy_orders:
            if order['user']['status'] == 'ingame':
                best_orders.append(order)
            if len(best_orders) == results:
                break
        # Add the best online buy orders to the list of best orders, if needed
        if len(best_orders) < results:
            for order in buy_orders:
                if order['user']['status'] == 'online':
                    best_orders.append(order)
                if len(best_orders) == results:
                    break
        # Add the best offline buy orders to the list of best orders, if needed
        if len(best_orders) < results:
            for order in buy_orders:
                if order['user']['status'] == 'offline':
                    best_orders.append(order)
                if len(best_orders) == results:
                    break
        return best_orders
