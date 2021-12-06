from django.forms import Form
from .models import Comment


class CommentForm(Form):

    class Meta:
        model = Comment
        field = ['Comment']
