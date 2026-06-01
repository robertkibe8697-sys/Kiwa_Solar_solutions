from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title
from django.db import models

class HomePage(models.Model):
    hero_title = models.CharField(max_length=200)
    hero_text = models.TextField()
    hero_image = models.ImageField(upload_to='homepage/')

    def __str__(self):
        return "Homepage"



class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title
    
    from django.db import models

class AboutPage(models.Model):
    heading = models.CharField(max_length=200, default="About Us")

    introduction = models.TextField()

   
   

    ceo_image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.heading