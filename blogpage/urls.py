from django.urls import path
from .views import home_page, login, signup, author_info, PostList, PostDetail

app_name = 'blogpage'

urlpatterns = [
    path('', home_page),
    path('login-user/', login),
    path('signup-new/', signup),
    path('author-info/<int:user_id>', author_info),
    path('blog-page/', PostList.as_view(), name='post_list'),
    path('detail-blog-page/<slug:slug>/', PostDetail.as_view(), name='post_detail'),

]
