from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIview, ArticleDetails, GenericAPIView, ArticleViewset

#routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewset, basename='article')



urlpatterns = [
    #function based view
    path('article/', article_list, name="list" ),
    path('article/<int:pk>/', article_detail, name="list" ),
    #class based view
    path('', ArticleAPIview.as_view()),
    path('<int:id>/', ArticleDetails.as_view()),
    #generic view
    path('generic/', GenericAPIView.as_view()),
    path('generic/<int:id>/', GenericAPIView.as_view()),
    #viewset
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    

]