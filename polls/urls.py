from django.urls import path
from . import views
app_name = 'polls'
#Sample Html Display
urlpatterns =[
  path('', views.index, name='index'),
  #detail--polls/1/
  path('<int:question_id>/',views.detail,name='detail'),
  #results--polls/1/results/
  path('<int:question_id>/results/',views.results,name='results'),
  #vote--polls/1/vote/
  path('<int:question_id>/vote/',views.vote,name='vote'),
]