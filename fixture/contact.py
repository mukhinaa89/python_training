from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//input[21]").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value_contact("firstname", contact.firstname)
        self.change_field_value_contact("middlename", contact.middlename)
        self.change_field_value_contact("lastname", contact.lastname)
        self.change_field_value_contact("nickname", contact.nickname)
        self.change_field_value_contact("title", contact.title)
        # add Company's information
        self.change_field_value_contact("company", contact.company)
        self.change_field_value_contact("address", contact.address)
        # add Phones and Email
        self.change_field_value_contact("home", contact.homephone)
        self.change_field_value_contact("mobile", contact.mobilephone)
        self.change_field_value_contact("work", contact.workphone)
        self.change_field_value_contact("phone2", contact.secondaryphone)
        self.change_field_value_contact("fax", contact.fax)
        self.change_field_value_contact("email", contact.email)
        self.change_field_value_contact("email2", contact.email2)
        self.change_field_value_contact("email3", contact.email3)
        self.change_field_value_contact("address2", contact.address2)
        self.change_field_value_contact("notes", contact.notes)
        # add Date of birth
        self.change_field_value_contact("byear", contact.birth_year)


    def change_field_value_contact(self, field_firstname, text):
        wd = self.app.wd
        if text is not None:
            # add Name (first, middle,last) and Nickname
            wd.find_element_by_name(field_firstname).click()
            wd.find_element_by_name(field_firstname).clear()
            wd.find_element_by_name(field_firstname).send_keys(text)


    def delete_first_contact(self):
        self.delete_contact_by_index(0)


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        #select first contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None


    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None


    def modify_contact_by_id(self, contact, id):
        wd = self.app.wd
        self.open_home_page()
        self.open_contact_to_modify_by_id(id)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_contact_to_modify_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath(
            "//input[@id='%s']/parent::td/following-sibling::td[7]//img[@title='Edit']" % id).click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def modify_first_contact(self):
        self.modify_contact_by_index(0)


    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        self.open_modification_form(index)
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_modification_form(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add"))>0):
            wd.find_element_by_link_text("home").click()


    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = row.find_elements_by_css_selector("tr[td]")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails, address=address))
        return list(self.contact_cache)


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()



    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        address2 = wd.find_element_by_name("address2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone,  address=address, address2=address2,
                       email=email, email2=email2, email3=email3)


    def get_contact_from_view_page(self, index):
        def clear(s):
            return re.sub("[() -]", "", s)
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        try:
            homephone = re.search("H: (.*)", text).group(1)
        except AttributeError:
            homephone = ''
        try:
            workphone = re.search('W: (.*)', text).group(1)
        except AttributeError:
            workphone = ''
        try:
            mobilephone = re.search('M: (.*)', text).group(1)
        except AttributeError:
            mobilephone = ''
        try:
            secondaryphone = re.search("P: (.*)", text).group(1)
        except AttributeError:
            secondaryphone = ''
        cells = wd.find_elements_by_xpath("//div[@id='content']/a")
        cells = cells[:-1]
        return Contact(all_phones_from_home_page='\n'.join(filter(lambda x: x !='',
                                                                  map(lambda x: clear(x),
                                                                      filter(lambda x: x is not None,[homephone, mobilephone, workphone, secondaryphone])))),
                       all_emails_from_home_page='\n'.join(map(lambda x: x.text, cells)))
