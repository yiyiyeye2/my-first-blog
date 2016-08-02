from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.post_list, name='post_list'),
	url(r'^post/(?P<pk1>\d+)$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk1>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^drafts/$',views.post_draft_list,name='post_draft_list'),
	url(r'^post/(?P<pk1>\d+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^post/(?P<pk1>\d+)/remove/$', views.post_remove, name='post_remove'),
	

	# There are two functions of this urlpattern, the first one is to create anurls.py file url using {%url%} model
	# which follows the regular expression here. The second function is to match the website address to
	# a certain veiw.
]