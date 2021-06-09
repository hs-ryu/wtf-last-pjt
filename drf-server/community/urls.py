from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    # 게시글 관련 URL
    path('createarticle/', views.createarticle, name='createarticle'),
    path('articles/', views.getallarticles, name='getallarticles'),
    path('articles/<int:article_pk>/', views.getarticle, name='getarticle'),
    path('articles/<int:article_pk>/updatearticle/', views.updatearticle, name='updatearticle'),
    path('articles/<int:article_pk>/deletearticle/', views.deletearticle, name='deletearticle'),
    path('articles/<int:article_pk>/likes/', views.likearticle, name='likearticle'),

    # 게시글의 댓글 관련 URL
    path('articles/<int:article_pk>/createcomment/', views.createcomment, name='createcomment'),
    path('articles/<int:article_pk>/comments/', views.getallcomments, name='getallcomments'),
    path('articles/<int:article_pk>/comments/<int:comment_pk>/updatecomment/', views.updatecomment, name='updatecomment'),
    path('articles/<int:article_pk>/comments/<int:comment_pk>/deletecomment/', views.deletecomment, name='deletecomment'),
]