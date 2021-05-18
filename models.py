from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    name_belt = models.CharField(max_length=50)
    name_color = models.CharField(max_length=50)
    price = models.DecimalField( max_digits=8, decimal_places=2,default=0.00)
    image = models.ImageField(null=True, blank=True)
    color1 = models.ImageField(null=True, blank=True)
    color2 = models.ImageField(null=True, blank=True)
    color3 = models.ImageField(null=True, blank=True)
    pattern1 = models.ImageField(null=True, blank=True)
    pattern2 = models.ImageField(null=True, blank=True)
    pattern3 = models.ImageField(null=True, blank=True)
    pattern4 = models.ImageField(null=True, blank=True)


    def _str_(self):
        return self.id,self.price,self.image,self.color1,self.pattern1
        def get_absolute_url(self):
            from django.urls import reverse
            return reverse('item', args=[str(self.id)])


class Item2(models.Model):
    name = models.CharField(max_length=50)
    name_belt = models.CharField(max_length=50)
    name_color = models.CharField(max_length=50)
    price = models.DecimalField( max_digits=8, decimal_places=2,default=0.00)
    image = models.ImageField(null=True, blank=True)
    color1 = models.ImageField(null=True, blank=True)
    color2 = models.ImageField(null=True, blank=True)
    color3 = models.ImageField(null=True, blank=True)
    pattern1 = models.ImageField(null=True, blank=True)
    pattern2 = models.ImageField(null=True, blank=True)
    pattern3 = models.ImageField(null=True, blank=True)
    pattern4 = models.ImageField(null=True, blank=True)

    def _str_(self):
        return self.id,self.price,self.image,self.color1,self.pattern1
        def get_absolute_url(self):
            from django.urls import reverse
            return reverse('item2', args=[str(self.id)])

class Item3(models.Model):
    name = models.CharField(max_length=50)
    name_belt = models.CharField(max_length=50)
    name_color = models.CharField(max_length=50)
    price = models.DecimalField( max_digits=8, decimal_places=2 ,default=0.00)
    image = models.ImageField(null=True, blank=True)
    color1 = models.ImageField(null=True, blank=True)
    color2 = models.ImageField(null=True, blank=True)
    color3 = models.ImageField(null=True, blank=True)
    pattern1 = models.ImageField(null=True, blank=True)
    pattern2 = models.ImageField(null=True, blank=True)
    pattern3 = models.ImageField(null=True, blank=True)
    pattern4 = models.ImageField(null=True, blank=True)

    def _str_(self):
        return self.id,self.price,self.image,self.color1,self.pattern1
        def get_absolute_url(self):
            from django.urls import reverse
            return reverse('item3', args=[str(self.id)])

class Comment(models.Model):
    user = models.ForeignKey(User,related_name='reviews',on_delete=models.CASCADE)
    item = models.ForeignKey(Item,related_name='reviews',on_delete=models.CASCADE)
    comment = models.TextField(max_length=1500)
    date_added = models.DateTimeField(auto_now_add=True)

class Comment2(models.Model):
    user = models.ForeignKey(User,related_name='reviews2',on_delete=models.CASCADE)
    item = models.ForeignKey(Item2,related_name='reviews2',on_delete=models.CASCADE)
    comment = models.TextField(max_length=1500)
    date_added = models.DateTimeField(auto_now_add=True)

class Comment3(models.Model):
    user = models.ForeignKey(User,related_name='reviews3',on_delete=models.CASCADE)
    item = models.ForeignKey(Item3,related_name='reviews3',on_delete=models.CASCADE)
    comment = models.TextField(max_length=1500)
    date_added = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(verbose_name="Phone number",max_length=10)
    address = models.CharField(max_length=200, null=True, blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        if self.first_name:
            name = self.first_name
        else:
            name = self.device
        return str(name)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

class OrderItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    product2 = models.ForeignKey(Item2, on_delete=models.SET_NULL, null=True)
    product3 = models.ForeignKey(Item3, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

