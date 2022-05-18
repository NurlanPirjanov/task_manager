from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name="task_edit"),
    path('<int:pk>/add/', TaskCommentView.as_view(), name="comment_add"),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('new/', TaskCreateView.as_view(), name='task_new'),
    path('', TaskMyListView.as_view(), name='task_list'),
    path('n/', TaskMyNewListView.as_view(), name='task_new_list'),
    path('like/<int:pk>', LikeView, name="like_post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)