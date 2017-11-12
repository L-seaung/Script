#!/usr/bin/env python
# -*- coding:utf-8 -*-
import crypt
import optparse
import threading



def cryptPass(cryptPassword, dictionary):
    salt = cryptPassword[0:2]
    dictFile = open(dictionary, 'r')

    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptpass = crypt.crypt(cryptPassword)
        if (cryptpass == cryptPassword):
            print('[+] found password : ' + word)
            return
        print('[-] not found password \n ' )
        return


def main():
    parser = optparse.OptionParser(
        'usage %prog -f <target password file name> -d <target dictionary file name>'
    )

    parser.add_option('-f', dest='fname', type='string', help='specify target password file name.')
    parser.add_option('-d', dest='dname', type='string', help='specify target dictionary file name.')

    (options, args) = parser.parse_args()

    if (options.fname == None | options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        fname = options.fname
        dname = options.dname
        passwordFile = open(fname, 'r')
        for line in passwordFile.readlines():
            if ':' in line:
                user = line.split(':')[0]
                password = line.split(':')[1].strip(' ')
                print('[*] Cracking password for : user')
                t = threading.Thread(target=cryptPass, args=(password, dname))
                t.start()

if __name__ == '__main__':
    main()


# def main():
#     passwordfile = open('password.txt', 'r')
#     for line in passwordfile.readlines():
#         if ':' in line:
#             user = line.split(':')[0]
#             password = line.split(':')[1].strip(' ')
#             print('[*] Cracking password for : user')
#             cryptPass(password)

# if __name__ == '__main__':
#     main()
