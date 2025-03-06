from django.shortcuts import render,redirect
from. models import CategoryDB , BooksDB, BackendUserDB
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from bookshop_UI.models import CustomerQuery

def index_page(request):
    data = CustomerQuery.objects.all
    return render(request,"index.html",{'data':data})

def add_category(request):
    return render(request,"add_category.html")

def save_categories(request):
    if request.method=="POST":
        category = request.POST.get('category')
        description = request.POST.get('description')
        image = request.FILES['image']

        obj = CategoryDB(category =category,Description =description,Image = image)
        obj.save()
        messages.success(request,"Category Added Successfully.!")
        return redirect(add_category)

def view_category(request):
    data = CategoryDB.objects.all
    return render(request,"view_category.html",{'data':data})

def editpage_category(request,category_id):
    data = CategoryDB.objects.get(id=category_id)
    return render(request,"edit_category.html",{'data':data})



def update_category(request,category_id):

    if request.method == "POST":
        category = request.POST.get('category')
        description = request.POST.get('description')

        try:
            image = request.FILES['image']
            x = FileSystemStorage()
            file = x.save(image.name,image)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=category_id).Image
            
        CategoryDB.objects.filter(id=category_id).update( category =category,Description =description,Image = file)
        messages.success(request, "Updated Successfully.!")
        return redirect(view_category)


def delete_category(request,category_id):
    data = CategoryDB.objects.get(id=category_id)
    data.delete()
    messages.info(request,"Category Deleted.!")
    return redirect(view_category)

def add_books(request):
    category_data = CategoryDB.objects.all
    return render(request,"add_books.html",{'category_data':category_data})

def save_books(request):
    if request.method=="POST":
        book_name = request.POST.get('name')
        book_cata = request.POST.get('category')
        book_des = request.POST.get('description')
        book_price = request.POST.get('price')
        book_img = request.FILES['image']

        ob = BooksDB(name =  book_name, category = book_cata, description = book_des, price = book_price,image = book_img)
        ob.save()
        messages.success(request,"New Book Added Successfully.!")
        return redirect(add_books)

def view_books(request):
    books = BooksDB.objects.all
    return render(request,"view_books.html",{'books':books})

def edit_books(request,book_id):
    data = BooksDB.objects.get(id=book_id)
    category = CategoryDB.objects.all

    return render(request,"edit_books.html",{'data':data,'category':category})

def update_books(request,book_id):
    if request.method=="POST":
        book_name = request.POST.get('name')
        book_cata = request.POST.get('category')
        book_des = request.POST.get('description')
        book_price = request.POST.get('price')
        
        try:
            image = request.FILES['image']
            x = FileSystemStorage()
            file = x.save(image.name,image)
        except MultiValueDictKeyError:
            file = BooksDB.objects.get(id=book_id).image
        BooksDB.objects.filter(id=book_id).update( name =  book_name, category = book_cata, description = book_des, price = book_price,image = file)
        messages.success(request,"Updated Successfully.!")
        return redirect(view_books)

def delete_books(request,book_id):
    x = BooksDB.objects.get(id=book_id)
    x.delete()
    messages.info(request,"Book Deleted.!!")
    return redirect(view_books)
def signup(request):
    return render(request,"signup_page.html")


def save_backendadmin(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password1')

        obj = BackendUserDB(name=name, email=email, password=password)
        obj.save()
        return redirect(signin_page)

def signin_page(request):
    return render(request,"sign_in.html")

def signin_admin(request):
    if request.method == "POST":
        username  = request.POST.get('username')
        password = request.POST.get('password')
        request.session['name'] = username
        request.session['password'] =password
        if BackendUserDB.objects.filter(name=username,password=password).exists():  # checking username and password exist in the db
            messages.success(request, "WELCOME.!")
            return redirect(index_page)
        else:
            messages.error(request, "User not found.!")
            return redirect(signin_page)
    else:
        return redirect(signin_page)

def user_logout(request):
    del request.session['name']
    del request.session['password']
    messages.success(request, "You have been signed out.")
    return redirect(signin_page)





