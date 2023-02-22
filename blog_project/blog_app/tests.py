from django.test import TestCase
from blog_app.models import Post
from django.contrib.auth.models import User

class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        
    def test_create_post(self):
        post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user
        )
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'This is a test post.')
        self.assertEqual(post.author, self.user)
        
    def test_update_post(self):
        post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user
        )
        new_title = 'Updated Test Post'
        new_content = 'This is an updated test post.'
        post.title = new_title
        post.content = new_content
        post.save()
        updated_post = Post.objects.get(pk=post.pk)
        self.assertEqual(updated_post.title, new_title)
        self.assertEqual(updated_post.content, new_content)

    def test_delete_post(self):
        post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user
        )
        post.delete()
        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(pk=post.pk)