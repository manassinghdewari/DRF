from django.urls import path

from . import views

urlpatterns = [
    # path('<int:pk>',views.ProductDetailAPIView.as_view())
    # or
    # path('/',views.product_create_view),
    # path('<int:pk>/',views.product_detail_view)

    # for function views
    # path("/", views.product_alt_views),
    # path("<int:pk>/", views.product_alt_views),

    # path('',views.product_mixin_view),
    # for authentication
    path('',views.product_list_create_view),
    path('<int:pk>/update/',views.product_update_view),
    path('<int:pk>/delete/',views.product_destroy_view),
    # path('<int:pk>/',views.product_detail_view)
    # path('<int:pk>/detail/',views.product_mixin_view)
    # for authentication
    path('<int:pk>/detail/',views.product_detail_view)
]
