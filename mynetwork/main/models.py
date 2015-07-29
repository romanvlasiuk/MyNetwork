from django.db import models
from django.contrib.auth.models import User


class Publication(models.Model):
    owner = models.ForeignKey(User)
    article = models.CharField(max_length=100, blank=True)
    text = models.TextField(blank=True)

    def __unicode__(self):
        return "{0} '{1}'".format(self.owner.username, self.article)

User.publications = property(lambda u: Publication.objects.filter(owner=u))
User.pub_amount = property(lambda u: len(Publication.objects.filter(owner=u)))


class Comment(models.Model):
    publication = models.ForeignKey(Publication)
    author = models.ForeignKey(User)
    text = models.TextField(blank=True)
    time = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.author.username

Publication.comments = property(lambda u: Comment.objects.filter(publication=u))


class Photo (models.Model):
    owner = models.ForeignKey(User)
    image = models.ImageField()
    title = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return '{0} : {1}'.format(self.owner.username, self.title)

User.photos = property(lambda u: Photo.objects.filter(owner=u))


