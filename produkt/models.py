from django.db import models

# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='make/',blank=True,null=True)

    def __str__(self):
        return self.name




class Product(models.Model):
    name_product = models.CharField(max_length=100)
    make = models.ForeignKey(Make,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    county = models.CharField(max_length=100)
    create_at = models.DateField(auto_now_add=True)
    desc = models.TextField()
    image = models.ImageField(upload_to='product/',blank=True,null=True)

    def __str__(self):
        return f'{self.name_product},{self.make}'




