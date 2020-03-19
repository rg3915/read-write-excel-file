from django.urls import path
from myproject.core import views as c


app_name = 'core'


urlpatterns = [
    path('', c.home, name='home'),
]
