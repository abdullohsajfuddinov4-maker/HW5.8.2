from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('product/<int:pk>',views.product,name='product'),
    path('full/<int:pk>',views.desc,name="full"),
    path('cretae_product/',views.create_product,name='create')
    ]