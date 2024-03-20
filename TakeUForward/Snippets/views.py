# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .custom_cache import custom_cache

from .models import CodeSnippetSubmission

from .serializers import SnippetCreateOrDetailSerializer

# Create your views here.


def custom_success_response(data):
    return Response({"status": "success", "payload": data}, status=status.HTTP_200_OK)


def custom_fail_response(data):
    return Response(
        {"status": "fail", "message": data}, status=status.HTTP_422_UNPROCESSABLE_ENTITY
    )


class SnippetSubmissionListOrCreateView(APIView):
    def get(self, request, *args, **kwargs):
        cached_snippets_data = custom_cache.get('snippets_data')

        if cached_snippets_data is not None:
            return custom_success_response(cached_snippets_data)
        
        else:
            snippets_submissions = CodeSnippetSubmission.objects.all()
            snippets_data = SnippetCreateOrDetailSerializer(
                snippets_submissions, many=True
            ).data
            custom_cache.set('snippets_data', snippets_data)
            return custom_success_response(snippets_data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = SnippetCreateOrDetailSerializer(data=data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            custom_cache.delete('snippets_data')
            return custom_success_response(serializer.data)
        else:
            return custom_fail_response(serializer.errors)
