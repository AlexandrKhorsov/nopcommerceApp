import time

import pytest
from selenium import webdriver
from pageObject import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("*******************Test_002_DDT_Login********************")
        self.logger.info("*******************Verify Login DDT test********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)


        self.rows=XLUtils.getRawCount(self.path,'Sheet1')

        lst_status = []  #Empty list variable

        for r in range(2,self.rows+1):
            XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1', r,3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"



            if act_title == exp_title:
                if self.exp=="Pass":
                    self.logger.info("*** Passed")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("*** failed")
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("*****failed*****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("******* passed ******")
                    lst_status.append("Pass")

            if "Fail" not in lst_status:
                self.logger.info("Login DDT test passed......")
                self.driver.close()
                assert True
            else:
                self.logger.info("**** Login DDT test failed ******")
                self.driver.close()
                assert False

            self.logger.info("******* End of Login DDT Test")
            self.logger.info("*********Completed TC_LoginDTT_002 ********************")

