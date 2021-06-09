from django.db import models
from django.conf import settings
import datetime
from django.utils import timezone

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
# 디렉터랑 액터는 credit으로 받아옴. 얘네 둘은 어차피 한 API로 호출 가능하니까 한번만 할까?
# 가능할까?
# class Director(models.Model):
#     name = models.CharField(max_length=100)
# class Actor(models.Model):
#     name = models.CharField(max_length=100)

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    # 상세정보나, 유튜브에서 예고편 들고오려면 id값 필요한듯.
    movie_id = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    # directors = models.ManyToManyField(Director)
    # actors = models.ManyToManyField(Actor)
    vote_average = models.FloatField(default=0)
    rank_total = models.FloatField(default=0)
    rank_average = models.FloatField(default=0)
    trailer = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    netflix = models.TextField(default='')
    watcha = models.TextField(default='')
    wavve = models.TextField(default='')
    naver = models.TextField(default='')
    release_date = models.DateField()
    clicked = models.IntegerField(default=0)
    last_cliked_time = models.DateTimeField(default=timezone.make_aware(datetime.datetime.strptime("2021-05-18 16:30:30", '%Y-%m-%d %H:%M:%S')))
    def __str__(self):
        return self.title


class NowShowingMovie(models.Model):
    movieNm = models.CharField(max_length=100)
    openDt = models.DateField()
    audiAcc = models.CharField(max_length=100)
    image_path = models.CharField(max_length=100)
    userRating = models.FloatField()
    def __str__(self):
        return self.movieNm


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    title = models.CharField(max_length=15)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    # 얘를 movie_pk로 해야하나.
    rank = models.FloatField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def username(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content
    def username(self):
        return self.user.username


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='votes')
    title = models.CharField(max_length=100)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def username(self):
        return self.user.username


class VoteComment(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='votecomments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vote_comments')
    choice = models.IntegerField()
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content
    def username(self):
        return self.user.username

