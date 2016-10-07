# -*- coding: utf-8 -*-

import antigravity
import sys

if __name__ == '__main__':
    if len(sys.argv) == 4:
        try:
            antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), bytes(sys.argv[3], 'UTF-8'))
        except Exception as e:
            print(e)
    else:
        print("Wront numbers of argument.\nExample of valid call: %s" % ("python3 geohashing.py 37.421542 -122.085589 2005-05-26-10458.68"))