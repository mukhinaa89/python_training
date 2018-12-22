# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="first", middlename="middle", lastname="last", nickname="nick", title="title", company="company", address="address1", home_phone="7123714", mobile_phone="123134",
                               work_phone="23423423", fax="234234", email="email@email.ru", birth_day="16", birth_month="January", birth_year="1989"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home_phone="", mobile_phone="",
                               work_phone="", fax="", email="", birth_day="", birth_month="-", birth_year=""))
