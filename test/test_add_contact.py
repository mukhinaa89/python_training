# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="first", middlename="middle", lastname="last", nickname="nick", title="title", company="company", address="address1", home_phone="7123714", mobile_phone="123134",
                               work_phone="23423423", fax="234234", email="email@email.ru", birth_day="16", birth_month="January", birth_year="1989"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home_phone="", mobile_phone="",
                               work_phone="", fax="", email="", birth_day="", birth_month="-", birth_year=""))
    app.session.logout()
