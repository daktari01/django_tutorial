from django.conf.urls import url
from home.views import HomeView


urlpatterns = [
    #url(r'post/(?P<block_id>\d+)/$', HomeView.as_view(), name='home'),
    url(r'^$', HomeView.as_view(), name='home'),
    #post/(?P<block_id>\d+)/$
]