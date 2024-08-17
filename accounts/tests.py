from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomeUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="will",
            email="will@gmail.com",
            password="testpass123"
        )

        self.assertEqual(user.username, "will")
        self.assertEqual(user.email, "will@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin", 
            email="superadmin@gmail.com", 
            password="testpass123"
        )

        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@gmail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    
    def test_update_user(self):
        User = get_user_model()
        update_user = User.objects.create_user(
            username="user", 
            email="user@email.com", 
            password="testpass123"
        )

        update_user.username = "userupdate"
        update_user.email = "userupdate@email.com"

        self.assertEqual(update_user.username, "userupdate")
        self.assertEqual(update_user.email, "userupdate@email.com")