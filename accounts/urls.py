from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('signup/', views.singup, name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html',form_class=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("create-sub/", views.create_sub, name="create sub"), 
    path("complete/", views.complete, name="complete"), 
]