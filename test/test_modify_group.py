from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(header="test322"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_new = Group(name="New grouPPP")
    app.group.modify_group_by_id(group.id, group_new)
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i].id == group_new.id:
            old_groups[i] = group_new
    assert len(old_groups) == len(new_groups)
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    if check_ui:
        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                             key=Group.id_or_max)
