from model.contact import Contact
import random


def test_modify_first_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", lastname="test", nickname="test", title="title"))
    old_contacts = db.get_contact_list()
    contact_new = Contact(firstname="sdf123", lastname="dsfsfw2234", nickname="dsffff2342", title="12312asd")
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact_new, contact.id)
    new_contacts = db.get_contact_list()
    for i in range(len(old_contacts)):
        if old_contacts[i].id == contact_new.id:
            old_contacts[i] = contact_new
    assert len(old_contacts) == len(new_contacts)
    def clean(contact):
        return Contact(id=contact.id, lastname=contact.lastname.strip(), firstname=contact.firstname.strip())
    if check_ui:
        assert sorted(map(clean, new_contacts), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# def test_modify_last_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(address="Moscow"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(lastname="Alibabaevich"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)