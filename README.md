# Pytest Practise

## Introduction
- This is my repo for Makers Module 2 - Golden Square: Testing Bites
- It contains practise code for learning how to use pytest
  
## Objectives
I used this project to learn how to:
- [x] Test functions using pytest
- [x] Test classes with equality using pytest
- [x] Learn to test for errors using pytest

## Setup
This project uses `pipenv`. Here's how to install it:

```shell
; python3 -m ensurepip --upgrade
; pip3 install --user pipenv
; echo 'export PATH="$PATH:$(python3 -m site --user-base)/bin" # Add Pipenv to PATH' >> ~/.zshrc
; source ~/.zshrc
; pipenv --version
pipenv, version ...
```
To test the practise code: 
```shell
# cd into the relevant directory:
; cd 1_testing_functions # Practise code for testing functions
; cd 2_testing_classes # Practise code for testing classes
; cd 2_testing_for_errors # Practise code for testing errors

# This will install the dependencies (pytest)
; pipenv install # NB: you may need to change interpreters 

# This will activate the project's virtualenv
; pipenv shell

# This will run all of the tests
; pytest

# This will exit the pipenv shell
; exit # or Ctrl-D
```