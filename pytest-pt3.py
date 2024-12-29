import pytest

@pytest.mark.login
def test_mylogin():
    print ('enter your logon credentials. ')
    print('open alnafi.com')
    print ('logon1')

@pytest.mark.task
def test_task():
    print ('task1')
    print('::::::::::::::::::::::MY TASK:::::::::::::::::::::::::')

@pytest.mark.data
def test_data():
    print('data')
    print('::::::::::::::::::::::MY DATA:::::::::::::::::::::::::')


# now do it using ini file and warning will not pop up

#create ini file extension and add code in it

@pytest.mark.skip
def test_skip():
    print('skip data example')
    print('skip example')
