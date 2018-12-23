from model.contact import Contact


def test_modify_first_name(app):
    app.contact.modify_first_contact(Contact(firstname="Vasiliy"))


def test_modify_last_name(app):
    app.contact.modify_first_contact(Contact(lastname="Alibabaevich"))