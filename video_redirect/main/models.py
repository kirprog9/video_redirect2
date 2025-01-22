from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.pk

class Video(models.Model):
    video_url = models.URLField(unique=True)

    def __str__(self):
        return self.video_url

class RedirectSite(models.Model):
    destination_url = models.URLField()

    def __str__(self):
        return self.destination_url
