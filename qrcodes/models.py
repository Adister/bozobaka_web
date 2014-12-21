from django.db import models

from users.models import users
from publisher.models import publishers

class qr_code(models.Model):
    
    id = models.AutoField(primary_key=True)
    publisher_id = models.ForeignKey(publishers)
    qr_code_generated = models.CharField(max_length=244, null=False, blank=False, unique=True)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False, null=False, blank=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True, null=False, blank=False)
    width = models.IntegerField(default=100)
    height = models.IntegerField(default=100)
    url = models.URLField(max_length=244,null=False, blank=False)
    label = models.CharField(max_length=244, blank=True, null=True)
    response_text = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.qr_code_generated

## Hold default values of all types of qr codes
class usage(models.Model):

    id = models.AutoField(primary_key=True)
    qr_code_id = models.ForeignKey(qr_code)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=True, null=False, blank=False)
    user_id = models.ForeignKey(users)
    os = models.CharField(max_length=244, blank=True, null=True)
    location = models.CharField(max_length=244, blank=True, null=True)
    type = models.IntegerField(null=True, blank=True)

class download(models.Model):

    id = models.AutoField(primary_key=True)
    qr_code_id = models.ForeignKey(qr_code, unique=True)
    download_link = models.URLField(null=False, blank=False)

    def __unicode__(self):
        return self.download_link

class key_value(models.Model):

    id = models.AutoField(primary_key=True)
    qr_code_id = models.ForeignKey(qr_code)
    key = models.CharField(max_length=244, null=False, blank=False)
    value = models.CharField(max_length=244, null=False, blank=False)

    def __unicode__(self):
        return self.key + " - " + self.value

class ratings(models.Model):

    id = models.AutoField(primary_key=True)
    usage_id = models.ForeignKey(usage)
    key_value_id = models.ForeignKey(key_value)

class ordering(models.Model):

    id = models.AutoField(primary_key=True)
    usage_id = models.ForeignKey(usage)
    key_value_id = models.ForeignKey(key_value)
    quantity = models.IntegerField(default=0, blank=False, null=False)


class differnt_use(models.Model):

    id = models.AutoField(primary_key=True)
    qr_code_recieved = models.CharField(max_length=244, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=True, null=False, blank=False)
    user_id = models.ForeignKey(users)
    os = models.CharField(max_length=244, blank=True, null=True)
    location = models.CharField(max_length=244, blank=True, null=True)