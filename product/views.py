from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from product.models import Product
from product.serializers import CategoryListSerializer, ProductDetailSerializer, ProductListSerializer


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class CreateProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
