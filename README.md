# Setup

How to install prereqisite software and setup a python project with virtual environment, get python dependencies and get the shodan API key.

## Prerequisites
The setup will include: (will be very similar on all Unix style Operating Systems, i.e. NOT Windows)
- `Visual Studio Code` (or any text editor / IDE you are comfortable with)
- optional: Command line tool / Terminal e.g. `iTerm`
- optional: Package manager `brew`
- `python3`

### Setup Visual Studio Code
Download from here https://code.visualstudio.com/download

or 

```bash
brew install --cask visual-studio-code
```

Optional: Download the VS Code extensions `Python` and `Pylance` for a nicer experience.

### Ensure you can access a Terminal

Your System should come with its own Terminal application, for Mac I use `iTerm`: https://iterm2.com/

VS Code also has a Terminal tab you can use.

### Setup python

In a terminal, check if python 3.x is already installed:

```
python --version
python3 --version
python2.7 --version
...
```
If you still need python 3, download the latest version  from here: https://www.python.org/downloads/

or

```bash
brew install python3 
```

## Project setup
Now we will:
- create a project folder and open it in VS Code
- install and activate a python virtual environment
- install necessary python libraries
- get the shodan API key

### Create project folder

Create the project `python_shodan` folder somewhere that fits you. Also create the file `shodan_demo.py`. Open the folder in VS Code.

or 

```bash
cd to/where/you/want/the/project
mkdir python_shodan
touch shodan_demo.py
code shodan_demo.py # If you have set the alias `code` for VS Code
```

### Install and activate a virtual python environment

This is not necessary, but it will simplify python package management. So I would recommend to do this. If you don't want to you can leave out this step and install the python packages directly, i.e. globally for your computer and not just this particular virtual environment.

Essentially we will be following this guide. Go to the link and Click on "Windows" for more information on that. We will be doing it for Unix systems.
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

1. Install the python package manager `pip` in a Terminal:
```bash
python3 -m pip install --user --upgrade pip
```

2. Install virtualenv for python:
```bash
python3 -m pip install --user virtualenv
```

3. Ensure you are in the directory with `shodan_demo.py` and create a virtualenv:
```bash
ls -a # Returns: ".    ..   shodan_demo.py"
python3 -m venv ".venv"
ls # Returns: ".    ..   .venv    shodan_demo.py"
```

4. Activate the virtual environment (VS Code will usually do it for you)
```bash
source .venv/bin/activate
```

### Install python packages

If you have installed and activated a python virtual envirment, check if is active before proceeding:

```bash
which python3 # Should return a path to `.venv/bin/python`
```

Install the packages `shodan`,`pandas` and `numpy`:
```bash
python3 -m pip install shodan numpy
```

### Shodan API key
Get you API key from https://account.shodan.io/

Be sure to register with an academic email for free credits: https://help.shodan.io/the-basics/academic-upgrade

