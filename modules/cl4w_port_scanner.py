#!/usr/bin/env python3
#~*- coding: utf-8 -*-
from rich.console import Console
from subprocess import call, check_output
from os import path, system
from os import name as  nm
from sys import exit
from shutil import which
from shlex import split as sp
from os import getcwd


console = Console()
linux_bin_url = "https://github.com/sc4rfurry/nimd4-ng/releases/download/v1.0/nimd4_linux_amd64"
win64_bin_url = "https://github.com/sc4rfurry/nimd4-ng/releases/download/v1.0/nimd4_win64.exe"
wget__path = which("wget")
chmod_path = which("chmod")
os = nm
wd = getcwd()
if os == "nt":
    bin_path = path.join(wd, "core", "bin", "nimd4_win64.exe")
else:
    bin_path = path.join(wd, "core", "bin", "nimd4_linux_amd64")



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





class PortScanner:
    def __init__(self, host):
        self.host = host
        self.port_range = input(f"{bcolors.OKGREEN}[+]{bcolors.ENDC} Enter port range to scan (ex: 1-1000): ")
        while True:
            if self.port_range == "":
                self.port_range = input(f"{bcolors.OKGREEN}[+]{bcolors.ENDC} Enter port range to scan (ex: 1-1000): ")
            else:
                break


    def task_description(self):
        return "Port Scanner"


    def get_port_status(self):
        try:
            print('\n')
            if path.exists(bin_path) and path.isfile(bin_path):
                if os == "nt":
                    cmd = f"{bin_path} -t {self.host} -r {self.port_range}"
                    system(cmd)
                else:
                    cmd = f"/usr/bin/chmod +x {bin_path}"
                    cmd = sp(cmd)
                    check_output(cmd)
                    cmd = f"{bin_path} -t {self.host} -r {self.port_range}"
                    cmd = sp(cmd)
                    call(cmd)
            else:
                console.print(f"""[~] Nimd4 not found, downloading...
        [cyan bold]- Linux Binary:[/cyan bold]\t\t{linux_bin_url}
        [cyan bold]- Windows Binary:[/cyan bold]\t{linux_bin_url}""", style="bold red")
        except Exception:
            console.print_exception(show_locals=True)
        except KeyboardInterrupt:
            console.print("[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)