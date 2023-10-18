from django.db import models

# Create your models here.
class tag(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name
    
class Custumer(models.Model) :
    CATEGORY=()
    name =models.CharField(max_length=200, blank=True, null=True)
    phone =models.CharField(max_length=200, blank=True, null=True)
    email =models.CharField(max_length=200, blank=True, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('Indoor', 'Indoor'),
        ('Out door', 'Out door'),
    )
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(tag)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS=(
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    custumer = models.ForeignKey(Custumer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    def __str__(self):
        # return '%s, %s,' % ( self.custumer, self.status,)
        return '%s, %s,' % (self.product.name, self.custumer)

# dibawah ini cara agar order tidak ada tambahan S di belakang 
    # class meta:
    #     verbose_name_plural="order"

