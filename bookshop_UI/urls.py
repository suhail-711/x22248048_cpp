from django.urls import path
from. import views


urlpatterns =[
    path('',views.home_page,name="home"),
    path('all_products/',views.products_page,name="products_page"),
    path('contact/',views.contact_us,name="contact"),
    path('about_us/',views.about_us,name="about"),
    path('cart/',views.cart_page,name="cart"),
    path('bookby_category/<category>',views.bookby_category,name="bookby_category"),
    path('single_book/<int:book_id>',views.single_book,name="single_book"),
    path('customer_query/',views.customer_queries,name="customer_query"),
    path('signup_page/',views.signup_page,name="signup_page")
    
]