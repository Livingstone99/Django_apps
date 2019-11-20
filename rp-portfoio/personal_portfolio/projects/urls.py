from django.urls import path
from . import views
urlpatterns = [
    path('', views.project_index, name = 'project_index'),
    path('<int:pk>/', views.project_detail, name = 'project_detail'),
]
# in line 4, we hook up the root URL of our app to the project_index view.
# it is slightly more complicated to hook up the project_detail view. to do this,
# we want the url to /1, /2, and so on, depending on the pk of the project.
# the pk value in url is the same pk passed to the view function, so you need
# to dynamically generate these urls depending on which project you want to view.
# to this, we used the <int:pk> notation. this tells django that the value
# passed in url is an integer,
# and its variable name is pk