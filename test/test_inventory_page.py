#open browser
#login
#products are visible or not
#expected result----------------> products should be visible


from pages.login_page import LoginPage
from utilities.read_excel import get_valid_test_data
u,p = get_valid_test_data()
from pages.inventory_page import InventoryPage
from time import sleep
import pytest


@pytest.mark.order(3)
def test_products_visibility(driver):
    lp=LoginPage(driver)
    lp.enter_username(u)
    lp.enter_pwd(p)
    lp.click_login_btn()
    sleep(3)
    In=InventoryPage(driver)
    assert In.check_product_displayed()==True,driver.save_screenshot("screenshots/products_not_displayed.png")
    sleep(3)









#open browser
#login
#click cart icon
#expected result----------------> cart page should be visible



@pytest.mark.order(4)
def test_verify_cartpage(driver):
    lp1=LoginPage(driver)
    lp1.enter_username(u)
    lp1.enter_pwd(p)
    lp1.click_login_btn()
    sleep(3)
    In1=InventoryPage(driver)
    In1.click_cart_icon()
    sleep(2)
    assert driver.current_url=='https://www.saucedemo.com/cart.html',driver.save_screenshot("screenshots/cart_page_not_opened.png")
    sleep(2)









