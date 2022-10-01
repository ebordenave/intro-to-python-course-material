# The function will have two parameters. The first parameter is a set of strings known as Colors. A second parameter
# is a list of tuple-2 known as Values. Colors will contain a set of randomly selected colors. Values will contain a
# list of tuples of size 2. Each tuple will contain color (str) and a number (int). The function should look at each
# tuple in Values. For each tuple, add the number (the second value in the tuple) to a list of numbers if the color
# in the tuple (the first value in the tuple) is in Colors. In other words, find all tuples that have a color in the
# Colors and add the tuples numbers to a list. Finally, the function should return the list of numbers collected in
# the order they are found in the values list.
#
# Example:
#
# Colors: {'black', 'pink', 'yellow'}
# values: [('green', 100), ('yellow', 13), ('red', 6)]
# Expected: [13]
#
# Colors: {'yellow'}
# values: [('black', 54), ('pink', 5)]
# Expected: []
#
# Colors: {'black', 'blue', 'yellow'}
# values: [('yellow', 29), ('yellow', 19), ('black', 31), ('yellow', 67), ('green', 44)]
# Expected: [29, 19, 31, 67]




# def find_color(colors:set, values:list) -> list: