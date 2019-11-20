from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post
from django.db.models import Count, Q
from .forms import CommentForm

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)|
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_list.html', context)


def get_category_count():
    queryset = Post\
    .objects\
    .values('categories__title')\
    .annotate(Count('categories__title'))
    return queryset

def index(request):
    featured = Post.objects.filter(featured=True)[0:5]
    latest = Post.objects.order_by('-timestamp')[0:6]
    context = {
        'object_list': featured,
        'latest': latest,
    }
    return render(request, 'index.html', context)

def blog(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:5]
    post_list = Post.objects.filter(top10=False)
    context ={
        'post_list' : post_list,
        'most_recent': most_recent,
        'category_count': category_count
    }
    return render(request, 'blog.html', context)

def top10(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:5]
    top10_list = Post.objects.filter(top10=True)
    context ={
        'top10_list' : top10_list,
        'most_recent': most_recent,
        'category_count': category_count
    }
    return render(request, 'top10.html', context)

def post(request, slug, id):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:5]
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'slug': post.slug,
                'id': post.id
            }))
    context = {
        'form': form,
        'post': post,
        'most_recent': most_recent,
        'category_count': category_count
    }
    return render(request, 'post.html', context)

def  aboutus(request):
    context = {
        'aboutus': aboutus
    }
    return render(request, 'aboutus.html', context)
