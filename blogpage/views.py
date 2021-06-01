from django.shortcuts import get_object_or_404, render, redirect
from .models import AuthorDetails, Post
from django.views import generic
# from django.forms import UserForm

# Create your views here.


def home_page(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    # if request.method == 'POST':
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         form.save()
    #         return redirect('/blog-page/')
    #     else:
    #         print('Form is invalid')
    # else:
    #     form = UserForm()

    return render(request, 'signup.html')


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogpage.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blogdetail.html'


def author_info(request, user_id):

    obj = get_object_or_404(AuthorDetails, id=user_id)
    return render(request, 'about.html', context={'user_obj': obj})

