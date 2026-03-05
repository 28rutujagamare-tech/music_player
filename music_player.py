import os 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']='hide'
import pygame

def play_music(folder,song_name):
    file_path=os.path.join(folder,song_name)

    if not os.path.exists(file_path):
        print('file not found')
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print(f'now playing :{song_name}')
    print('command :[P]ause,[R]esume,[S]top')

    while True:
        command=input('>').upper()
        if command =='P':
            pygame.mixer.music.pause()
            print("Pause⏸️")
        elif command =='R':
            pygame.mixer.music.unpause()
            print("Resume🟰")
        elif command =='S':
            pygame.mixer.music.stop()
            print("Stop🛑")
            return
        else:
            print('invalid command')

def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print('audio initialization failed ', e)
        return

    folder='music'

    if not os.path.isdir(folder):
        print(f'folder {folder} not found')
        return
    
    mp3_file=[file for file in os.listdir(folder) if file.endswith('.mp3')]

    if not mp3_file:
        print('no mp3 found')
    
    while True:
        print('➖'*10,'music player','➖'*10)
        for index,song in enumerate(mp3_file):
            print(f'{index}.{song}')
        print('➖'*10,'end','➖'*10)

        choice_input=(input('enter your choice or else if you want to quit type(q)'))
        if choice_input.upper()=='Q':
            print('byeeeee')
            break

        choice=int(choice_input)

        if 0<=choice <len(mp3_file):
            play_music(folder,mp3_file[choice])
        else:
            print('invaile choice')

if __name__=='__main__':
    main()
