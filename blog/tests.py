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
        post.image = "test_image.jpg"

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
        self.assertEquals(test_post.image_file(), post.image)
        self.assertEquals(test_post.favorited, 0)
        self.assertEquals(test_post.times_favorited(), "")

    def test_user_can_only_favorite_once(self):
        post = Post()

    def test_post_favorited_returns_correct_value(self):

        post_no_favorites = Post()
        post_no_favorites.title = "I have no favorites"
        post_no_favorites.save()

        self.assertEqual(post_no_favorites.favorited, 0)
        self.assertEqual(post_no_favorites.times_favorited(), "")

        post_with_2_favorites = Post()
        post_with_2_favorites.title = "Two people like me"
        post_with_2_favorites.favorited = 2
        post_with_2_favorites.save()

        self.assertEqual(post_with_2_favorites.favorited, 2)
        self.assertEqual(post_with_2_favorites.times_favorited(), 2)