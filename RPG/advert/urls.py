from django.urls import path


from . import views
from .views import *

urlpatterns = [
   path('create/', views.advert_new, name='advert_new'),
   path('', PostList.as_view()),
   path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/comment_new/', views.comment_new, name='comment_new'),
   path('comment/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
   path('comments/', CommentList.as_view()),

]
