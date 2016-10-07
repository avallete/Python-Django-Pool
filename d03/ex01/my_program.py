# -*- coding: utf-8 -*-

import path

def run():
    module_path = path.__file__[0:-7]
    d = path.Path("%s%s" % (module_path, "ex01"))
    f = path.Path("%s%s" % (module_path, "filetest"))
    d.makedirs_p()
    f.write_text("a little text test ! :)\n")
    with open(f.abspath(), 'r') as fd:
        print(fd.read())


if __name__ == '__main__':
    run()