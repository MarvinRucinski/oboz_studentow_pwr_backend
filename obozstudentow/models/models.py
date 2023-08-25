from django.db import models
from django_resized import ResizedImageField
from django.contrib import admin

# Separate models

class Icons(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Ikonka"
        verbose_name_plural = "Ikonki"


class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.ForeignKey(Icons, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
class ScheduleItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    location = models.CharField(max_length=100, null=True, blank=True)
    photo = ResizedImageField(upload_to='schedule', blank=True)
    visible = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Harmonogram"
        verbose_name_plural = "Harmonogram"

    def __str__(self):
        return self.name
    
    @admin.display(
        boolean=True,
        description='Ma zdjęcie?',
    )
    def has_image(self):
        return bool(self.photo)
    

class Bus(models.Model):
    description = models.CharField(max_length=100)
    location = models.URLField()

    class Meta:
        verbose_name_plural = "Busy"

    def __str__(self):
        return "Bus " + self.description



class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Obrazek"
        verbose_name_plural = "Obrazki"


class Setting(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Ustawienie"
        verbose_name_plural = "Ustawienia"

class Partners(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    logo = ResizedImageField(upload_to='partners', force_format=None, size=[400, 400])

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partnerzy"


class House(models.Model):
    name = models.CharField(max_length=10)
    key_collected = models.BooleanField(default=False, verbose_name="Klucz odebrany")

    def __str__(self):
        return 'Domek nr ' + self.name

    class Meta:
        verbose_name = "Domek"
        verbose_name_plural = "Domki"

class HouseCollocationForImport(models.Model):
    house = models.CharField(max_length=10)
    bandId = models.CharField(max_length=6, blank=True, null=True, unique=True)
