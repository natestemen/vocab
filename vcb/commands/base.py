"""The base command."""

import os.path

from ruamel.yaml import YAML


class Base(object):
    """A base command."""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        self.home_dir = os.path.expanduser("~")
        self.vocab_dir = os.path.join(self.home_dir, ".vocab")
        self.vocabrc = os.path.join(self.vocab_dir, "vocab.conf")

    def current_vocab(self):
        yaml = YAML()
        with open(self.vocabrc) as f:
            rc = yaml.load(f)
            return rc["current_vocab"]

    def current_vocab_file(self):
        return os.path.join(self.vocab_dir, self.current_vocab())

    def run(self):
        raise NotImplementedError("You must implement the run() method yourself!")
