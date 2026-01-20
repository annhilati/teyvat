from rhombus import *

n = Noise(-5, amplitudes=[1.0])

y = lambda: y_clamped_gradient(-4060, 4060, -4060, 4060)

bottom = range_choice(y(), min_inclusive=-64, max_exclusive=-60, when_in_range=1, when_out_of_range=0)
top = range_choice(
    input=y(),
    min_inclusive=64,
    max_exclusive=65,
    when_in_range=range_choice(
        input=noise(n, xz_scale=1, y_scale=0),
        min_inclusive=-0.6,
        max_exclusive=2,
        when_in_range=1,
        when_out_of_range=0),
    when_out_of_range=0)

FINAL_DESTINY = max(bottom, top)