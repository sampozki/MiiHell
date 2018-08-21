import winsound
import os
import random
# TODO kaikki


def main():
    directory = 'Mii/'
    sounds = os.listdir(directory)
    while True:
        sound = random.choice(sounds)
        print(sound)
        winsound.PlaySound(directory + sound, winsound.SND_FILENAME)


if __name__ == '__main__':
    main()
