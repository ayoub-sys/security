#! /usr/bin/env python3
import subprocess
from termcolor import colored


def change_mac_address(interface,mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])

def main():
    interface=str(input("[*] Enter Interface To Change TO Mac"))
    new_mac_address=input("[*] Enter New Mac Adress")
    before_change=subprocess.check_output(["ifconfig",interface])
    change_mac_address(interface,new_mac_address)
    after_change=subprocess.check_output(["ifconfig",interface])
    if before_change==after_change:
        print(colored("[!!] Failed To Change Mac Address","red"))
    else:
        print(colored("[+] Mac Address Changed To "+new_mac_address+" On_interface: "+interface,"green"))

main()


