from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Product
from rest_framework.exceptions import ValidationError
# Create your views here.

@api_view(['GET'])
def list_product(request):
    products = Product.objects.all()

    data = [{'title': product.title, 'desc': product.desc, 'price': product.price, 'color': product.color} \
        for product in products]

    return Response({
        'count': products.count(),
        'msg': 'list',
        'status': status.HTTP_200_OK,
        'data': data
    })


@api_view(['GET'])
def detail_product(request,pk):
    product = Product.objects.filter(pk=pk).first()

    if not product:
        raise ValidationError({'msg': 'Product not found', 'status':status.HTTP_400_BAD_REQUEST})

    return Response({
        'count': 'detail',
        'status': status.HTTP_200_OK,
        'data': {'title': product.title, 'desc': product.desc, 'price': product.price, 'color': product.color} 
    })


@api_view(['POST'])
def create_product(request):
    product = Product.objects.create(**request.data)

    
    return Response({
        'count': 'created',
        'status': status.HTTP_201_CREATED,
        'data': {'title': product.title, 'desc': product.desc, 'price': product.price, 'color': product.color} 
    })

@api_view(['PATCH'])
def update_product(request, pk):

    product = Product.objects.filter(pk=pk).first()

    if not product:
        raise ValidationError({'msg': 'Product not found', 'status':status.HTTP_400_BAD_REQUEST})
    
    title = request.data.get('title')

    if title:
        product.title = title

    product.save()
    
    return Response({
        'count': 'updated',
        'status': status.HTTP_200_OK,
        'data': {'title': product.title, 'desc': product.desc, 'price': product.price, 'color': product.color} 
    })

@api_view(['DELETE'])
def delete_product(request, pk):

    product = Product.objects.filter(pk=pk).first()

    if not product:
        raise ValidationError({
            'msg': 'Product not found',
            'status': status.HTTP_400_BAD_REQUEST
        })

    product.delete()

    return Response({
        'msg': 'Product deleted',
        'status': status.HTTP_200_OK
    })