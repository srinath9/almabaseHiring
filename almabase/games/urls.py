from django.conf.urls import url,include

# from forms import GamesForm
from . import views
urlpatterns = [
    url(r'^$', views.all, name='index'),
    url(r'^all/$', views.all, name='index'),
 	url(r'^accounts/', include('registration.backends.simple.urls')),
 	url(r'^all/(?P<page_id>[0-9]+)/$', views.pagination, name='pagination'),
 	url(r'^accounts/profile/$', views.all, name='profile'),

 	# url(r'^accounts/register/$', RegistrationView.as_view( form_class=GamesForm
  #       ),
  #       name='registration_register',
    # ),
]
