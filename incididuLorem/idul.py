def my_generator():
    yield [5, 24, 0.0027901435057182357]

# Using the generator
for value in my_generator():
    print(value)
