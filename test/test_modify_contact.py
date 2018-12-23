from model.contact import Contact


def test_modify_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(nickname="test"))
    app.contact.modify_first_contact(Contact(firstname="Vasiliy"))


def test_modify_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(address="Moscow"))
    app.contact.modify_first_contact(Contact(lastname="Alibabaevich"))