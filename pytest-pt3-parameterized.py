import pytest

# @pytest.mark.parametrize('username , password', [('am3030441@gmail.com' , 'abrar123') , ('samira@gmail.com' , 'samira123')])
# def test_parametrize(username , password):
#     print('logon details')
#     print('you are logging in now')
#     print(username, 'and' , password

# now use the above code using function

def func_cred():
    return [
        ('am3030441@gmail.com', 'abrar123'),
        ('samira@gmail.com', 'samira123')
    ]

@pytest.mark.parametrize('username , password' , func_cred())
def test_parametrize(username , password):
    print('logon details')
    print('you are logging in now')
    print(username, 'and' , password)

#use verifying title example now
#
# def test_verify_title():
#     expected_title = 'Al Nafi'
#     actual_title = 'Al Nafi'
#
#     # if actual_title == expected_title:
#     #     print('It is passed')
#     # else:
#     #     print('it is failed')
#
#     assert actual_title == expected_title