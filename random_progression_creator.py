from random import choice

chords = [
    "I",
    "Idom7",
    "I7",
    "vi",
    "vi7",
    "ii",
    "ii7",
    "iii7",
    "I7",
    "IV",
    "IVdom7",
    "IV7",
    "viidom7",
    "V7",
    "Vdom7"
]
keys = [
        'Cb', 'ab', 'Gb', 'eb', 'Db', 'bb', 'Ab', 'f', 'Eb', 'c', 'Bb', 'g', 'F', 'd', 'C', 'a',
        'G', 'e', 'D', 'b', 'A', 'f#', 'E', 'c#', 'B', 'g#', 'F#', 'd#', 'C#', 'a#'
    ]

class Progression:
    """A progression object.
    
    This is an object that generates a list of relative chords of a given
    length and generates a 'key' attribute.
    
    Specifically created for use with the mingus library.
    """
    def __init__(self):
        self.key = choice(keys)
    def get_new(self, length: int):
        yield [choice(chords) for p in range(length)]
