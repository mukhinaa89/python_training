from model.contact import Contact


def test_modify_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(nickname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="Vasiliy"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(address="Moscow"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="Alibabaevich"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)