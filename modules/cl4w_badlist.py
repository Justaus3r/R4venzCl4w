#!/usr/bin/env python3
# ~*- coding: utf-8 -*-
from subprocess import call, PIPE
from shlex import split
from os import name, system
from shutil import which
from os import path, getcwd


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKCYAN = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
        self.BOLD = ''
        self.UNDERLINE = ''


os = name
pw = getcwd()
if os == "nt":
    python3_path = which("python").lower()
else:
    python3_path = which("python3")
if os == "nt":
    check_rep_path = str(pw) + "\\core\\misc\\check_rep\\check_rep.py"
else:
    check_rep_path = str(pw) + "/core/misc/check_rep/check_rep.py"



class BadList:
    def __init__(self, ip):
        self.ip = ip

    def bl__check__(self):
        try:
            print("\n", f"{bcolors.OKCYAN}={bcolors.ENDC}" * 120)
            print(f"\n\t\t\t{bcolors.OKCYAN}[+]{bcolors.ENDC} {bcolors.OKBLUE}Checking IP: {bcolors.OKGREEN}{bcolors.UNDERLINE}{self.ip}{bcolors.ENDC} {bcolors.ENDC}")
            cmd = python3_path + " " + check_rep_path + " " + "-q" + " " + self.ip
            if os == "nt":
                system(cmd)
            else:
                cmd = split(cmd)
                call(cmd)
        except Exception as e:
            print(f"{bcolors.FAIL}Error: {e} {bcolors.ENDC}")
        