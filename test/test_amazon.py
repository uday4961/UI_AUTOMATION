import pytest
from modules.amazon_module.amazon_page import AmazonMainPage


@pytest.mark.usefixtures("driver")
class TestAmazonPage:

    @pytest.fixture(autouse=True)
    def setup_page(self, request, driver):
        request.cls.page = AmazonMainPage(driver)
        request.cls.page.open_amazon_page()

    def test_search_product(self):
        self.page.enter_product("laptop")
        self.page.click_search()

    def test_sort_products(self):
        self.page.enter_product("laptop")
        self.page.click_search()
        self.page.sort_by("Price: Low to High")

    def test_filter_by_rating(self):
        self.page.enter_product("laptop")
        self.page.click_search()
        self.page.select_four_star_rating()

    def test_open_first_product(self):
        self.page.enter_product("laptop")
        self.page.click_search()
        self.page.click_first_product()
