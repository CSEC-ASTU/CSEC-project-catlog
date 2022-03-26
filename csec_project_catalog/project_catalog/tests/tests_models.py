# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

from django.test import TestCase
from project_catalog.models import Image, Project, Rating, User


class ModelTestCases(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            password=",Yn#jjzbcd",
            email="111lennon@thebeatles.com",
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_valid_rating_creation(self):
        rating = Rating.objects.create(
            emoji="😀",
            created_by=self.user,
            deleted_by=self.user,
            is_deleted=False,
            id=2,
            created_at=28 / 11 / 2018,
        )
        self.assertEqual(rating.id, 2)

        self.assertEqual(rating.emoji, "😀")
        self.assertEqual(rating.created_by, self.user)
        self.assertTrue(rating.created_at, 28 / 11 / 2018)
        self.assertTrue(rating.is_deleted == False)
        self.assertEqual(rating.deleted_by, self.user)
        self.assertTrue(rating.updated_at != None)

    def test_valid_image_creation(self):
        image = Image.objects.create(
            id=1,
            created_by=self.user,
            is_deleted=False,
            deleted_by=self.user,
            created_at=28 / 11 / 2018,
        )
        self.assertEqual(image.id, 1)
        self.assertEqual(image.created_by, self.user)
        self.assertTrue(image.created_at, 28 / 11 / 2018)
        self.assertTrue(image.is_deleted == False)
        self.assertEqual(image.deleted_by, self.user)
        self.assertTrue(image.updated_at != None)

    def test_valid_project_creation(self):
        project = Project.objects.create(
            id=1,
            title="sniuke ksjh",
            description="#7777opowoe",
            github_link="https://github.com/CSEC-ASTU/CSEC-project-catlog",
            created_by=self.user,
            is_deleted=False,
            deleted_by=self.user,
            created_at=28 / 11 / 2018,
        )
        self.assertEqual(project.id, 1)
        self.assertEqual(project.title, "sniuke ksjh")
        self.assertEqual(project.description, "#7777opowoe")
        self.assertEqual(
            project.github_link, "https://github.com/CSEC-ASTU/CSEC-project-catlog"
        )
        self.assertTrue(project.project_link is not None)
        self.assertEqual(project.created_by, self.user)
        self.assertTrue(project.created_at, 28 / 11 / 2018)
        self.assertTrue(project.is_deleted is False)
        self.assertEqual(project.deleted_by, self.user)
        self.assertTrue(project.updated_at is not None)
