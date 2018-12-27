"""The create command."""

from ruamel.yaml import YAML
import csv
import os
from .base import Base


class Create(Base):
    """do some required setup for a new vocab set"""

    def run(self):
        yaml = YAML()
        if not os.path.isdir(self.vocab_dir):
            os.mkdir(self.vocab_dir)
            with open(self.vocabrc, 'x') as f:
                yaml.dump({'current_vocab': None}, f)
        new_vocab_file = os.path.join(self.vocab_dir, self.options['<name>'])
        if not os.path.isfile(new_vocab_file):
            with open(new_vocab_file, 'x') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerow(['key', 'value', 'date_added'])
            with open(self.vocabrc) as f:
                vocabrc = yaml.load(f)
            vocabrc['current_vocab'] = self.options['<name>']
            with open(self.vocabrc, 'w') as f:
                yaml.dump(vocabrc, f)
            print('Your vocab path has been set to', new_vocab_file)
        else:
            print('You already have a vocab under that name please try ' \
                  'another name or add vocab to that file')