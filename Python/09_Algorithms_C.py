# Algorithm

# Sort a list

# We start with a few random numbers
start  = [ 12, 5, 16, 0, 25 ]

# We want them storted
finish = [ 0, 5, 12, 16, 25 ]


# Index in the list
#     [0]  [1]  [2]  [3]  [4] 
l = [ 12,   5,  16,   0,  25 ]

print(l, "Starting point")

# Let's swap index [0] and [3]
# We use t for temporary storage

t    = l[0]
l[0] = l[3]
l[3] = t

print(l, "After first swap")

# Let's swap index [2] and [3]

t    = l[2]
l[2] = l[3]
l[3] = t

print(l, "After second swap")


exit() # Remove this line to continue
