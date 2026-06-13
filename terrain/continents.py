from rhombus import *

continents_rarity_noise = Noise(-10, [1.9, 1.0])
continents_noise = Noise(-9, [1.0])

continent_rarity_filter = noise(continents_rarity_noise, 1, 0)



OUT = range_choice(input=continent_rarity_filter, min_inclusive=0, max_exclusive=10, when_in_range=noise(continents_noise, 1, 0), when_out_of_range=continent_rarity_filter)
    # Maybe when_out_of_range should be something else because it is more than a filter then



# import json
# print(json.dumps(OUT.as_dict()))