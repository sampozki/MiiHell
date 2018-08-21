import winsound
import os
import time
import random


def main():
    directory = 'Mii/'
    sounds = sorted(os.listdir(directory), key=lambda x: int(os.path.splitext(x)[0]))
    while True:
        for sound in sounds:
            winsound.PlaySound(directory + sound, winsound.SND_FILENAME)
            time.sleep(round(random.uniform(0, 3), 1))


if __name__ == '__main__':
    main()
