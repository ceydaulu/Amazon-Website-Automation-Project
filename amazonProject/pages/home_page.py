from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    COOKIE_BUTTON = (By.ID, 'sp-cc-accept')
    SEARCH_TEXTBOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ACCOUNT_TEXT = (By.ID, 'nav-link-accountList-nav-line-1')
    CART_BUTTON = (By.ID, 'nav-cart')
    ORDER_BUTTON = (By.ID, 'nav-orders')
    BEST_SELLERS_BUTTON = (By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
    TODAYS_DEALS_BUTTON = (By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_gb']")
    NEW_RELEASES_BUTTON = (By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_newreleases']")

    expected_account_text = 'Merhaba, Giriş yapın'
    expected_cart_text = 'Alışveriş'
    expected_orders_text = 'İadeler'
    expected_best_sellers_text = 'Çok Satanlar'
    expected_todays_deals_text = 'Günün Fırsatları'
    expected_new_releases_text = 'Yeni Çıkanlar'

    def is_cookie_button_clickable(self):
        # Çerezler butonunun tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.COOKIE_BUTTON)

    def is_cookie_button_visible(self):
        # Çerezler butonunun görünür olup olmadığını kontrol eder.
        return self.is_element_visible(self.COOKIE_BUTTON)

    def click_cookie_button(self):
        # Çerezler butonuna tıklar.
        self.click_element(*self.COOKIE_BUTTON)

    def is_search_textbox_visible(self):
        # Arama metin kutusunun görünür olup olmadığını kontrol eder.
        return self.is_element_visible(self.SEARCH_TEXTBOX)

    def is_search_textbox_clickable(self):
        # Arama metin kutusunun tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.SEARCH_TEXTBOX)

    def click_search_textbox(self):
        # Arama metin kutusuna tıklar.
        self.click_element(*self.SEARCH_TEXTBOX)

    def send_search_textbox(self, text):
        # Arama metin kutusuna metin gönderir.
        self.send_text(text, *self.SEARCH_TEXTBOX)

    def click_search_icon(self):
        # Arama ikonuna tıklar.
        self.click_element(*self.SEARCH_ICON)

    def is_search_icon_visible(self):
        # Arama ikonunun görünür olup olmadığını kontrol eder.
        return self.is_element_visible(self.SEARCH_ICON)

    def is_search_icon_clickable(self):
        # Arama ikonunun tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.SEARCH_ICON)

    def is_account_text_display(self):
        # Hesap metninin var olup olmadığını kontrol eder.
        return self.get_text(self.ACCOUNT_TEXT)

    def is_cart_visible(self):
        # Sepet butonunun görünür olup olmadığını kontrol eder.
        return self.is_element_visible(self.CART_BUTTON)

    def is_cart_text_display(self):
        # Sepet metninin var olup olmadığını kontrol eder.
        return self.get_text(self.CART_BUTTON)

    def is_cart_clickable(self):
        # Sepet butonunun tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.CART_BUTTON)

    def is_orders_visible(self):
        # Siparişler butonunun görünür olup olmadığını kontrol eder.
        return self.is_element_visible(self.ORDER_BUTTON)

    def is_orders_clickable(self):
        # Siparişler butonunun tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.ORDER_BUTTON)

    def is_orders_text_display(self):
        # Siparişler metninin var olup olmadığını kontrol eder.
        return self.get_text(self.ORDER_BUTTON)

    def is_best_sellers_visible(self):
        # Çok Satanlar butonunun görünür olup olmadığını kontrol eder.
        return self.is_element_visible(self.BEST_SELLERS_BUTTON)

    def is_best_sellers_clickable(self):
        # Çok Satanlar butonunun tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.BEST_SELLERS_BUTTON)

    def is_best_sellers_text_display(self):
        # Çok Satanlar metninin var olup olmadığını kontrol eder.
        return self.get_text(self.BEST_SELLERS_BUTTON)

    def is_todays_deals_visible(self):
        # Günün Fırsatları butonunun görünür olup olmadığını kontrol eder.
        return self.is_element_visible(self.TODAYS_DEALS_BUTTON)

    def is_todays_deals_clickable(self):
        # Günün Fırsatları butonunun tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.TODAYS_DEALS_BUTTON)

    def is_todays_deals_text_display(self):
        # Günün Fırsatları metninin var olup olmadığını kontrol eder.
        return self.get_text(self.TODAYS_DEALS_BUTTON)

    def is_new_releases_visible(self):
        # Yeni Çıkanlar butonunun görünür olup olmadığını kontrol eder.
        return self.is_element_visible(self.NEW_RELEASES_BUTTON)

    def is_new_releases_clickable(self):
        # Yeni Çıkanlar butonunun tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.NEW_RELEASES_BUTTON)

    def is_new_releases_text_display(self):
        # Yeni Çıkanlar metninin var olup olmadığını kontrol eder.
        return self.get_text(self.NEW_RELEASES_BUTTON)

