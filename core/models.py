from django.db import models


class Effects(models.Model):
    draft = models.CharField(max_length=30)
    cause = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.draft


class Solutions(models.Model):
    draft = models.CharField(max_length=30)
    body = models.TextField()

    def __str__(self):
        return self.draft


class Info(models.Model):
    draft = models.CharField(max_length=30)
    body = models.TextField()

    def __str__(self):
        return self.draft


class ReadMore(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name




class Sources(models.Model):
    name = models.CharField(max_length=50)
    url = models.TextField()

    def __str__(self):
        return self.name