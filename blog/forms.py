from django.forms import ModelForm
from .models import BlogPost


class CreatBlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ("title", "authors", "body", "image",)
