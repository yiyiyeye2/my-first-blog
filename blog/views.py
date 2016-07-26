from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
	# __lte means less than or equal, this is used when filtering the QuerySets 
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk1):
	post = get_object_or_404(Post,pk=pk1)
	# pk is a parameter which is similar to id, and server finds the post in Post according to pk value
	return render(request, 'blog/post_detail.html', {'post':post})
	