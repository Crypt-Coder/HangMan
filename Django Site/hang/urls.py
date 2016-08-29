from django.conf.urls import url
from . import views

app_name = 'hang'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^game/$',views.game,name = 'game'),
    url(r'^hint/$',views.hint,name = 'hint'),
    url(r'^add/$',views.add,name = 'add'),
]
