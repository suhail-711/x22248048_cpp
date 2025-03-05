from django.urls import path
from. import views


urlpatterns =[
    path('index/',views.index_page,name="index"),
    path('category/',views.add_category,name="category"),
    path('savecategory/',views.save_categories,name="savecategory"),
    path('viewcategory/',views.view_category,name="viewcategory"),
    path('editpage_category/<int:category_id>',views.editpage_category,name="editpage_category"),
    path('update_category/<int:category_id>',views.update_category,name="update_category"),
    path('delete_category/<int:category_id>',views.delete_category,name="deletecategory"),
    path('add_books/',views.add_books,name="add_books"),
    path('save_books/',views.save_books,name="save_books"),
    path('view_books/',views.view_books,name="view_books"),
    path('edit_books/<int:book_id>',views.edit_books,name="edit_books"),
    path('update_books/<int:book_id>',views.update_books,name="update_books"),
    path('delete_books/<int:book_id>',views.delete_books,name="delete_books"),
    path('signup/',views.signup,name="signup"),
    path('save_backendadmin/',views.save_backendadmin,name="save_backendadmin"),
    path('signin/',views.signin_page,name="signin"),
    path('user_signin/',views.signin_admin,name="user_signin"),
    path('user_logout/',views.user_logout,name="logout")


]

