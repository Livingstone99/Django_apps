from django.urls import path
from .import views

urlpatterns = [
    path("", views.piction, name="piction"),
    path('redirect/',views.piction, name = "success" )
    # path("<int:pk>/", views.blog_detail, name="blog_detail"),
    # path("<category>/", views.blog_category, name="blog_category"),
]