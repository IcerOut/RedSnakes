from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from ConferenceManager.views import *
from ConferenceManager.models import *
import json

class TestUrls(SimpleTestCase):
    
    def test_home(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_conference_list(self):
        url = reverse('conference_list')
        self.assertEquals(resolve(url).func, conference_list)

    def test_evaluation_results(self):
        url = reverse('evaluation_results')
        self.assertEquals(resolve(url).func, evaluation_results)

    def test_assign_reviewers(self):
        url = reverse('assign_reviewers')
        self.assertEquals(resolve(url).func, assign_reviewers)

    def test_bidding(self):
        url = reverse('bidding')
        self.assertEquals(resolve(url).func, bidding)

    def test_evaluation(self):
        url = reverse('evaluation')
        self.assertEquals(resolve(url).func, evaluation)

    def test_review(self):
        url = reverse('review')
        self.assertEquals(resolve(url).func, review)

    def test_section_choices(self):
        url = reverse('section_choices')
        self.assertEquals(resolve(url).func, section_choices)
    
    def test_split_papers_into_sections(self):
        url = reverse('split_papers_into_sections')
        self.assertEquals(resolve(url).func, split_papers_into_sections)

    def test_chair_register(self):
        url = reverse('chair_register')
        self.assertEquals(resolve(url).func, chair_register)

    def test_speaker_register(self):
        url = reverse('speaker_register')
        self.assertEquals(resolve(url).func, speaker_register)

    def test_listener_register(self):
        url = reverse('listener_register')
        self.assertEquals(resolve(url).func, listener_register)

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.conference_list_url = reverse('conference_list')
        self.chair_register_url = reverse('chair_register')
        self.speaker_register_url = reverse('speaker_register')
        self.listener_register_url = reverse('listener_register')
        self.evaluation_results_url = reverse('evaluation_results')
        self.assign_reviewers_url = reverse('assign_reviewers')
        self.bidding_url = reverse('bidding')

    def test_home(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_conference_list(self):
        response = self.client.get(self.conference_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'conference-list.html')

    def test_chair_register(self):
        response = self.client.get(self.chair_register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'chair-register.html')

    def test_speaker_register(self):
        response = self.client.get(self.speaker_register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'speaker-register.html')

    def test_listener_register(self):
        response = self.client.get(self.listener_register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'listener-register.html')

    def test_assign_reviewers(self):
        response = self.client.get(self.assign_reviewers_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'assign-reviewers.html')

    def test_evaluation_results(self):
        response = self.client.get(self.evaluation_results_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'evaluation-results.html')

    def test_bidding(self):
        response = self.client.get(self.bidding_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bidding.html')    
