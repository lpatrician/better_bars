"""
    *** Description ***
    Creates a random progression of chords and plays them using fluidsynth.
    You must specify the SF2 soundfont file.
"""

from mingus.core import *
from mingus.core import chords as ch
from mingus.containers import NoteContainer, Note
from mingus.midi import fluidsynth
import time
import sys
from random import *
from random_progression_creator import Progression

run_length = range(int(input("How long a song? ")))
ind_length = int(input("How many bars? "))
prog = Progression()
SF2 = '/Users/leopatrician/Desktop/SoundFonts/mustheory2/mustheory2.sf2'
key = prog.key

for l in run_length:
    loop = next(prog.get_new(ind_length))
    chords = progressions.to_chords(loop, key)
    if not fluidsynth.init(SF2):
        print("Couldn't load SoundFont", SF2)
        sys.exit(1)
    i = 0
    for chord in chords:
        c = NoteContainer(chords[i])
        l = Note(c[0].name)
        p = c[1]
        l.octave_down()
        print(ch.determine(chords[i])[0])

        # Play chord and lowered first note

        fluidsynth.play_NoteContainer(c)
        fluidsynth.play_Note(l)
        time.sleep(1.0)

        # Play highest note in chord

        fluidsynth.play_Note(c[-1])

        # 50% chance on a bass note

        if random() > 0.50:
            p = Note(c[1].name)
            p.octave_down()
            fluidsynth.play_Note(p)
        time.sleep(0.50)

        # 50% chance on a ninth

        if random() > 0.50:
            l = Note(intervals.second(c[0].name, key))
            l.octave_up()
            fluidsynth.play_Note(l)
        time.sleep(0.25)

        # 50% chance on the second highest note

        if random() > 0.50:
            fluidsynth.play_Note(c[-2])
        time.sleep(0.25)
        fluidsynth.stop_NoteContainer(c)
        fluidsynth.stop_Note(l)
        fluidsynth.stop_Note(p)
        i += 1
    print("-" * 20)

rating = int(input("Give those bars a rating! Enter a number 1 to 10: ", or 1))

if rating in range(1, 11):
    print("Thanks - we've saved your rating.")
else:
    print("Error: invalid rating.")
    rating = 5