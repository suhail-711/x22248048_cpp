from django.shortcuts import render,redirect
from backend.models import *
from. models import *
from django.contrib import messages


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
        # Get cart details for the customer
    data = CartDetails.objects.filter(customer_name=request.session['name'])

    subtotal = 0
    for d in data:
        subtotal += d.total  # Summing up the totals of each cart item

    # Calculate the delivery charge based on subtotal
    if subtotal >= 50:
        delivery = 2
    else:
        delivery = 3

    # Calculate the final total (subtotal + delivery charge)
    total = subtotal + delivery

    # Render the cart.html template with the calculated values
    return render(request, "cart.html", {
        'data': data,
        'total': total,
        'subtotal': subtotal,
        'delivery': delivery
    })

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

def save_useraccount(request):
   
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password1')

        obj = UserAccount(name=name, email=email, password=password)
        obj.save()
        messages.success(request, "Success! Your account is now active.Please Login.. Happy shopping")
        return redirect(signup_page)



def user_login(request):
    if request.method == "POST":
        username  = request.POST.get('username')
        password = request.POST.get('password')
        request.session['name'] = username
        request.session['password'] =password
        if UserAccount.objects.filter(name=username,password=password).exists():  # checking username and password exist in the db
            messages.success(request, "WELCOME.!")
            return redirect(home_page)
        else:
            messages.error(request, "User not found.!")
            return redirect(signup_page)
    else:
        return redirect(signup_page)

def user_logout(request):
    del request.session['name']
    del request.session['password']
    messages.success(request, "You have been signed out.")
    return redirect(signup_page)

def save_cart(request):
    if request.method == "POST":
        user = request.POST.get('user')
        book = request.POST.get('bookname')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        total = request.POST.get('total')

        obj = CartDetails(customer_name=user, book=book, price=price, quantity=quantity, total=total)  # saving product details into cart db
        obj.save()
        messages.success(request, "Your book has been added to the cart..Great choice!!")
        return redirect(products_page)


def remove_cartitem(request, book_id):

    x = CartDetails.objects.get(id=book_id)
    x.delete()
    messages.success(request, "The book has been removed from your cart")
    return redirect(cart_page)