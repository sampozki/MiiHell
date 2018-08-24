# MiiHell  ©sampozki -2018

from winsound import PlaySound, SND_FILENAME
from os import listdir, path
from time import sleep, time
from random import uniform, randint, choice
from shutil import rmtree, copytree
from pydub import AudioSegment


def main(mutation, modulation):
    start = time()
    loop = 1
    destinationdirectory = 'Temp/'
    directory = 'Mii/'

    if path.isdir(destinationdirectory):
        rmtree(destinationdirectory)
        copytree(directory, destinationdirectory)
        print('Created new temporary folder from ' + directory + ' to ' + destinationdirectory)
    else:
        copytree(directory, destinationdirectory)
        print('Created temporary folder from ' + directory + ' to ' + destinationdirectory)

    soundlist = sorted(listdir(destinationdirectory), key=lambda x: int(path.splitext(x)[0]))

    print('Original play order: ' + ', '.join(soundlist))

    while True:
        for sound in soundlist:
            PlaySound(destinationdirectory + sound, SND_FILENAME)
            sleep(round(uniform(0, 2), 1))
        print()

        # Changes the pitch
        if modulation:
            if randint(0, 1) == 1:
                for a in range(0, randint(1, 3)):
                    filu = choice(soundlist)
                    sound = AudioSegment.from_file(destinationdirectory + filu, format='wav')
                    octaves = round(uniform(-0.18, 0.18), 2)
                    new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
                    changedsound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
                    changedsound = changedsound.set_frame_rate(44100)
                    changedsound.export(destinationdirectory + filu, format='wav')
                    print(filu + ' ~ ' + str(octaves) + ' octaves', end="  ")
            else:
                print()

        print()

        # Mutates the pattern
        if mutation:
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
    mutation = True
    modulation = True
    main(mutation, modulation)
