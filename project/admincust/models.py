from django.db import models

from PIL import Image

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    status = models.BooleanField(default=True)
    # seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank = True, null=True)
    def __str__(self):
        return self.name

class Seller(models.Model):
    seller_name = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    customers = models.ManyToManyField(Customer, blank=True, related_name='customers')

    def __str__(self):
        return self.seller_name
    
class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,)
    product_name = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    image = models.ImageField(null=True, blank=True, upload_to=' static')

    def __str__(self):
        return self.product_name

    def save(self):
        super().save()
        print(self.image)
        # print(self.image.height)
        # print(self.image.width)
        # print(self.image.path)
        if self.image is not None:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                print('-------------------')
                output_size = (300, 300)
                img.thumbnail(output_size)
                print(self.image.size)
                    # print(self.image.path)
                print('saved')
                img.save(self.image.path)

