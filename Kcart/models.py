from django.db import models


# Create your models here.
class Product(models.Model):
    Product_Id = models.AutoField
    Product_Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=300)
    Category = models.CharField(max_length=50,default="")
    Sub_Category = models.CharField(max_length=50,default="")
    Price = models.IntegerField(default=0)
    Image = models.ImageField(upload_to="Kcart/images",default="")

    Publish_Date = models.DateField()
    def __str__(self):
        return self.Product_Name

class Contact(models.Model):
    Msg_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=70)
    Email = models.CharField(max_length=70, default="")
    Phone = models.CharField(max_length=70, default="")
    Description = models.CharField(max_length=500)

    def __str__(self):
        return self.Name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=15)
    additional_phone =models.CharField(max_length=15)
    amount = models.IntegerField(default=0)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

