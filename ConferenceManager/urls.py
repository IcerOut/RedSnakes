from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from ConferenceManager import api, views

urlpatterns = [
    path('', views.home, name='home'),
    path('conference-list/', views.conference_list, name='conference_list'),
    path('evaluation-results/', views.evaluation_results, name='evaluation_results'),
    path('submit-new-conference/', views.add_new_conference, name='submit_new_conference'),
    path('assign-reviewers/', views.assign_reviewers, name='assign_reviewers'),
    path('bidding/', views.bidding, name='bidding'),
    path('evaluation/', views.evaluation, name='evaluation'),
    path('review/', views.review, name='review'),
    path('section-choices/', views.section_choices, name='section_choices'),
    path('split-papers-into-sections/', views.split_papers_into_sections, name='split_papers_into_sections'),
<<<<<<< HEAD
=======
    path('chair-register/', views.chair_register, name='chair_register'),
    path('speaker-register/', views.speaker_register, name='speaker_register'),
    path('listner-register/', views.listener_register, name='listener_register'),

>>>>>>> 31cf69d94b75d27f4fdc17b0335034c9af2139aa
    path('api/conferences/getAll', api.conference_list, name='api_conference_list'),
    path('api/conferences/add', api.add_new_conference, name='add_new_conference'),
]