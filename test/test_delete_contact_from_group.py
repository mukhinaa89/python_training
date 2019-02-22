from model.group import Group
from model.contact import Contact
import random
from fixture.orm import ORMFixture


def test_delete_contact_to_group(app,orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(orm.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="firstNaMe", lastname="LaStNaMe", nickname="nicNAME", title="tItLe"))
    all_groups = orm.get_group_list()
    group = random.choice(all_groups)
    all_contacts_in_group = orm.get_contacts_in_group(group)
    if len(all_contacts_in_group) == 0:
        all_contacts_in_group = orm.get_contacts_in_group(group)
        all_contacts_not_in_group = orm.get_contacts_not_in_group(group)
        if len(all_contacts_not_in_group) == 0:
            app.contact.add(Contact(firstname="firstNaMe", lastname="LaStNaMe", nickname="nicNAME", title="tItLe"))
            all_contacts_not_in_group = orm.get_contacts_not_in_group()
        contact = random.choice(all_contacts_not_in_group)
        app.contact.add_contact_to_group(group.id, contact)
        all_contacts_in_group.append(contact)
        assert sorted(orm.get_contacts_in_group(group), key=Group.id_or_max) == sorted(all_contacts_in_group,
                                                                                      key=Group.id_or_max)
        all_contacts_in_group = orm.get_contacts_in_group(group)
    contact = random.choice(all_contacts_in_group)
    app.contact.delete_contact_from_group(group.id, contact)
    all_contacts_in_group.remove(contact)
    assert sorted(orm.get_contacts_in_group(group), key=Group.id_or_max) == sorted(all_contacts_in_group, key=Group.id_or_max)


