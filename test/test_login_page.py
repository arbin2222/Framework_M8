#Testcase1:-
# Open browser
# enter url
# enter valid login credentials:-
# username---> standard_user
# password---> secret_sauce
# click on login button
# expected result ---> navigate to inventory page



import pytest
from pages.login_page import LoginPage
from utilities.read_excel import get_valid_test_data
u,p=get_valid_test_data()
from time import sleep



@pytest.mark.order(1)
def test_valid_cred(driver):
    lp=LoginPage(driver)
    lp.enter_username(u)
    sleep(2)
    lp.enter_pwd(p)
    sleep(2)
    lp.click_login_btn()
    sleep(2)
    assert driver.current_url=='https://www.saucedemo.com/inventory.html',driver.save_screenshot('screenshot/invalid_cred.png')






# Testcase2:-
# Open browser
# enter url
# enter invalid login credentials:-
# username---> arbin
# password---> 123456
# click on login button
# expected result ---> same page


from utilities.read_excel import get_invalid_test_data
us,psd = get_invalid_test_data()



@pytest.mark.order(2)
def test_invalid_cred(driver):
    lp=LoginPage(driver)
    lp.enter_username(us)
    lp.enter_pwd(psd)
    lp.click_login_btn()
    sleep(3)

    assert driver.current_url=='https://www.saucedemo.com/',driver.save_screenshot('screenshots/test-case_2.png')




# Testcase3:-
# Open browser
# enter url
# enter invalid login credentials:-
# username---> arbin
# password---> secret_sauce
# click on login button
# expected result ---> same page




# Testcase4:-
# Open browser
# enter url
# enter invalid login credentials:-
# username--->  '      '
# password--->   '      '
# click on login button
# expected result ---> same page



































