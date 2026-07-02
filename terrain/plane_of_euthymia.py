from rhombus import *
when = conditional.when

n = Noise(-5, amplitudes=[1.0])

hills_heightmap = noise(n, y_scale=0)

radius = lambda: emath.sqrt(coords.x()**2 + coords.z()**2, iterations=1)

heightmap = when(radius()).atmost(200).then(-0.2).otherwise(hills_heightmap)

FINAL_DESTINY = maps.extrude_heightmap(heightmap, (-1.2, 1.2), (5, 24))
