from django.test import TestCase
from datetime import date
from .models import Post

# Create your tests here.
class PostTest(TestCase):

    def test_create_post(self):
        # Create post and set attributes
        post = Post()
        post.title = "Post Title"
        post.text = "Here the blog post content"

        # Save the post
        post.save()

        # Check post was saved
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        test_post = all_posts[0]
        self.assertEquals(test_post, post)

        # Check attributes
        self.assertEquals(test_post.title, post.title)
        self.assertEqual(test_post.text, post.text)
        self.assertEquals(test_post.published, date.today())

