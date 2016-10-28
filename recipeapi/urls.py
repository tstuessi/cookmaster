# url page
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_recipe/(?P<recipe>.*)/$', views.get_recipe, name="get recipe"),
    url(r'^$', views.index, name="recipe index")
]
