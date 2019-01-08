from sys import maxsize
class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None,
                 company=None, address=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, fax=None, email=None, birth_day=None, birth_month=None, birth_year=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.fax = fax
        self.email = email
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) or (self.firstname == other.firstname and self.lastname == self.lastname)


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize