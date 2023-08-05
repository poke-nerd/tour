def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return [item.strip() for item in data]

trainers_file = 'trainers.txt'
moves_file = 'moves.txt'
items_file = 'items.txt'
pokemon_file = 'pokemon.txt'

trainers = read_txt_file(trainers_file)
pokemon = read_txt_file(pokemon_file)
items = read_txt_file(items_file)
moves = read_txt_file(moves_file)

# Organize data into Pokepaste format with separate teams
pokepaste = ''
for i in range(47):
    pokepaste += f'{trainers[i]}\n'
    for j in range(6):
        j = 6*i + j
        pokepaste += f'{pokemon[j]}' + ' @ ' +f'{items[j]}\n'
        for k in range(4):
            k = 4*j + k
            pokepaste += '-' + f'{moves[k]}\n'
        pokepaste += '\n'

# Save the Pokepaste content to a new file
pokepaste_file = 'pokepaste.txt'
with open(pokepaste_file, 'w', encoding='utf-8') as file:
    file.write(pokepaste)

print("Pokepaste created and saved to 'pokepaste.txt'.")
