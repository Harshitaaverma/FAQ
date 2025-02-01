import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_faq_api():
    client = APIClient()
    faq = FAQ.objects.create(question="What is Django?", answer="A web framework.")
    
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
    assert response.data[0]['question'] == "What is Django?"