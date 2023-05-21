# from django.shortcuts import render
# from django.http import JsonResponse
# from products.models import Product
# from django.forms.models import model_to_dict
# import json
# Create your views here.

# def api_home(request,*args,**kwargs):
#     # request -> httpRequest -> Django
#     # print(dir(request))
#     # request.body
#     body=request.body   #byte string of JSON data
#     data = {}
#     try:
#         data=json.loads(body)   #string of JSON data -> Python Dict
#     except:
#         pass
#     print(body)
#     data['params'] = dict(request.GET)   #to get query from the url
#     data['content_type']=request.content_type
#     data['headers']=dict(request.headers)
#     # return JsonResponse({"message":"Hi there, this is your Django API response !!"})
#     return JsonResponse(data)
 
#  51:34

# By using models

# def api_home(request,*args,**kwargs):
#     model_data=Product.objects.all().order_by("?").first()
#     data={}
#     # if model_data:
#         # data['id']=model_data.id
#         # data['title']=model_data.title
#         # data['content']=model_data.content
#         # data['price']=model_data.price
#     # as we are converting the data to json format
#     # we can do same usign model_to_dict function 

#     if model_data:
#         # data=model_to_dict(model_data)
#         data=model_to_dict(model_data,fields=['id','title','price'])
#     return JsonResponse(data)



# now we are going to use Django Rrest Framework 

from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product

from products.serializers import ProductSerializer

# @api_view(["GET"])
# def api_home(request,*args,**kwargs):
#     model_data =Product.objects.all().order_by("?").first()
#     data={}
#     if model_data:
#         data=model_to_dict(model_data,fields=['id','title','price','sale_price'])
#     return Response (data)

# by using serializers we can easily get all the data

# @api_view(["GET"])
# def api_home(request,*args,**kwargs):
#     instance =Product.objects.all().order_by("?").first()
#     data={}
#     if instance:
#         data=ProductSerializer(instance).data
#     return Response (data)


@api_view(["POST"])
def api_home(request,*args,**kwargs):
    serializer = ProductSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        print(instance)
        data=serializer.data
        return Response(data)
    return Response({"invalid":"Not good data"},status=400)
    
        