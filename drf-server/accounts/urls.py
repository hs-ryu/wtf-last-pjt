from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('verify-user/', views.verify_user),
    path('<username>/', views.profile, name='profile'),
    path('userinfo/<int:user_id>/', views.userinfo),
    path('deleteaccount/<int:user_id>/', views.deleteaccount)
]
