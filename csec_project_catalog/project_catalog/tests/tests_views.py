# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
import email
from django.test import TestCase

from project_catalog.models import Rating
from authentication.models import User


class ModelTestCases(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            password=",Yn#jjzbcd",
            email="lennon@thebeatles.com",
            phone_number="+251912345678",
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_valid_rating_creation(self):
        rating = Rating.objects.create(
            emoji="😀",
            created_by=self.user,
            is_deleted=False,
        )
        self.assertEqual(rating.emoji, "😀")
        self.assertEqual(rating.created_by, self.user)
        self.assertTrue(rating.created_at is not None)
        self.assertTrue(rating.is_deleted is False)
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
import email
from django.test import TestCase

from project_catalog.models import Rating
from authentication.models import User


class ModelTestCases(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            password=",Yn#jjzbcd",
            email="lennon@thebeatles.com",
            phone_number="+251912345678",
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_valid_rating_creation(self):
        rating = Rating.objects.create(
            emoji="😀",
            created_by=self.user,
            is_deleted=False,
        )
        self.assertEqual(rating.emoji, "😀")
        self.assertEqual(rating.created_by, self.user)
        self.assertTrue(rating.created_at is not None)
        self.assertTrue(rating.is_deleted is False)