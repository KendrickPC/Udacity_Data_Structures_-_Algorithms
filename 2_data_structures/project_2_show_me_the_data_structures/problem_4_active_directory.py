# Active Directory
'''
In Windows Active Directory, a group can consist of user(s) and
group(s) themselves. We can construct this hierarchy as such.
Where User is represented by str representing their ids.
'''


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


# Write a function that provides an efficient look up of
# whether the user is in a group.

def is_user_in_group(user, group):    
    # Base case checking is user or group is None.
    if user is None or group is None:
        return False
    
    for group_user in group.get_users():
        if group_user == user:
            return True

    for sub_group in group.get_groups():
        return is_user_in_group(user, sub_group)

    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
# Adding fake_user seeing if False if returned
fake_user = "John Doe"
parent.add_user(fake_user)

print(is_user_in_group(fake_user, None))
print(is_user_in_group(None, parent))
print(is_user_in_group(sub_child_user, parent))
print(is_user_in_group(sub_child_user, sub_child))
print(is_user_in_group(fake_user, sub_child))

'''
<<< False
<<< True
<<< True
<<< False
<<< False
'''
