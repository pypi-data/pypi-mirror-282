
### Step 6: Create Test Cases in `tests/test_models.py`

# tests/test_models.py

from django.test import TestCase
from desmy_python.models import DesmyManager
from models import MyModel  # Update with your actual app name

class DesmyManagerTest(TestCase):
    def setUp(self):
        self.model = MyModel.objects.create(name="Test", description="Test description")

    def test_create(self):
        obj = MyModel.objects.create(name="New", description="New description")
        self.assertIsNotNone(obj)

    def test_createOrUpdate(self):
        obj, created = MyModel.objects.createOrUpdate(name="Test", defaults={'description': 'Updated description'})
        self.assertFalse(created)
        self.assertEqual(obj.description, 'Updated description')
        
    def test_delete(self):
        MyModel.objects.delete(id=self.model.id)
        self.assertFalse(MyModel.objects.filter(id=self.model.id).exists())

    def test_read(self):
        obj = MyModel.objects.read(name="Test").first()
        self.assertIsNotNone(obj)

    def test_readWithPaginated(self):
        page = MyModel.objects.readWithPaginated(page=1, per_page=1, search_query="Test")
        self.assertEqual(len(page), 1)

    def test_update(self):
        MyModel.objects.update(pk=self.model.id, description="Updated description")
        obj = MyModel.objects.get(id=self.model.id)
        self.assertEqual(obj.description, "Updated description")
