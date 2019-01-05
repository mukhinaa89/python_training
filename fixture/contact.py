from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add"))>0):
            wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//input[21]").click()
        wd.find_element_by_link_text("home page").click()

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
        self.change_field_value_contact("home", contact.home_phone)
        self.change_field_value_contact("mobile", contact.mobile_phone)
        self.change_field_value_contact("work", contact.work_phone)
        self.change_field_value_contact("fax", contact.fax)
        self.change_field_value_contact("email", contact.email)
        self.change_field_value_contact("home", contact.home_phone)
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
        wd = self.app.wd
        self.open_home_page()
        #select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_link_text("home").click()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()


    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add"))>0):
            wd.find_element_by_link_text("home").click()


    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("tr[name=entry]"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=text, id=id))
        return contacts