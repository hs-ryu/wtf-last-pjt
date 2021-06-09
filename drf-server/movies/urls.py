from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # DB 생성과 관련된 URL
    path('savegenre/', views.savegenre, name='savegenre'),
    path('savemovies/', views.savemovies, name='savemovies'),
    path('savenowshowing/', views.savenowshowing, name='savenowshowing'),

    # 영화와 관련된 URL
    path('getmovies/', views.getmovies, name='getmovies'),
    path('getmovies/<int:movie_pk>/', views.getmoviedetail, name='getmoviedetail'),
    path('getpopularmovies/', views.getpopularmovies, name='getpopularmovies'),
    path('getnowshowing/', views.getnowshowing, name='getnowshowing'),
    path('getmovies/<int:movie_pk>/likes/', views.likemovie, name='likemovie'),
    path('getgenre/<int:movie_pk>/', views.getgenre, name='getgenre'),
    # 영화 검색
    path('searchmovies/<str:search_item>/', views.searchmovies, name='searchmovies'),
    # 해당 플랫폼에서 상영중인 영화들 목록 불러오기
    path('<str:platform>/', views.platformmovies, name='platformmovies'),

    # 리뷰와 관련된 URL
    path('<int:movie_pk>/reviews/', views.getallreviews, name='getallreviews'),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.getreview, name='getreview'),
    path('<int:movie_pk>/createreview/', views.createreview, name='createreview'),
    path('<int:movie_pk>/reviews/<int:review_pk>/updatereview/', views.updatereview, name='updatereview'),
    path('<int:movie_pk>/reviews/<int:review_pk>/deletereview/', views.deletereview, name='deletereview'),
    path('<int:movie_pk>/reviews/<int:review_pk>/likes/', views.likereview, name='likereview'),

    # 댓글과 관련된 URL
    path('<int:movie_pk>/reviews/<int:review_pk>/createcomment/', views.createcomment, name='createcomment'),
    path('<int:movie_pk>/reviews/<int:review_pk>/getcomments/', views.getcomments, name='getcomments'),
    path('<int:movie_pk>/reviews/<int:review_pk>/<int:comment_pk>/deletecomment/', views.deletecomment, name='deletecomment'),
    path('<int:movie_pk>/reviews/<int:review_pk>/<int:comment_pk>/updatecomment/', views.updatecomment, name='updatecomment'),

    # # 투표와 관련된 URL
    path('<int:movie_pk>/votes/', views.getallvotes, name='getallvotes'),
    path('<int:movie_pk>/votes/<int:vote_pk>/', views.getvote, name='getvote'),
    path('<int:movie_pk>/createvote/', views.createvote, name='createvote'),
    path('<int:movie_pk>/<int:vote_pk>/deletevote/', views.deletevote, name='deletevote'),

    # # 투표 댓글과 관련된 URL
    path('<int:movie_pk>/votes/<int:vote_pk>/createvotecomment/', views.createvotecomment, name='createvotecomment'),
    path('<int:movie_pk>/votes/<int:vote_pk>/votecomments/', views.getvotecomments, name='getallvotecomments'),
    path('<int:movie_pk>/votes/<int:vote_pk>/<int:votecomment_pk>/deletevotecomment/', views.deletevotecomment, name='deletevotecomment'),
]