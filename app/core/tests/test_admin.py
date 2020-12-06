from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse # to generate urls for admin page.


class AdminSiteTests(TestCase):

    def setUp(self):
        # use to create test client, new user to test out tests
        # make sure user is logged in
        # create non authenticated user for trsting
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email ='admintest@testing.com',
            password = 'test123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@testing.com',
            password='test123',
            name='Test name'
        )

    def test_for_user_listed(self):
        """Test that users are listed in users list"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url) # for response
        # this is to perform HTTP get on our URL

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """ TEST that the user edit page works"""
        url = reverse('admin:core_user_change',args=[self.user.id])
        # url will be -- /admin/core/user/1/
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        # 200 for ok http call.

    def test_create_user_page(self):
        """TEST that create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
