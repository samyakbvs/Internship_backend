from django.db import models

# Create your models here.

class Post(models.Model):
    Name = models.CharField(max_length = 264)
    Init_time = models.DateTimeField()
    Description = models.TextField()
    Author = models.CharField(max_length = 264)
    Image = models.FileField(blank=True)
    Video = models.FileField(blank=True)
    Doc = models.FileField(blank=True)

    def __str__(self):
        return self.Name
