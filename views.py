from django.shortcuts import render
from myapp.models import Item,Comment,Comment2,Comment3,Item2,Item3,Customer,Order,OrderItem
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic.detail import DetailView
from myapp.forms import RegisterForm,ProfileForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages


# Create your views here.
def ItemDetailView(request, pk):
    item=Item.objects.get(id=pk)
    item.save()
    
    if request.method == 'POST':
        item=Item.objects.get(id=pk)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=item)
        orderItem.quantity=request.POST.get('quantity',False)
        orderItem.save()
        return redirect('cart')
        
    context = {
        'item': item,
    }
    return render(request, 'shopdetail1.html', context)

def Commentview(request,pk):
    item=Item.objects.get(id=pk)
    item.save()
    if request.method == 'POST' and request.user.is_authenticated:
        comment = request.POST.get('comment', '')
        review = Comment.objects.create(item=item, user=request.user ,comment=comment)
        return redirect('itemDetailView',pk) 
    context = {
        'item': item,
    }
    return render(request, 'shopdetail1.html', context)


def Item2DetailView(request, pk):
    item=Item2.objects.get(id=pk)
    item.save()

    if request.method == 'POST':
        item=Item2.objects.get(id=pk)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product2=item)
        orderItem.quantity=request.POST.get('quantity',False)
        orderItem.save()
        return redirect('cart') 
        
    context = {
        'item': item,
    }
    return render(request, 'shopdetail5.html', context)

def Commentview2(request,pk):
    item=Item2.objects.get(id=pk)
    item.save()
    if request.method == 'POST' and request.user.is_authenticated:
        comment = request.POST.get('comment', '')
        review = Comment2.objects.create(item=item, user=request.user ,comment=comment)
        return redirect('item2DetailView',pk) 
    context = {
        'item': item,
    }
    return render(request, 'shopdetail5.html', context)

def Item3DetailView(request, pk):
    item=Item3.objects.get(id=pk)
    item.save()

    if request.method == 'POST':
        item=Item3.objects.get(id=pk)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product3=item)
        orderItem.quantity=request.POST.get('quantity',False)
        orderItem.save()
        return redirect('cart')
        
    context = {
        'item': item,
    }
    return render(request, 'shopdetail9.html', context)

def Commentview3(request,pk):
    item=Item3.objects.get(id=pk)
    item.save()
    if request.method == 'POST' and request.user.is_authenticated:
        comment = request.POST.get('comment', '')
        review = Comment3.objects.create(item=item, user=request.user ,comment=comment)
        return redirect('item3DetailView',pk) 
    context = {
        'item': item,
    }
    return render(request, 'shopdetail5.html', context)


def Cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    context = {'order':order}
    return render(request, 'cart.html', context)




def Register(request):
    if request.method == 'POST':
        r_form = RegisterForm(request.POST)
        p_form = ProfileForm(request.POST)
        if r_form.is_valid() and p_form.is_valid():
            user = r_form.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            messages.success(request,f'Registration complete')
            return redirect('login')
    else:
        r_form = RegisterForm(request.POST)
        p_form = ProfileForm(request.POST)
    return render(request, "register.html",{'r_form': r_form, 'p_form':p_form})

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username OR password is incorrect')
    context = {}
    return render(request, "login.html",context)

def Logout(request):
    logout(request)
    return redirect('home')

def Home(request):
    return render(request,'index.html')

def About(request):
    return render(request,'aboutus.html')

def Forum(request):
    return render(request,'forum.html')

def Forum1(request):
    return render(request,'forum1.html')

def Forum2(request):
    return render(request,'forum2.html')

def Forum3(request):
    return render(request,'forum3.html')

def Forum4(request):
    return render(request,'forum4.html')

def Product(request):
    return render(request,'product.html')


