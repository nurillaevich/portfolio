from django.shortcuts import render, get_object_or_404, redirect

from main.form import CommentForm
from main.models import Post, Comment, Pricing, About, Friends


def home_page(request):
    posts = Post.objects.all().order_by('created')[:9]
    context = {'posts': posts}
    return render(request, 'index.html', context)


def gallery_page(request):
    posts = Post.objects.all().order_by('-created')
    context = {'posts': posts}
    return render(request, 'gallery.html', context)


def gallery_detail(request, pk, *args, **kwargs):
    form = CommentForm()
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post_id=pk).order_by('-created')
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(f'detail/{post.id}')
    context = {'form': form,
               'posts': post,
               'comments': comments}
    return render(request, 'single.html', context)


def pricing_page(request, *args, **kwargs):
    pricing = Pricing.objects.all()
    context = {
        'pricings': pricing,

    }
    return render(request, 'pricing.html', context)


def about_page(request):
    about = About.objects.all()
    friends = Friends.objects.all()
    context = {
        'abouts': about,
        'friends': friends
    }
    return render(request, 'about.html', context)
