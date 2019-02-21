import re
from model.contact import Contact


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test_firstname'
                                   # , lastname='test_lastname',
                                   # address='test_address', all_emails_from_home_page='eemail\neemail2\neemail3',
                                   # all_phones_from_home_page='12345\n(123)45\n5432 1-\n333333'))
                                   ))
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    # assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    # assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    # assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    # assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))
