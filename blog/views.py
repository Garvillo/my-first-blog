from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone
from .models import Post


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def home(request):
	data = [['00',11]
	,['01',10]
	,['02',9]
	,['03',9]
	,['04',8]
	,['05',7]
	,['06',5]
	,['07',3]
	,['08',4]
	,['09',6]
	,['10',8]
	,['11',12]
	,['12',16]]
	return render(request, 'registration/home.html', {'data': data})