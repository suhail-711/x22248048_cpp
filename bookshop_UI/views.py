from django.shortcuts import render,redirect
from backend.models import *
from. models import *


def home_page(request):
    category=CategoryDB.objects.all
    return render(request,"home.html",{'category':category})

def products_page(request):
    books = BooksDB.objects.all
    return render(request,"products.html",{'books':books})

def contact_us(request):
    return render(request,"contact.html")

def about_us(request):
    return render(request,"about.html")


def bookby_category(request,category):
    books = BooksDB.objects.filter(category=category)
    return render(request,"booksby_category.html",{'books':books})

def cart_page(request):
    return render(request,"cart.html")

def single_book(request,book_id):
    book= BooksDB.objects.get(id=book_id)
    return render(request,"single_book.html",{'book':book})


def customer_queries(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        obj = CustomerQuery(name=name,email=email,message=message)
        obj.save()
        return redirect(contact_us)

def signup_page(request):
    return render(request, "signup_page.html")



