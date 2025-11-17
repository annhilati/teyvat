import json5

jsonc_data = """
{
    // Kommentare sind erlaubt
    name: "json5-test", // Auch hier
    "version": 2, 
    "config": [
        1, 2, 3, // Trailing comma erlaubt (optional)
    ]
}
"""

data = json5.loads(jsonc_data)
print(data)
# Ausgabe: {'name': 'json5-test', 'version': 2, 'config': [1, 2, 3]}