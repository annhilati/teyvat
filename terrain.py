from rhombus.language import *

c = ConfiguredDensity("teyvat:constant/test", 5.0)

continent_noise = Noise(-10, [2, 1, 2, 2, 2, 1, 1, 1, 1])


natlan_erosion_noise = Noise(-9, [3.5, 0, 2, 4, 2, 2, 3])

natlan_erosion = clamp(noise(natlan_erosion_noise, 1.3, 0) - 0.1, min=-1, max=1)

natlan_height_map = spline(natlan_erosion, [
        (-1,    -1,     0),
        (-0.6,  -0.95,  0),
        (-0.61, -0.6,   0),
        (-0.2,  -0.55,  0),
        (-0.21, -0.2,   0),
        ( 0.05, -0.2,   0),
        ( 0.21,  0.2,   0),
        ( 0.6,   0.3,   0),
        ( 0.61,  0.8,   0),
        ( 1,     0.8,   0)
])

terrain_natlan = natlan_height_map + y_clamped_gradient(from_y=64, to_y=256, from_value=1.001, to_value=-1.001)

out = terrain_natlan