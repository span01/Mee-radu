"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import ItemDetailView
from myapp.views import Item2DetailView
from myapp.views import Item3DetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:pk>', views.ItemDetailView,name='itemDetailView'),
    path('comment/<int:pk>',views.Commentview,name='comment'),
    path('item2/<int:pk>', views.Item2DetailView,name='item2DetailView'),
    path('comment2/<int:pk>',views.Commentview2,name='comment2'),
    path('item3/<int:pk>', views.Item3DetailView,name='item3DetailView'),
    path('comment3/<int:pk>',views.Commentview3,name='comment3'),
    path('',views.Home,name='home'),
    path('Product/',views.Product,name='item'),
    path('aboutus/',views.About,name='Aboutus'),
    path('forum/',views.Forum,name='Forum'),
    path('forum1/',views.Forum1,name='Forum1'),
    path('forum2/',views.Forum2,name='Forum2'),
    path('forum3/',views.Forum3,name='Forum3'),
    path('forum4/',views.Forum4,name='Forum4'),
    path('register/',views.Register,name='register'),
    path('login/',views.Login, name='login'),
    path('logout/',views.Logout, name='logout'),
    path('cart/',views.Cart, name='cart'),
]
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)