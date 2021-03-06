from django.test import TestCase
from .models import Post, Comment


class TestItemModel(TestCase):
    
    #test to check blog post can be created
    def test_can_create_a_blog_post_with_title_content_created_date_published_date_views_tag_and_image(self):
        blog = Post(title='test',content='test',views='1', tag='test' )
        blog.save()
        self.assertEqual(str(blog.title), 'test')
        self.assertEqual(str(blog.content), 'test')
        self.assertEqual(str(blog.views), '1')
        self.assertEqual(str(blog.tag), 'test')


   
