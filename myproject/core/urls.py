from django.urls import path
from myproject.core import views as c


app_name = 'core'


urlpatterns = [
    path('', c.home, name='home'),
    path('read-file/', c.read_file, name='read_file'),
]
