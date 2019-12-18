from django.conf.urls import url

from . import views
app_name = 'dashboard'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^dashboard', views.index, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'^$', views.login, name='login')
    #     url(r'^restaurants$', views.restaurants, name='restaurants'),
    #     url(r'^restaurants/specials/(?P<restaurant>[a-z0-9 ]+)$',
    #         views.specials, name='specials'),
]
