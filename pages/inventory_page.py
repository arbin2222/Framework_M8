class InventoryPage:
    product_disp="xpath","//div[@class='inventory_item']"
    cart_icon="xpath","//a[@data-test='shopping-cart-link']"


    def __init__(self,driver):
        self.driver=driver


    def check_product_displayed(self):
        return self.driver.find_element(*InventoryPage.product_disp).is_displayed()



    def click_cart_icon(self):
        self.driver.find_element(*InventoryPage.cart_icon).click()