from django.urls import path

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
    path('split-papers-into-sections/', views.split_papers_into_sections,
         name='split_papers_into_sections'),

    path('chair-register/', views.chair_register, name='chair_register'),
    path('speaker-register/', views.speaker_register, name='speaker_register'),
    path('listener-register/', views.listener_register, name='listener_register'),

    path('api/conferences/getAll', api.conference_list, name='api_conference_list'),
    path('api/conferences/add', api.add_new_conference, name='add_new_conference'),
    path('api/conferences/get?id=', api.get_conference_by_id, name='get_conference_by_id'),
    path('api/conferences/signUp', api.sign_up, name='sign_up'),
    path('api/file_upload', api.file_upload, name='file_upload'),
    path('api/conferences/getSections', api.get_all_sections, name='get_all_sections'),

    path('api/papers/add', api.add_new_paper, name='add_new_paper'),
    path('api/papers/getAll', api.get_all_papers, name='get_all_papers'),
    path('api/papers/get?id=', api.find_paper, name='find_paper'),
    path('api/papers/sendAbstract', api.add_new_abstract, name='add_new_abstract'),

    path('api/reviews/add', api.add_new_review, name='add_new_review'),
    path('api/reviews/getAll', api.get_all_reviews, name='get_all_reviews'),
    path('api/reviews/sendBidding', api.add_new_bid, name='add_new_bid')
]
