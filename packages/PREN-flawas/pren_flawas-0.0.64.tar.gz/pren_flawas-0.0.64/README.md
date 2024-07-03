# PREN Python Module


## Intention
This module uses various helper functions to manage the tasks from the PREN module at HSLU Lucerne. 
It is a Python module that can be accessed via the PyPi public repository.  

## Installation
### Create virtual environment
If no virtual environment is existing run the following code to create a new virtual 
environment in your folder. 
```bash
python -m env
```
Afterwards the activation of the virtual environment is needed to start the virtual environment. 
This is done with the following command: 
```bash
source env/bin/activate
```
To finish the setup we need to install the following modules:
```bash
pip install RPi.GPIO
pip install PREN-flawas
```
We are now able to use the module with the following command
```bash
from PREN_flawas import Engine, Display
```

## Author
[@flawas](https://github.com/flawas)
