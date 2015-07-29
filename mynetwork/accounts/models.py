from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    birthday = models.DateField(blank=True, null=True)
    about = models.TextField(blank=True)
    photo = models.ImageField(blank=True)

    def __unicode__(self):
        return self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

