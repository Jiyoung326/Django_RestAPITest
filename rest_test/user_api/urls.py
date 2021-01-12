from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserView.as_view()), #뒤에 아무것도 안 붙을 때, 처리해줄 곳
    path('<int:u_id>', views.UserView.as_view())#뒤에 u_id들어올 때, 처리해줄 곳
]