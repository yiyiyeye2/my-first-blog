from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
	# __lte means less than or equal, this is used when filtering the QuerySets 
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk1):
	post = get_object_or_404(Post,pk=pk1)
	# pk is a parameter which is similar to id, and server finds the post in Post according to pk value
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST) #Create a form instance with POST data.
		if form.is_valid():
			post = form.save(commit=False)# Create, but don't save the new instance.
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk1=post.pk)

	else:
		form = PostForm()

	return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk1):
	post = get_object_or_404(Post, pk=pk1)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		# A subclass of ModelForm can accept an existing model instance as the keyword argument instance; 
		# if this is supplied, save() will update that instance. 
		# If it’s not supplied, save() will create a new instance of the specified model: 
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk1=post.pk)

	else:
		form = PostForm(instance=post)

	return render(request, 'blog/post_edit.html', {'form':form})
