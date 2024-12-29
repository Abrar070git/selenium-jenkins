import pytest

def setup_function(function):   #for starting
    print (':::::::::::::::starting browser::::::::::::::::::::')

def teardown_function():
    print('::::::::::::::::ending browser::::::::::::::::::::::')

def test_mylogin():
    print ('testing mylogin1. ')
    print('testing mylogin1. ')
    print('my logon page1. ')

def test_mylogin1():
    print ('testing mylogin2. ')
    print('testing mylogin2. ')
    print ('my logon page2')