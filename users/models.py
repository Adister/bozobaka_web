from django.db import models

class gplus_users(models.Model):

    id = models.AutoField(primary_key=True)
    user_id = models.CharField(unique=True, max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=254, null=True)
    secondary_email = models.EmailField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=False)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=100, default="mumbai", null=True, blank=False)
    phone = models.CharField(max_length=15, null=True, blank=False)
    image_url = models.TextField()
    profile_url = models.TextField()
    date_of_birth = models.DateField()
    mobile_os = models.CharField(max_length=20, default="android", null=True, blank=False)
    os_version = models.CharField(max_length=20, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user_id

class fb_users(models.Model):

    id = models.AutoField(primary_key=True)
    user_id = models.CharField(unique=True, max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=254, null=True)
    secondary_email = models.EmailField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=False)
    gender = models.CharField(max_length=6, null=True, blank=True)
    location = models.CharField(max_length=100, default="mumbai", null=True, blank=False)
    phone = models.CharField(max_length=15, null=True, blank=False)
    image_url = models.TextField()
    profile_url = models.TextField()
    date_of_birth = models.DateField()
    mobile_os = models.CharField(max_length=20, default="android", null=True, blank=False)
    os_version = models.CharField(max_length=20, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.user_id

class users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, null=True, unique=True)
    gplus_id = models.IntegerField()
    fb_id = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True, auto_now=True)

