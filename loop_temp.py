#!/usr/bin/env python
import os
import sys

def main(argv):
    if (len(argv) == 1):
        print("Usage: " + os.path.basename(argv[0]) + " <filename/path>")
        sys.exit()
    else:
        if os.path.isfile(argv[1]): # if argument is a file
            with open(argv[1]) as f:
                for line in f:
                    print("Do something with " + line.strip())
        elif os.path.isdir(argv[1]):
            for filename in os.listdir(argv[1]): #if argument is a path
                    print("Do something with " + filename)
        else:
            print('Syntax error')
            sys.exit()

if __name__ == "__main__":
    main(sys.argv)

TODO = '''
        [ ] - Add recursive option

        '''