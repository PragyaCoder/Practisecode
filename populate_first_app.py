import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()


## FAKE POP SCRIPT
import random
from first_app.models import Topic,AccessRecord,Webpage,User
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    
    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        # create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_full_name = fakegen.name().split()
        fake_fn = fake_full_name[0]
        fake_ln = fake_full_name[1]
        fake_email = fakegen.email()

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic = top,url = fake_url, name = fake_name)[0]

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name = webpg,date = fake_date)[0]

        # create a fake user record for that user model
        user = User.objects.get_or_create(first_name = fake_fn,last_name = fake_ln, email = fake_email)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")