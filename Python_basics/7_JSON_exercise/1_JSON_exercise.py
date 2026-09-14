import json

def main():
    print('Welcome! Lets add a new Pokemon to the Pokemons file')
    with open("7_JSON_Exercise/pokemons.json", mode='r', encoding='utf-8') as read_file:
        pokemons = json.load(read_file)
        print(pokemons[0].keys())
        new_register = ask_sub_values(pokemons[0])
        pokemons.append(new_register)
    with open("7_JSON_Exercise/pokemons.json", mode='w', encoding='utf-8') as write_file:
        json.dump(pokemons, write_file, indent=2, ensure_ascii=False)

def ask_sub_values(sub_dictionary):
    new_register = {}
    for key, value in sub_dictionary.items():
        if isinstance(value, dict):
            new_register[key] = ask_sub_values(value)
        elif isinstance(value, bool):
            answer = input(f' {key} (Write True or False) :')
            new_register[key] = answer == 'True'
        elif isinstance(value,int):
            answer = int(input(f'{key}: '))
            new_register[key] = answer
        elif isinstance(value, list):
            answer = input(f'{key} (If there is more than ONE answer, separate with COMMA ",") : ')
            new_register[key] = answer.split(',')
        else:
            answer = input(f'{key}: ')
            if answer:
                new_register[key] = answer   
            else:
                new_register[key] = None     
    return new_register


try:
    main()
except Exception as ex:
    print(f'There is a general error: {ex}')

#