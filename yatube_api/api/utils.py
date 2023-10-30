from django.shortcuts import get_object_or_404

from posts.models import Post


def get_post(self):
    return get_object_or_404(Post, id=self.kwargs.get('post_id'))
