# Plays random samples atm cos even more anoying
# TODO Play in correct order but in random intervals :DDDDD

import winsound
import os
import random


def main():
    directory = 'Mii/'
    sounds = os.listdir(directory)
    while True:
        sound = random.choice(sounds)
        print(sound)
        winsound.PlaySound(directory + sound, winsound.SND_FILENAME)


if __name__ == '__main__':
    main()
