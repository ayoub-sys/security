#! /usr/bin/env python3
import crypt
from termcolor import colored


def crackPass(cryptword):
    salt=cryptword[0:2]
    dictionary=open("dictionary.txt","r")
    for word in dictionary.readlines():
        word=word.strip("\n")
        cryptPass=crypt.crypt(word,salt)
        if (cryptPass==cryptword):
            print(colored("[+] Found Password: "+word,"green"))
            return 
    print(colored("[-] Password Not Found!!","red"))
    return

def main():
    passFile=open("pass1.txt","r")
    for line in passFile:
        if ":" in  line:
            user=line.split(":")[0]
            cryptword=line.split(":")[1].strip(" ").strip("\n")
            print ("[*] Cracking The Password For User: "+user)
            crackPass(cryptword)



main()