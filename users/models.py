from django.db import models

class gplus_users(models.Model):

    id = models.AutoField(primary_key=True)
    user_id = models.CharField(unique=True, max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254, null=True)
    secondary_email = models.EmailField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=False)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=100, default="mumbai", null=True, blank=False)
    phone = models.CharField(max_length=15, null=True, blank=False)
    image_url = models.TextField(null = True, blank = True)
    profile_url = models.TextField(null = True, blank = True)
    date_of_birth = models.DateField(null = True, blank = True)
    mobile_os = models.CharField(max_length=20, default="android", null=True, blank=False)
    os_version = models.CharField(max_length=20, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.email + " " + self.name

class fb_users(models.Model):

    id = models.AutoField(primary_key=True)
    user_id = models.CharField(unique=True, max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254, null=True)
    secondary_email = models.EmailField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=False)
    gender = models.CharField(max_length=6, null=True, blank=True)
    location = models.CharField(max_length=100, default="mumbai", null=True, blank=False)
    phone = models.CharField(max_length=15, null=True, blank=False)
    image_url = models.TextField(null = True, blank = True)
    profile_url = models.TextField(null = True, blank = True)
    date_of_birth = models.DateField(null = True, blank = True)
    mobile_os = models.CharField(max_length=20, default="android", null=True, blank=False)
    os_version = models.CharField(max_length=20, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.email + " " + self.name

class users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, null=True, unique=True)
    gplus_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    fb_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return self.email