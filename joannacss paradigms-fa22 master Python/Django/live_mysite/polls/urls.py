from django.urls import path
from . import views

app_name = 'polls'  # used to define the application namespace
                    # this way, you can refer to a url using app_name:url_name (ex: polls:detail)


urlpatterns = [
    # ex: /polls/
    path('',views.IndexView.as_view(), name='index'),                                
    
    # ex: /polls/5/
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='detail'),   
    
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), 
    
    # ex: /polls/5/vote/
    path('<int:pk>/vote/', views.vote, name='vote'),             
]
