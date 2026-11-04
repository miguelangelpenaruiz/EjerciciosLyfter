import games

EASY_WORDS = [casa,pelo,mano,rojo]
MEDIUM_WORDS = [lapiz,reloj,canal,comer,jamon]
HARD_WORDS = [correr,lanzar,pelota,tomate,cabeza]

def play(game):
    while game.user_tries():
        game.show_word()
        print(f'You have {game.user_tries()} tries left')
        try:
            answer = input(game.user_participation())
        except ValueError:
            print('You lost!!')
        if answer:
            print('Congratulations!! You Won')

def menu():
    print("\nSelect difficulty")
    print('A) Easy')
    print('B) Medium')
    print('C) Hard')
    print('X) Exit')
    option = input('write the letter of list: ').strip().upper()
    while True:
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
                True