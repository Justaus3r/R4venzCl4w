[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



##
# R4venzCl4w (◣_◢)ノ-=≡≡卍
A modular Framework for **Pentesters** and **Bug Hunters** written in Python3.

### 🔧 Technologies & Tools

![](https://img.shields.io/badge/OS-Linux-informational?style=flat-square&logo=ubuntu&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Editor-VS_Code-informational?style=flat-square&logo=visual-studio&logoColor=white&color=5194f0)
![](https://img.shields.io/badge/Language-python-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Python_Version-3.10-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)

##

### 📚 Requirements
> - Python 3.9+
> - pip3

### Features
- Quick and easy to use
- Modular Framework
- Enumerate IP(Dns, Whois, Port Scanning, Blacklist Checker, Ping, Traceroute, Geolocation) etc.
- Scans Host using `Shodan's API` 

> `Note:` Please keep in mind that the tool is still in development and more features will be added soon.
#

## Table of Contents
- [R4venzCl4w (◣_◢)ノ-=≡≡卍](#r4venzcl4w-ノ-)
    - [Installation](#installation)
    - [Config](#config)
    - [Usage](#usage)
        - [Options](#options)
        - [Example](#example)
    - [Todo](#todo)
    - [Contributing](#contributing)
    - [License](#license)

 ### Features Implementation
* IP Enumeration
    - [x] Dns Lookup
    - [x] Reverse Dns Lookup
    - [x] Whois
    - [x] Port Scanning
    - [x] Blacklist Checker     ( [**dfirsec's**](https://github.com/dfirsec) Tool --> [check_rep](https://github.com/dfirsec/check_rep) )
    - [x] Ping
    - [x] Trace
    - [x] GeoLocation
    - [x] Shodan                (Scans Host on Shodan using Shodan's API: `API key Required`)
- Domain Enumeration
    - [ ] Going to be implemented in **ver: 1.3.0**
    > `Current version: 1.2.0` -   **Stable**
#
##

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.
if not installed, install it using the following command.
```bash
sudo apt-get install python3-pip
```

> It is advised to install the python requirements in a virtual environment, for that install the venv package.

```bash
    python3 -m pip install venv
    python3 -m venv env
    source env/bin/activate
```

After that run the following commands:
```bash
    sudo apt-get install traceroute     # For Debian based distros
    python3 -m pip install -r requirements.txt
```
#

## Config
> `Shodan`  module uses the Shodan's API so make sure you have `.configx` file in your folder. If the `.configx` file is not there you can create it with the following Data:
```bash
% Config File for R4wenzCl4w


# Global Settings
# Global Variables are defined here. These variables can be used in any of the other sections.
$ GLOBAL_VAR: <Global Variable Here>



# Environment Variables
# Shodan API Key Example --> SHODAN_API_KEY:gA**************************
- SHODAN_API_KEY:<API Key Here>
```
#

## Usage

```bash
python3 main.py -i [IP Address]
```

#### Options

```bash
        -i              IP Address to Enumerate
        -d              Domain to Enumerate  # Going to be implemented in **ver: 1.3.0**
        -h              Help Menu
```

##

#### Example
```bash
1) python3 main.py -i 1.1.1.1
2) python3 main.py -i 8.8.8.8
```
#

## Todo
- [x] To add More Modules
- [ ] Optimize the Workflow
- [ ] Implement Domain Enumeration
- [ ] Saving results in json, text Format

#


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)