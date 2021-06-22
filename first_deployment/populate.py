
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MAIN.settings')

import django
django.setup()

from App import models

from django.contrib.auth.models import User

from faker import Faker
fakegen=Faker()

def populate(N=1000):

    for i in range(N):

        fakeuser=fakegen.unique.user_name()
        fakeemail=fakegen.unique.email()

        acc=User.objects.get_or_create(username=fakeuser, email=fakeemail)

if __name__=='__main__':
    print('starting')
    populate()
    print('done')
