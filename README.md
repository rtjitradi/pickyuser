# pickyuser
Custom User - Implementing your own login &amp; signup page without the defaults for the server

There are two ways to extend users in Django: the "profile" method and a custom user. We've already used the profile method for our first project, so now we'll cover the custom user.

This project is simply about implementing a custom user from the ground up so that you can use it in the next assignment.

Your Task
Implement your own login and signup page (don't use the defaults) for the server that leads to a locked-down "homepage". The homepage should show:

the username of the person who is logged in
the display name of the person who is logged in
the output the value of `settings.AUTH_USER_MODEL`
NOTE: DO NOT name any part of your app "user" -- it will have conflict with the built-in user model and give you all sorts of errors that are really difficult to debug if you don't know what you're looking for. Use "custom_user", "myuser", "dudewheresmyuser"... literally anything but "user" will work.

Extra Credit (2 points)

Extend your custom user field so that it has the following nullable fields:

Homepage (URLField)
Age (IntegerField)
Extra Credit (1 point)

(this is the hard part) Make the custom fields appear on the admin panel and available for editing.

Extra Credit (1 point)

1 additional bonus point if you make the superuser command ask for their age.

Submission
Submit a link to your repo

https://github.com/<github_username>/<repo_name>
Rubric
West Coast Custom Users
West Coast Custom Users
Criteria	Ratings	Pts
This criterion is linked to a Learning OutcomeThe homepage displays the username & display name of currently logged-in user
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
This criterion is linked to a Learning OutcomeImplements functional custom user model
5.0 pts
Full Marks
0.0 pts
No Marks
5.0 pts
This criterion is linked to a Learning OutcomeRepo contains pyproject.toml that includes all necessary dependencies to run application
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeThe homepage displays the output value of settings. AUTH_USER_MODEL
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
This criterion is linked to a Learning OutcomeEC (2 pts)
view longer description
0.0 pts
Full Marks
0.0 pts
No Marks
0.0 pts
This criterion is linked to a Learning OutcomeEC (1 pt)
view longer description
0.0 pts
Full Marks
0.0 pts
No Marks
0.0 pts
This criterion is linked to a Learning OutcomeEC (1 pt)
view longer description
0.0 pts
Full Marks
0.0 pts
No Marks
0.0 pts
Total Points: 10.0
