from django.db import models

# Create your models here.


# Create Model for below:
# Sliders
# Special Offers
STATUS = (('active', 'active'), ('', 'default'))


class Offer(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='offer')
    description = models.TextField()
    rank = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='slider')
    url = models.CharField(max_length=500)
    rank = models.IntegerField()
    status = models.CharField(choices=STATUS, blank=True, max_length=100)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField(max_length=400, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name
