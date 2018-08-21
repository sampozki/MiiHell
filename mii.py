from winsound import PlaySound, SND_FILENAME
from os import listdir, path
from time import sleep
from random import uniform


def main():
    directory = 'Mii/'
    soundlist = sorted(listdir(directory), key=lambda x: int(path.splitext(x)[0]))
    while True:
        for sound in soundlist:
            PlaySound(directory + sound, SND_FILENAME)
            sleep(round(uniform(0, 3), 1))


if __name__ == '__main__':
    main()
