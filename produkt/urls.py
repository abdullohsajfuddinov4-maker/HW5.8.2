from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('product/<int:pk>',views.product,name='product'),
    path('full/<int:pk>',views.desc,name="full"),
    path('create_product/', views.create_product, name='create'),
    path('updata_product/<int:pk>/', views.updata_product, name='updata'),
    path('del_product/<int:pk>/', views.del_product, name='del'),

]