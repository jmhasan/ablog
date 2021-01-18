from django.urls import path
# from .import views
from .views import HomeView, ArticalDetailView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticalDetailView.as_view(), name='article-dtail'),

]
