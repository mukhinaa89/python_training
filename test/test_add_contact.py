# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="first", middlename="middle", lastname="last", nickname="nick", title="title", company="company",
                      address="address1", address2="address2", homephone="7123714", mobilephone="123134",
                      workphone="23423423", fax="234234", email="email@email.ru",email2="email2@email.ru", email3="email3@email.ru",
                      birth_day="16", birth_month="January", birth_year="1989", secondaryphone="1001", notes="NoteS")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home_phone="", mobile_phone="",
#                                 work_phone="", fax="", email="", birth_day="", birth_month="-", birth_year="")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
