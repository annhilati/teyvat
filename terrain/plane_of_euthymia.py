from rhombus import *

n = Noise(-5, amplitudes=[1.0])

hills = noise(n, xz_scale=1, y_scale=0) + y_clamped_gradient(from_value=1.2, to_value=-1.2, from_y=5, to_y=24)

radius = lambda: emath.sqrt(coords.x()**2 + coords.z()**2)

FINAL_DESTINY = range_choice(input=coords.x(), min_inclusive=0, max_exclusive=15, when_in_range=1, when_out_of_range=hills)