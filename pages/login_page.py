class LoginPage:
    un="id","user-name"
    pwd="id","password"
    login_btn="id","login-button"

    def __init__(self,driver):
        self.driver=driver


    def enter_username(self,username):
        self.driver.find_element(*LoginPage.un).send_keys(username)


    def enter_pwd(self,password):
        self.driver.find_element(*LoginPage.pwd).send_keys(password)



    def click_login_btn(self):
        self.driver.find_element(*LoginPage.login_btn).click()



