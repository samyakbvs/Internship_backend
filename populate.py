import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','internship.settings')

import django
django.setup()

import random
from lms.models.post_models import Post
from faker import Faker

fake = Faker()

Titles = ['Java','C++','Python','Postrges','Deployment','Cricket','SAT','ACT','Essays','College','Career']

for i in range(100):
    post = Post(Name=Titles[random.randint(0,10)],Description=fake.sentence(nb_words=100),Author=fake.name())
    post.save()

# class Post(models.Model):
#     Name = models.CharField(max_length = 264)
#     Init_time = models.DateTimeField()
#     Description = models.TextField()
#     Author = models.CharField(max_length = 264)
#     Image = models.FileField(blank=True)
#     Video = models.FileField(blank=True)
#     Doc = models.FileField(blank=True)
#
#     def __str__(self):
#         return self.Name
