from django.urls import path

from product.views import ProductListCreateView, ProductDetailView, CreateProductView

urlpatterns = [
    path('all/', ProductListCreateView.as_view(), name = 'product-list'),
    path('find/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('create/', CreateProductView.as_view(), name = 'adding')
]
