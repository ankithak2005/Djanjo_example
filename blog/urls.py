from django.urls import path
from blog import views

urlpatterns=[
    path('',views.index,name='index'),
    path('post_details/<int:id>',views.post_details,name='post_details'),
    path('resume',views.resume,name='resume'),
    path('post_details_in_html/<int:post_id>',views.post_details_in_html,name='post_details_in_html'),
    path('indexhtml',views.indexhtml,name='indexhtml'),
    path('get/<int:p_id>',views.dbaccess,name='dbaccess'),
]