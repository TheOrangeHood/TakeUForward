from django.urls import path
from .views import *

# BASE_URL = api/


urlpatterns = [
    path("snippets", SnippetSubmissionListOrCreateView.as_view(), name="snippets")
]
