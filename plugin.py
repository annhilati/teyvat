from beet import Context
from beet.contrib.worldgen import WorldgenNoiseSettings, Dimension
import yaml
import rhombus

def beet_default(ctx: Context):
    data = ctx.data

    # Fill surface_rule with external yaml file
    with open("./pack/data/teyvat/worldgen/noise_settings/surface_rules.yml", "r", encoding="utf-8") as f:
        data[WorldgenNoiseSettings]["teyvat:teyvat"].data["surface_rule"] = yaml.load(f, Loader=yaml.SafeLoader)
    
    # Fill surface_rule with external yaml file
    with open("./pack/data/teyvat/dimension/biomes.yml", "r", encoding="utf-8") as f:
        data[Dimension]["teyvat:teyvat"].data["generator"]["biome_source"]["biomes"] = yaml.load(f, Loader=yaml.SafeLoader)

    from terrain.natlan import OUT as natlan_terrain
    from terrain.continents import OUT as continent_terrain
    rhombus.inject(ctx, natlan_terrain, "teyvat:natlan_terrain")
    rhombus.inject(ctx, rhombus.math.sgn(continent_terrain), "teyvat:continents")