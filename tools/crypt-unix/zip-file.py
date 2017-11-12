#!/usr/bin/env python
# -*- coding:utf-8 -*-
import zipfile
import optparse
import threading


def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print('[+] Found password' + password + '\n')
    except:
        return


def main():
    parser = optparse.OptionParser(
        'usage%prog -f <zipfile> -d <dictionary>'
    )
    parser.add_option('-f', dest='fname', type='string', help='specify zip file name.')
    parser.add_option('-d', dest='dname', type='int', help='specify dictionary file.')

    (options, args) = parser.parse_args()
    if (options.fname == None | options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        fname = options.fname
        dname = options.dname
    zipfile = zipfile.ZipFile(fname)
    passFile = open('password.txt', 'r')

    for line in passFile.readlines():
        password = line.strip('\n')
        t = threading.Thread(target=extractFile, args=(zipfile, password))
        t.start()

if __name__ == '__main__':
    main()
