from rest_framework import serializers
from .models import CodeSnippetSubmission


class SnippetCreateOrDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeSnippetSubmission
        fields = ["username", "code_language", "code_snippet", "stdinput", "created_at", "stdoutput"]
        read_only_fields = ["stdoutput"]
