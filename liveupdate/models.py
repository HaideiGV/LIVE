from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import now



class Update(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return "[ %s ] %s " % (
            self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            self.text
        )



class Contacts(models.Model):
    subject = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=False, default=datetime.now())
    email = models.EmailField(max_length=254)
    text = models.TextField(max_length=100)

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return str(self.text)


class Category(models.Model):
    category = models.CharField(max_length=200)
    class Meta:
        ordering = ['category']

    def __unicode__(self):
        return str(self.category)



class Links(models.Model):
    category = models.ForeignKey(Category)
    linkUrl = models.URLField(max_length=500, unique=True)
    rating = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    class Meta:
        ordering = ['linkUrl']

    def __unicode__(self):
        return str(self.linkUrl)


class LinkRateEvent(models.Model):
    link = models.ForeignKey(Links)
    user = models.ForeignKey(User)
    is_like = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_like']

    def __unicode__(self):
        return str(self.is_like)