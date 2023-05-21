from rest_framework import generics, mixins, permissions, authentication
from .models import Product
from .serializers import ProductSerializer

# for function based views
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.http import Http404
# or this
from django.shortcuts import get_object_or_404
from .permissions import IsStaffEditorPermission


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        print("title", title)
        print("content", content)
        if content is None:
            content = title
        serializer.save(content=content)
        print("content", content)


product_create_view = ProductCreateAPIView.as_view()


# Retrive view is for retriving the data
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field='pk'


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


product_destroy_view = ProductDestroAPIView.as_view()


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    # permission_classes=[permissions.DjangoModelPermissions]
    permission_classes = [IsStaffEditorPermission]

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        if content is None:
            content = title
        serializer.save(content=content)


product_list_create_view = ProductListCreateAPIView.as_view()


# Mixins


class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        print("args", args)
        print("kwargs", kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


product_mixin_view = ProductMixinView.as_view()


# Function based Views


@api_view(["GET", "POST"])
def product_alt_views(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            # detail view
            # queryset=Product.objects.filter(pk=pk)
            # if not queryset.exists():
            #     raise Http404
            # or we can do same thing with get_object_or_404
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        queryset = Product.objects.all()
        # queryset repersents all the products
        data = ProductSerializer(queryset, many=True).data
        # queryset serialized using ProductSerializer many=True means
        # there
        return Response(data)
    if method == "POST":
        serializer = ProductSerializer(
            data=request.data
        )  # for initilization of ProductSerializer
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"Invalid": "not good data"}, status=400)
