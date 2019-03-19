from BasePage import BasePage

class TwitterMainPage(BasePage):

    def click_signup_button(self):
        self.driver = BasePage
        button_sign_up = self.driver.find_element_by_xpath("//div[@class='StaticLoggedOutHomePage-buttons']/a[contains(text(),'Sign up')]")
        button_sign_up.click()