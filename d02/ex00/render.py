# -*- coding: utf-8 -*-

import sys
import re
import settings

def get_template(filename):
    try:
        with open(filename, 'r') as fd:
            template = fd.read()
        return template
    except IOError:
        print("Error opening %s" % filename)
        return None

def write_in_file(filename, data):
    try:
        with open(filename, 'w') as fd:
            fd.write(data)
    except IOError:
        print("Error writing %s" % filename)

def run(filename):
    template = get_template(filename)
    if template:
        data_dict = vars(settings)
        try:
            filled_template = template.format(**data_dict)
            write_in_file("%s%s" % (filename[0:-9], ".html"), filled_template)
        except KeyError:
            print("Error, cannot fill the template %s" % filename)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if re.search('\.template$', sys.argv[1]) is not None:
            run(sys.argv[1])
        else:
            print("Your file must be a .template file.")