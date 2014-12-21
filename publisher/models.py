from django.db import models

# Create your models here.
class publishers(models.Model):

    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, null=True, unique=True)
    gplus_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    fb_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return self.email