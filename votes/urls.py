from django.urls import path
from . import views

app_name = 'votes'
urlpatterns = [
    path('', views.index, name='index'),

    path('<int:partylist_id>/<int:candidate_id>', views.detail_candidate, name='detail_candidate'),
    # path('<int:partylist_id>/', views.detail_candidate, name='detail_candidate'),

    # path('<int:position_id>/', views.detail_candidate, name='detail_candidate'),
    # path('<int:position_id>/', views.detail_candidate, name='detail_candidate'),

    path('<int:candidate_id>/vote', views.vote, name='vote'),

    path('create_partylist/', views.create_partylist, name='create_partylist'),
    # path('<int:partylist_id>/update_partylist/', views.update_partylist, name='update_partylist'),
    # path('<int:partylist_id>/delete_partylist/', views.delete_partylist, name='delete_partylist'),
    #
    path('create_position/', views.create_position, name='create_position'),
    # path('<int:position_id>/update_position/', views.update_position, name='update_position'),
    # path('<int:position_id>/delete_position/', views.delete_position, name='delete_position'),
    #
    path('create_candidate/', views.create_candidate, name='create_candidate'),
    path('<int:candidate_id>/update_candidate', views.update_candidate, name='update_candidate'),
    # path('<int:candidate_id>/delete_candidate', views.delete_candidate, name='delete_candidate'),


#


    path('register/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]
