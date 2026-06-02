"""
Locators for Category Page
"""

from selenium.webdriver.common.by import By


class CategoryLocators:
    """Category page locators"""

    # Categories section
    CATEGORY_SECTION = (
        By.XPATH,
        "//div[@class='left-sidebar']"
    )

    # Main categories
    WOMEN_CATEGORY = (
        By.XPATH,
        "//a[@href='#Women']"
    )

    MEN_CATEGORY = (
        By.XPATH,
        "//a[@href='#Men']"
    )

    KIDS_CATEGORY = (
        By.XPATH,
        "//a[@href='#Kids']"
    )

    # Women subcategories
    WOMEN_DRESS_SUBCATEGORY = (
        By.XPATH,
        "//div[@id='Women']//a[contains(text(),'Dress')]"
    )

    WOMEN_TOPS_SUBCATEGORY = (
        By.XPATH,
        "//div[@id='Women']//a[contains(text(),'Tops')]"
    )

    WOMEN_SAREE_SUBCATEGORY = (
        By.XPATH,
        "//div[@id='Women']//a[contains(text(),'Saree')]"
    )

    # Men subcategories
    MEN_TSHIRTS_SUBCATEGORY = (
        By.XPATH,
        "//div[@id='Men']//a[contains(text(),'Tshirts')]"
    )

    MEN_SHIRTS_SUBCATEGORY = (
        By.XPATH,
        "//div[@id='Men']//a[contains(text(),'Jeans')]"
    )

    # Products
    PRODUCT_ITEMS = (
        By.XPATH,
        "//div[contains(@class,'product-image-wrapper')]"
    )

    # Category title
    CATEGORY_TITLE = (
        By.XPATH,
        "//h2[@class='title text-center']"
    )