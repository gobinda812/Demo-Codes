from django.db import models
import weekday_field
# Create your models here.
class Aboutme(models.Model):
    aboutme_bengali = models.TextField(blank=True,null=True)
    aboutme_hindi = models.TextField(blank=True,null=True)
    aboutme_english = models.TextField(blank=True,null=True)
    whatsapp = models.IntegerField()
    email = models.EmailField()

class Region(models.Model):
    region =models.CharField(max_length=300)
    def __str__(self):
        return self.region


class Timming(models.Model):
    DAYS_OF_WEEK = (
    ('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    )
    day =  models.CharField(max_length=200, choices= DAYS_OF_WEEK)
    open = models.CharField(max_length=10)
    close = models.CharField(max_length=10)

    def __str__(self):
        return "{} : {} - {}".format(self.day,self.open, self.close)


class NearPlace(models.Model):
    place = models.CharField(max_length=200)
    def __str__(self):
        return self.place

class Chamber(models.Model):
    chamber_location = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    full_address =models.TextField()
    phone1 = models.BigIntegerField()
    phone2= models.BigIntegerField(blank=True, null=True)
    timming = models.ManyToManyField(Timming, related_name="Timming")
    nearest_places = models.ManyToManyField(NearPlace, related_name="NearestPlaces", blank=True)
    geo_loc = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.chamber_location

class Announcement(models.Model):
    datetimming = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Youtube(models.Model):
    link = models.URLField()
    title = models.CharField(max_length=400, default='Enter your title')
    description = models.TextField(blank=True,null=True)

class Gallery(models.Model):
    img = models.ImageField(upload_to='special_image')
    description = models.TextField(blank=True, null=True)