# django_project
This project aims to create django project for regression testing.

#TODO move it to documentation
issues:

1) Missing table:
(django.db.utils.OperationalError: no such table: e.g. 'regression_category')
python manage.py migrate --run-syncdb

Create a new user in django

from django.contrib.auth.models import User

user = User.objects.create_user('john', 'email@email.com', '123')

user.save()


=======

Prerequisites:
- Installed and configured virtualenv
- python3 and pip3


Installation instructions:

1) Clone project into your local disk.
2) Activate virtualenv 'workon <project's name>'
3) Run 'pip install -r requirements.txt'



