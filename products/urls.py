from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create , name="create"),
    path('<int:product_id>', views.detail , name="detail"),
    path('<int:product_id>/upvote', views.upvote , name="upvote"),
]
