from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('/about', views.about, name="about"),
    path('/login', views.login_user, name="login"),
    path('/logou', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('product/<int:pk>', views.product, name="product"),
    path('category/<str:foo>', views.category, name='category'),
    path('shopcart/', views.shopcart, name="shopcart"),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('all_product/', views.all_product, name="all_product")

]