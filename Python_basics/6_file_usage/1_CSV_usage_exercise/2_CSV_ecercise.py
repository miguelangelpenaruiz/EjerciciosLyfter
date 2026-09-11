# Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del 
# ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.


import csv

def main ():
    while True:
        print('Welcome! Please select a option of the menu \n Menu: \n a) Register a new video game \n b) Print the list of video games loaded \n c) Exit')
        selection = input('Write a or b or c: ')
        if selection == 'a':
            register_new_video_game()
        elif selection == 'b':
            print_video_games()
        elif selection == 'c':
            break
        else:
            print("You didn't write a valid answer!!")
    

def register_new_video_game():

    niu_name = input('Name of the video game:')
    niu_genre = input('Genre of the video game:')
    niu_developer = input('Name of the video game developer:')
    niu_score = input('Video game ESRB score:')
    new_register = dict([('Name',niu_name),('Genre', niu_genre) ,('Developer', niu_developer), ('Score', niu_score)])
    with open('6_File_Usage/1_CSV_usage_exercise/video_games_tabs.csv', 'a', encoding='utf-8', newline='') as file:
        headers = new_register.keys()
        writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(new_register)

def print_video_games():
    try:
        with open('6_File_Usage/1_CSV_usage_exercise/video_games_tabs.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for video_games in reader:
                print(video_games['Name'],video_games['Genre'],video_games['Developer'],video_games['Score'])
    except FileNotFoundError as ex:
        print(f'No video games file registered yet: {ex}')

try:
    main()
except Exception as ex:
    print(f'There is a general error: {ex}')