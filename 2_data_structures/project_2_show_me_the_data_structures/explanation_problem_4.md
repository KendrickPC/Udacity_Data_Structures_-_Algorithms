# Active Directory

My is_user_in_group function checks the base case first. 

If the user is in group, a recursive search if done for subgroups
and results are returned as True or False.

### Function Efficiency

is_user_in_group function has a runtime of O(m * n): m is the number
of users and n represents the number of groups.
The runtime is O(m * n), where m is the number of users and n the number of groups. 

In a worst case scenario, all groups and users will need to be
checked. A stack overhead occurs because of recursion.

My space complexity is  O(m * n), due to recursively calling
my stack with user and group as parameters.
