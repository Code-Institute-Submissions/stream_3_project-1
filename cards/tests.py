from django.test import TestCase

# Create your tests here.

class TestCardViews(TestCase):
    
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
    def test_get_browse_all_cards_page(self):
        page = self.client.get("/cards/all_cards")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cards.html")
        
    def test_categorys_page_for_a_category_that_does_not_exist(self):
        page = self.client.get("/categories/1600")
        self.assertEqual(page.status_code, 404)
