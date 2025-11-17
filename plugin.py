from beet import Context, JsonFileBase
from json5 import loads

def beet_default(ctx: Context):
    JsonFileBase.decoder = loads