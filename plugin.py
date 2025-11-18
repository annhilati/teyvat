from beet import Context, JsonFileBase, JsonFile
from typing import Any
from json5 import loads

def require(ctx: Context):
    JsonFileBase.decoder = loads

def pipeline(ctx: Context):
    JsonFileBase.decoder = loads
    for _, json_file in ctx.data.list_files(extend=JsonFileBase[Any]):
        print(_)
        print(json_file.data)
        json_file.text = json_file.encoder(json_file.data)