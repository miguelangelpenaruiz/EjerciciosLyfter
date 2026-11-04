import games

EASY_WORDS = ["casa","pelo","mano","rojo"]
MEDIUM_WORDS = ["lapiz","reloj","canal","comer","jamon"]
HARD_WORDS = ["correr","lanzar","pelota","tomate","cabeza"]

def play(game):
    while game.game_over_method() == False:
        print(game.show_word())
        print(f'You have {game.user_tries} tries left')
        answer = input('Guess the word: ').strip().lower()
        participation = game.user_participation(answer)
        if participation:
            print('Congratulations!! You Won')
            break

def menu():
    while True:
        print("\nSelect difficulty")
        print('A) Easy')
        print('B) Medium')
        print('C) Hard')
        print('X) Exit')
        option = input('write the letter of list: ').strip().upper()
        match option:
            case "A":
                play(games.GameModeEasy(EASY_WORDS))
            case "B":
                print('')
            case "C":
                print('')
            case "X":
                break
            case _:
                print('Invalid answer! Please make sure you to write a valid option (A-C or X for exit)')