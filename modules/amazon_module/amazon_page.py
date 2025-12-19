from base.selenium_base import SeleniumBase
from resource.automation_data.Automation_website_page_data import *

class AmazonMainPage(SeleniumBase):

    def open_amazon_page(self):
        self.driver.get(AMAZON_URL)

    # ---------------- SEARCH ----------------
    def enter_product(self, product_name):
        self.send_keys(SEARCH_BOX, product_name)

    def click_search(self):
        self.click(SEARCH_BUTTON)

    # ---------------- PRODUCT ----------------
    def click_first_product(self):
        self.wait.until(lambda d: len(d.find_elements(*FIRST_PRODUCT_LINK)) > 0)
        self.click(FIRST_PRODUCT_LINK)

    # ---------------- DROPDOWN ----------------
    def sort_by(self, visible_text):
        self.select_by_text(SORT_DROPDOWN, visible_text)

    # ---------------- RADIO BUTTON ----------------
    def select_four_star_rating(self):
        self.select_radio(REVIEW_4_STARS)
