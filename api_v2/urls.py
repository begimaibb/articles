from django.urls import path

from api_v2.views import ArticleView, ArticleCrudView

app_name = "api_v2"


urlpatterns = [
    path("articles/", ArticleView.as_view()),
    path("articles/<int:pk>/", ArticleView.as_view()),
    path("article/<int:pk>/", ArticleCrudView.as_view())
]