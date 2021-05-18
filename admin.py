from django.contrib import admin
from myapp.models import Item,Comment,Comment2,Comment3,Item2,Item3,Customer
from myapp.models import Order,OrderItem

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','name_belt','name_color','price','image','color1','color2','color3','pattern1','pattern2','pattern3','pattern4']
admin.site.register(Item,ItemAdmin)

class Item2Admin(admin.ModelAdmin):
    list_display = ['name','name_belt','name_color','price','image','color1','color2','color3','pattern1','pattern2','pattern3','pattern4']
admin.site.register(Item2,Item2Admin)

class Item3Admin(admin.ModelAdmin):
    list_display = ['name','name_belt','name_color','price','image','color1','color2','color3','pattern1','pattern2','pattern3','pattern4']
admin.site.register(Item3,Item3Admin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','item','comment','date_added']
admin.site.register(Comment,CommentAdmin)

class Comment2Admin(admin.ModelAdmin):
    list_display = ['user','item','comment','date_added']
admin.site.register(Comment2,Comment2Admin)

class Comment3Admin(admin.ModelAdmin):
    list_display = ['user','item','comment','date_added']
admin.site.register(Comment3,Comment3Admin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','phone','address']
admin.site.register(Customer,ProfileAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
