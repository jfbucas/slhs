# Chocolate cake algorithm

# Ingredients
flour     = 120 # grams
butter    = 120 # grams
chocolate = 200 # grams
suggar    =  80 # grams
eggs      =   4

# Instruments
spoon = 1
mould = 1
bowl  = []

if free_time == 40: # minutes

    # Set the temperature
    preheat_oven(200) # degrees
    
    # Melt Chocolate and Butter
    chocolate_butter = microwave( [chocolate, butter], 500 ) # Watts
    
    # Mix ingredients
    bowl = mix_ingredients( [eggs, suggar, flour, chocolate_butter] )

    # Pour in silicon mould
    pour( bowl, mould )
    
    # Put in oven
    ovenize( mould, 25 ) # minutes

