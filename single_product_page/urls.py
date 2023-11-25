from . import views
from django.urls import path

urlpatterns = [
    path('', views.SingleProductDetailView.as_view(), name="product")
]
