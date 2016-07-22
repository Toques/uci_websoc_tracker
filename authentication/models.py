from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User)
    phone_number = models.CharField(blank = True,max_length = 11)
    class Meta:
        permissions = (
            ('can_view', 'Can View'),
            ('can_modify', 'Can Modify'),
        )
    def __str__(self):
        return self.user.username