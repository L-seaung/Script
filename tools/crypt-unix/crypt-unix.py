#!/usr/bin/env python
# -*- coding:utf-8 -*-
import crypt
import optparse
import threading


def cryptPass(cryptPassword):
    salt = cryptPassword[0:2]
    dictFile = open('dictionary.txt', 'r')

    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptpass = crypt.crypt(cryptPassword)
        if (cryptpass == cryptPassword):
            print('[+] found password : ' + word)
            return
        print('[-] not found password \n ' )
        return

def main():
    passwordfile = open('password.txt', 'r')
    for line in passwordfile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            password = line.split(':')[1].strip(' ')
            print('[*] Cracking password for : user')
            cryptPass(password)

if __name__ == '__main__':
    main()
