from django.db import models

# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    licensenum = models.CharField(max_length=100,blank=True)
    price = models.DecimalField(max_digits=9,decimal_places=2,null=True)
    showroom = models.ForeignKey('Showroom',on_delete=models.CASCADE,related_name='Showroom',null=True,blank=True)
    
    def __str__(self):
        return self.name
    


class Showroom(models.Model):
    shopname= models.CharField(max_length=50)
    loction = models.CharField(max_length=50)
    zipcode = models.IntegerField(blank=True)

    def __str__(self):
        return self.shopname
    
    

    