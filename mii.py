# MiiHell  ©sampozki -2018

from winsound import PlaySound, SND_FILENAME
from os import listdir, path
from time import sleep, time
from random import uniform, randint, choice
from shutil import rmtree, copytree
from pydub import AudioSegment
from configparser import ConfigParser
from sys import argv


def main(mutation, modulation, continuesaved):
    start = time()
    loop = 1
    destinationdirectory = 'Temp/'
    directory = 'Mii/'

    cfg = ConfigParser()
    if path.isfile('save.ini'):
        cfg.read('save.ini')
    else:
        a = open('save.ini', 'w')
        a.close()

    if not continuesaved:
        if path.isdir(destinationdirectory):
            rmtree(destinationdirectory)
            copytree(directory, destinationdirectory)
            print('Created new temporary folder from ' + directory + ' to ' + destinationdirectory)
            soundlist = sorted(listdir(destinationdirectory), key=lambda x: int(path.splitext(x)[0]))
        else:
            copytree(directory, destinationdirectory)
            print('Created temporary folder from ' + directory + ' to ' + destinationdirectory)
            soundlist = sorted(listdir(destinationdirectory), key=lambda x: int(path.splitext(x)[0]))

    else:
        if path.isdir(destinationdirectory):
            rmtree(destinationdirectory)
            copytree(directory, destinationdirectory)
        else:
            copytree(directory, destinationdirectory)
        if 'settings' in cfg:
            if 'soundlist' in cfg['settings']:
                print("\nLoaded old play order and statistics.")
                soundlist = cfg['settings']['soundlist'].split(", ")
            else:
                soundlist = sorted(listdir(destinationdirectory), key=lambda x: int(path.splitext(x)[0]))
                cfg['settings'] = {'soundlist': ", ".join(soundlist)}
        else:
            soundlist = sorted(listdir(destinationdirectory), key=lambda x: int(path.splitext(x)[0]))
            cfg['settings'] = {'soundist': ", ".join(soundlist)}

    if 'loop' in cfg['settings']:
        print('\n\nRound: ' + str(cfg['settings']['loop']) + ' | Time Spend: ' + str(cfg['settings']['playtime']) + ' minutes')
        print('Current play order: ' + ', '.join(soundlist))
    else:
        print('Original play order: ' + ', '.join(soundlist))

    while True:
        for sound in soundlist:
            PlaySound(destinationdirectory + sound, SND_FILENAME)
            sleep(round(uniform(0, 2), 1))
            if randint(0, 100000) == 88:
                PlaySound('surprise.wav', SND_FILENAME)
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

        cfg['settings'] = {'soundlist': ", ".join(soundlist),
                           'loop': loop,
                           'playtime': playtime}
        with open('save.ini', 'w') as configfile:
            cfg.write(configfile)


if __name__ == '__main__':
    if len(argv) == 1:
        mutation = True
        modulation = True
        continuesaved = True

    else:
        for a in range(0, len(argv)-1):
            if argv[a].lower() == "t":
                argv[a] = True
            elif argv[a].lower() == "f":
                argv[a] = False

        mutation = argv[0]
        modulation = argv[1]
        continuesaved = argv[2]

    print("\nPattern mutation:", mutation, "Pitch modulation:", modulation, "Load from profile:", continuesaved, "\n")
    main(mutation, modulation, continuesaved)
