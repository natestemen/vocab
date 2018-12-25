"""The practice command."""

import pandas as pd
from ruamel.yaml import YAML
import os.path
from termcolor import colored
from random import shuffle
from .base import Base

class Practice(Base):
    """practice your current vocab"""

    def run(self):
        yaml = YAML()
        home_directory = os.path.expanduser('~')
        vocab_directory = os.path.join(home_directory, '.vocab')
        vocabrc_file = os.path.join(vocab_directory, 'vocab.conf')
        with open(vocabrc_file) as f:
            current_vocab = yaml.load(f)['current_vocab']
        vocab_file = os.path.join(vocab_directory, current_vocab)
        with open(vocab_file) as f:
            vocab_data = pd.read_csv(f)
        if not self.options['--ordered']:
            vocab_data = vocab_data.sample(frac=1)
        if self.options['--no-tones']:
            vocab_data['tone'] = vocab_data['value']
            vocab_data['value'] = vocab_data.value.apply(lambda s: ''.join(l for l in s if not l.isdigit()))
        correct = 0
        for _, row in vocab_data.iterrows():
            print('Prompt:', colored(row['key'], attrs=['bold']))
            guess = input()
            if guess == row['value']:
                correct += 1
                print(colored('Correct!', 'green'))
                if self.options['--no-tones']:
                    print('With tones its:', colored(row['tone'], 'yellow'))
            else:
                print(colored('Incorrect', 'red'), 'it is', colored(row['value'], 'red', attrs=['underline']))
        print('Score:', correct, '/', len(vocab_data))