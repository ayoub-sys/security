#! /usr/bin/env python3
from termcolor import colored
import hashlib



def tryopen(wordlist):
    global pass_file
    try:
        pass_file=open(wordlist,"r")
    except:
        print("[!!] No Such File At That Path")
        quit()

pass_hash=input("[*] Enter MD5 Hash Value:")
wordlist=input("[*] Enter Path To The Password File:")
tryopen(wordlist)

for word in pass_file:
    print(colored("[-] Trying " +word.strip('\n'), "red"))
    enc_wrd=word.encode("utf-8")
    md5digest=hashlib.md5(enc_wrd.strip()).hexdigest()
    if md5digest==pass_hash:
        print(colored("[+] Password Found:"+ word ,"green"))
        exit(0)
print("[!!] Password  Not In List !")