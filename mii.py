# MiiHell  ©sampozki -2018

from winsound import PlaySound, SND_FILENAME
from os import listdir, path
from time import sleep, time
from random import uniform, randint


def main():
    start = time()
    directory = 'Mii/'
    loop = 1
    soundlist = sorted(listdir(directory), key=lambda x: int(path.splitext(x)[0]))

    print('Round: ' + str(loop) + '\nCurrent play order: ' + ', '.join(soundlist))

    while True:
        for sound in soundlist:
            PlaySound(directory + sound, SND_FILENAME)
            sleep(round(uniform(0, 3.5), 1))

        # Mutates the pattern
        for a in range(0, randint(1, 2)):
            mutationa = randint(0, len(soundlist)-1)
            mutationb = randint(0, len(soundlist)-1)
            soundlist[mutationa], soundlist[mutationb] = soundlist[mutationb], soundlist[mutationa]
            print(soundlist[mutationa] + " <-> " + soundlist[mutationb], end="  ")

        loop += 1
        playtime = round((time() - start) / 60, 1)

        print('\n\nRound: ' + str(loop) + ' | Time Spend: ' + str(playtime) + ' minutes')
        print('Current play order: ' + ', '.join(soundlist))


if __name__ == '__main__':
    main()
