# Python Stack - Day 2

# Loops (Deeper Dive)

# for-in loops with range() function

# for-in loops over lists with range() function
# colors = ['blue', 'yellow', 'green', 'red']
# for i in range(len(colors)):
#     print(colors[i])

# # for-in loops over lists without range() function
# for color in colors:
#     print(f'Without range function: {color}')

# for-in loops through dictionaries
shang = {
    'real_name': 'Shang-Chi',
    'code_name': 'Shang-Chi, Master of Kung Fu',
    'origin': 'Raised to be an assassin.',
    'arch_enemy': 'Fu Manchu'
}

# for key_name in shang:
#     print(key_name) # prints out key names
#     print(shang[key_name]) # prints out values at key names
#     print(key_name, shang[key_name]) # prints out key name, then value at key name

# This is a list of dictionaries

marvel_superheroes = [
    {
        'real_name': 'Shang-Chi',
        'code_name': 'Shang-Chi, Master of Kung Fu',
        'origin': 'Raised to be an assassin.',
        'arch_enemy': 'Fu Manchu'
    },
    {
        'real_name': 'Peter Parker',
        'code_name': 'Spider-Man',
        'origin': 'Radioactive spider.',
        'arch_enemy': 'Green Goblin'
    },
    {
        'real_name': 'Luke Cage',
        'code_name': 'Luke Cage',
        'origin': 'Failed prison experiment.',
        'arch_enemy': 'Diamondback'
    },
    {
        'real_name': 'Matt Murdock',
        'code_name': 'Daredevil',
        'origin': 'Radioactive isotopes.',
        'arch_enemy': 'Kingpin'
    },
    {
        'real_name': 'Steve Rogers',
        'code_name': 'Captain America',
        'origin': 'Super soldier serum.',
        'arch_enemy': 'The Red Skull'
    },
]

for superhero in marvel_superheroes:
    for trait in superhero:
        print(superhero[trait])

