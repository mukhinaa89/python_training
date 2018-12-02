# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.create_contact(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd):
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("first")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("middle")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("last")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("nick")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("title")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("company")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("address1")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("7123714")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("123134")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("23423423")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("234234")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("email@email.ru")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("16")
        wd.find_element_by_xpath("//option[@value='16']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_xpath("//option[@value='January']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1989")
        # submit contact creation
        wd.find_element_by_xpath("//input[21]").click()

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
