from selenium.webdriver.common.by import By

AMAZON_URL = "https://www.amazon.com"

# Homepage
SEARCH_BOX = (By.ID, "twotabsearchtextbox")
SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

# Results Page
SORT_DROPDOWN = (By.ID, "s-result-sort-select")
FIRST_PRODUCT_LINK = (By.XPATH,"(//div[@data-component-type='s-search-result']//h2//a)[1]")
RESULTS_HEADER = (By.CSS_SELECTOR, "span.a-color-state.a-text-bold")  # e.g., "wireless mouse"

# Filters - Review Rating (4 Stars & Up)
REVIEW_4_STARS = (
    By.XPATH,
    "//section[@aria-label='4 Stars & Up']//a"
)
