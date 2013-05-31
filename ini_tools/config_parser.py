from ConfigParser import *
from StringIO import StringIO


class WZConfigParser(ConfigParser):
    """
    Extended ConfigParser
    Add handling space comments started from spaces.
    Save ini files on ini :)
    """
    header = None

    def optionxform(self, optionstr):
        """default emplementation makes it lowercase"""
        return optionstr

    # def pre_read(self):
    def load(self, path):
        with open(path) as f:
            lines = f.readlines()
        is_header = True
        self.header = []
        new_lines = []
        for original_line in lines:
            line = original_line.strip()
            if line:

                if is_header:
                    if line.startswith(';'):
                        self.header.append(original_line)
                    else:
                        is_header = False
                new_lines.append(line)

        fp = StringIO('\n'.join(new_lines))
        self.readfp(fp)

    def save(self, fp):
        if self.header:
            for line in self.header:
                fp.write(line)
            fp.write('\n')
        self.write(fp)