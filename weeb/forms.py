from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'description', 'image', 'type']