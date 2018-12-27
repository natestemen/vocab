"""The base command."""

import os.path
import re

from ruamel.yaml import YAML
from termcolor import colored

PINYIN_TONES = {
    0: "aoeiuv\u00fc",
    1: "\u0101\u014d\u0113\u012b\u016b\u01d6\u01d6",
    2: "\u00e1\u00f3\u00e9\u00ed\u00fa\u01d8\u01d8",
    3: "\u01ce\u01d2\u011b\u01d0\u01d4\u01da\u01da",
    4: "\u00e0\u00f2\u00e8\u00ec\u00f9\u01dc\u01dc",
}

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

    def update_current_vocab(self):
        yaml = YAML()
        with open(self.vocabrc) as f:
            vocabrc = yaml.load(f)
        vocabrc["current_vocab"] = self.options["<name>"]
        with open(self.vocabrc, "w") as f:
            yaml.dump(vocabrc, f)
        print("You are now using {}.".format(colored(self.options["<name>"], "green")))

    def show_tones(self, s):
        s = s.lower()
        r = ""
        t = ""
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz? ':
                t += c
            else:
                if c in '1234':
                    tone = int(c)
                    m = re.search("[aoeiu\u00fc]+", t)
                    if len(m.group(0)) == 1:
                        t = t[:m.start(0)] + PINYIN_TONES[tone][PINYIN_TONES[0].index(m.group(0))] + t[m.end(0):]
                    else:
                        if 'a' in t:
                            t = t.replace("a", PINYIN_TONES[tone][0])
                        elif 'o' in t:
                            t = t.replace("o", PINYIN_TONES[tone][1])
                        elif 'e' in t:
                            t = t.replace("e", PINYIN_TONES[tone][2])
                        elif t.endswith("ui"):
                            t = t.replace("i", PINYIN_TONES[tone][3])
                        elif t.endswith("iu"):
                            t = t.replace("u", PINYIN_TONES[tone][4])
                        else:
                            t += "!"
                r += t
                t = ""
        r += t
        return r

    def run(self):
        raise NotImplementedError("You must implement the run() method yourself!")