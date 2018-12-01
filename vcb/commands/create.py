"""The create command."""


import yaml

import os

from .base import Base


class Create(Base):
    """do some required setup for a new vocab set"""

    def run(self):
        home_directory = os.path.expanduser('~')
        vocab_directory = os.path.join(home_directory, '.vocab')
        if not os.path.isdir(vocab_directory):
            os.mkdir(vocab_directory)
        new_vocab_file = os.path.join(vocab_directory, self.options['<name>'])
        if not os.path.isfile(new_vocab_file):
            open(new_vocab_file, 'x').close()
            print('Your vocab path has been set to', new_vocab_file)
        else:
            print('You already have some vocab under that name please try ' \
                  'another name or add vocab to that file')