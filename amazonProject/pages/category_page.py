from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CategoryPage(BasePage):
    PRODUCT_TITLE = (By.XPATH, "(//span[@class='a-size-base-plus a-color-base a-text-normal'])[17]")
    SECOND_PAGE = (By.CSS_SELECTOR, "a.s-pagination-item.s-pagination-button[aria-label='2 sayfasına git']")
    SEARCH_TEXT = (By.CSS_SELECTOR, '.a-color-state')
    RESULTS_TEXT = (By.CSS_SELECTOR, "h2.a-size-medium-plus.a-spacing-none.a-color-base.a-text-bold:nth-of-type(1)")
    QUICKFILTER = (By.ID, "a-autoid-0-announce")
    expected_search_text = '"samsung"'
    expected_results_text = 'Sonuçlar'

    def click_second_page(self):
        # İkinci sayfaya tıklar.
        self.click_element(*self.SECOND_PAGE)

    def is_second_page_visible(self):
        # İkinci sayfanın görünür olup olmadığını kontrol eder.
        return self.is_element_visible(self.SECOND_PAGE)

    def is_second_page_clickable(self):
        # İkinci sayfanın tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.SECOND_PAGE)

    def click_product_and_get_title(self):
        # Ürün başlığını alır, başlığı yazdırır ve ürüne tıklar.
        product_title = self.get_text(self.PRODUCT_TITLE)
        print(f"Ürün Başlığı: {product_title}")
        self.click_element(*self.PRODUCT_TITLE)
        return product_title

    def is_product_title_clickable(self):
        # Ürün başlığının tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.PRODUCT_TITLE)

    def is_product_title_visible(self):
        # Ürün başlığının görünür olup olmadığını doğrular.
        return self.is_element_visible(self.PRODUCT_TITLE)

    def is_search_text_display(self):
        # Ürün başlığının görünür olup olmadığını kontrol eder. ("samsung")
        return self.get_text(self.SEARCH_TEXT)

    def is_results_text_display(self):
        # Sonuçlar başlığının var olup olmadığını kontrol eder.
        return self.get_text(self.RESULTS_TEXT)

    def is_quickfilter_visible(self):
        # Hızlı filtre butonunun görünür olup olmadığını kontrol eder.
        return self.is_element_visible(self.QUICKFILTER)

    def is_quickfilter_clickable(self):
        # Hızlı filtre butonunun tıklanılır olup olmadığını kontrol eder.
        return self.is_element_clickable(self.QUICKFILTER)
