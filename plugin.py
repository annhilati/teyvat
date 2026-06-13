from beet import Context
from beet.contrib.worldgen import WorldgenNoiseSettings, Dimension
import yaml
import rhombus

def beet_default(ctx: Context):
    data = ctx.data

    # Fill surface_rule with external yaml file
    with open("./pack/data/teyvat/worldgen/noise_settings/surface_rules.yml", "r", encoding="utf-8") as f:
        data[WorldgenNoiseSettings]["teyvat:teyvat"].data["surface_rule"] = yaml.load(f, Loader=yaml.SafeLoader)

    # Fill biomes with external yaml file
    with open("./pack/data/teyvat/dimension/biomes.yml", "r", encoding="utf-8") as f:
        data[Dimension]["teyvat:teyvat"].data["generator"]["biome_source"]["biomes"] = yaml.load(f, Loader=yaml.SafeLoader)

    from terrain.natlan import OUT as natlan_terrain
    from terrain.plane_of_euthymia import FINAL_DESTINY as plane_of_euthymia_terrain
    from terrain.primordial_sea import FINAL_DESTINY as primordial_sea_terrain
    natlan_terrain.inject(ctx.data, "teyvat:natlan_terrain")
    plane_of_euthymia_terrain.inject(ctx.data, "teyvat:plane_of_euthymia_final_destiny")
    primordial_sea_terrain.inject(ctx.data, "teyvat:primordial_sea_final_destiny")
