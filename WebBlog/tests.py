from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

# Create your tests here.
class BlogTests(TestCase):

    def setUp(self):        # bu user yaratish uchun testing strukturasi
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret'
        )
                        #bu post yaratishdagi testing strukturasi
        self.post = Post.objects.create(
            title='New post',
            body='Text of post',
            author=self.user,
        )
                # bu sarlavhani özini qaytarib turish edi boshidagi öshani test qilyapti
    def test_string_representation(self):
        post = Post(title='Text of post')
        self.assertEqual(str(post), post.title)
                        # va bu endi tekshirib boshlaydi tepadagi berilgan struktura böyicha
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'New post')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Text of post')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Text of post')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Text of post')
        self.assertTemplateUsed(response, 'post_detail.html')
    