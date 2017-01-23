# url page
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^recipe/(?P<recipe_id>.*)/$', views.recipe, name="recipe"),
    url(r'^$', views.index, name="recipe index"),
    url(r'^newrecipe$', views.new_recipe, name="new recipe"),
]
