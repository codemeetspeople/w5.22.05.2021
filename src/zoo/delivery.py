import os
from string import ascii_lowercase
import random

MODULE_PATH = os.path.abspath(os.path.dirname(__file__))
ANIMALS_PATH = os.path.join(MODULE_PATH, 'animals.py')


def deliver(animal):
    sound_template = ''.join([random.choice(ascii_lowercase) for i in range(4)])
    class_template = (
        '@animal_in_zoo\n'
        'class {class_name}(Animal):\n'
        '    @classmethod\n'
        '    def speak(cls):\n'
        '        print(f\'{{cls.get_title()}} say {sound}-{sound}\')\n\n'
    )

    source = open(ANIMALS_PATH, 'r')
    source_code = source.read()
    source.close()

    tpl = class_template.format(
        class_name=animal.capitalize(),
        sound=sound_template
    )

    destination = open(ANIMALS_PATH, 'w')
    destination.write(f'{source_code}\n{tpl}')
    destination.close()
