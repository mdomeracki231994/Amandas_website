from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .serializers import ProductSerializer, AllProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def product_list(request):
    products = Product.objects.all()
    serializer = AllProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view()
def product_detail(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
