# 2. The Lazy Robot
# A robot is programmed to clean only if the user gives it a command, but due to indentation, it might slack off.

clean = True
tidy = True

if clean:
    print("Cleaning in progress...")
    print("Cleaning done!")
    if tidy:
      print("Tidying in progress...")
      print("Tidying done!")
print("Time for a nap.")  # Robot always naps after cleaning

