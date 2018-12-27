"""The use command."""


from ruamel.yaml import YAML
import os.path
from .base import Base


class Use(Base):
    """set the current vocab"""

    def run(self):
        yaml = YAML()
        vocab_directory = self.vocab_dir
        new_vocab_file = os.path.join(vocab_directory, self.options['<name>'])
        if not os.path.isfile(new_vocab_file):
            print('You do not have that vocab file yet.\n' \
                  'Use vcb create {} to generate it.'.format(self.options['<name>']))
            return
        with open(self.vocabrc) as f:
            dat = yaml.load(f)
        dat['current_vocab'] = self.options['<name>']
        with open(self.vocabrc, 'w') as f:
            yaml.dump(dat, f)
        print("You're now using your {} vocab, located at {}".format(self.options['<name>'], new_vocab_file))