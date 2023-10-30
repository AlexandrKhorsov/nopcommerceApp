import time
from selenium.webdriver.support.ui import Select
class AddCustomer():
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn bg-blue']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrator')]"
    lstitemRegistred_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrofVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_byxpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_byxpath(self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_byxpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_byxpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_byxpath(self.txtPassword_xpath).send_keys(password)

    def setCustomRoles(self,role):
        self.driver.find_element_byxpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
           self.listitem =  self.driver.find_element_byxpath(self.txtcustomerRoles_xpath).click()
        elif role == 'Administrators':
            self.listitem=self.driver.find_element_byxpath(self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element_byxpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_byxpath(self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_byxpath(self.lstitemRegistred_xpath)
        elif role =='Vendors':
            self.listitem = self.driver.find_element_byxpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_byxpath(self.lstitemGuests_xpath)
       #use below element if you can not click ome elements
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setGender(self, gender):
        if gender=='Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element_by_id(self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()


    def setFirstName(self, fname):
        self.driver.find_element_byxpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_byxpath(self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element_byxpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element_byxpath(self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self,content):
        self.driver.find_element_byxpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_byxpath(self.btnSave_xpath).click()