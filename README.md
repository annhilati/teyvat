## Impressions
> This is a proof of concept for the Natlan terrain generation as of December 2025. First features for the biome are present too.
![alt text](.github/Natlan%20December%202025.png)

## Dump for Developers

- Density Functions
  - `source/`: 2D-Maps
  - `noise_router/`: Fertige DFs für den Noise Router

1. Land oder Meer? -> DF für Land-Terrain bzw. DF für Meeres-Terrain
2. Terrainart bestimmen -> DF für bestimmte Terrainart; weitläufig verblenden
3. Terrain bauen, aus beliebigen Heightmaps und anderen DF (z.B. Arcs)

## Map of the Density Functions

```mermaid
flowchart BT
    NR((Noise Router))
    nr/final_destiny[noise_router/final_destiny] --> NR
    t/natlan[terrain/natlan] --> nr/final_destiny
    t/natlan/height[terrain/natlan/height] --> t/natlan
    n/natlan_erosion[noise/natlan_erosion] --> t/natlan/height
    Nnate{{natlan_erosion}} --> n/natlan_erosion

```
