import pytest
import time
from pageObject import LoginPage
from pageObject.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("**************** Test_003_AddCustomer **********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****************Login successful")
        self.logger.info("Starting add customer Test")

        self.addcust = AddCustomer(self.driver)  # created object AddCustomer is a class from AddCustomerPage
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("************* Providing customer info *******************")

        self.email = random_generator() + "@gmail.com"
        self.email.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomRoles("Guest")
        self.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Pavan")
        self.addcust.setLastName("Kumar")
        self.addcust.setDob("7/05/1985")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing...")
        self.addcust.clickOnSave()

        self.logger.info('*******Saving customer info*****')

        self.logger.info('********Add customer validation******')

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)

        if'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("***Add customer Test Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("*****Add customer Test Failed************")
            assert True == False
        self.driver.close()
        self.logger.info("***** Ending Home Title Test ********")

    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return  ''.join(random.choice(chars) for x in range(size))





