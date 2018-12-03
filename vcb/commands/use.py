"""The use command."""


from ruamel.yaml import YAML

import os.path

from .base import Base


class Use(Base):
    """set the current vocab"""

    def run(self):
        yaml = YAML()
        home_directory = os.path.expanduser('~')
        vocab_directory = os.path.join(home_directory, '.vocab')
        vocabrc_file = os.path.join(vocab_directory, 'vocab.conf')
        new_vocab_file = os.path.join(vocab_directory, self.options['<name>'])
        if not os.path.isfile(new_vocab_file):
            print('You do not have that vocab file yet.\n' \
                  'Use vcb create {} to generate it.'.format(self.options['<name>']))
            return
        with open(vocabrc_file) as f:
            dat = yaml.load(f)
        dat['current_vocab'] = self.options['<name>']
        with open(vocabrc_file, 'w') as f:
            yaml.dump(dat, f)
        print("You're now using your {} vocab, located at {}".format(self.options['<name>'], new_vocab_file))