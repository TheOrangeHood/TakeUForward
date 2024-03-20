from django.db import models

# Create your models here.


class CodeLanguage(models.TextChoices):
    CPP = "C++", "c++"
    PYTHON = "Python", "python"
    JAVA = "Java", "java"
    JAVASCRIPT = "Javascript", "javascript"


class CodeSnippetSubmission(models.Model):
    username = models.CharField(max_length=50)
    code_language = models.CharField(choices=CodeLanguage.choices, max_length=10)
    code_snippet = models.TextField()
    stdinput = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    stdoutput = models.TextField()

    def __str__(self) -> str:
        return self.username
