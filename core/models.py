from django.db import models

class Hero(models.Model):
    image_url = models.URLField()
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    about = models.TextField(default="hello");

    def __str__(self):
        return self.name
    
class Media(models.Model):
    linkedIn_url = models.URLField(max_length=200, unique=True)
    gitHub_url = models.URLField(max_length=200, unique=True)
    email = models.CharField(max_length=200, default='favourokerri767@gmial.com')

    def __str__(self):
        return self.linkedIn_url

class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tools(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    github_link = models.URLField(max_length=200)
    demo_link = models.URLField(max_length=200)
    video_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Certifications(models.Model):
    image_url = models.URLField(max_length=200)
    description = models.CharField(max_length=255)


    def __str__(self):
        return self.description

