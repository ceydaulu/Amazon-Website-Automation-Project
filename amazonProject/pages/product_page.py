from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
    BACK_BREADCRUMB = (By.ID, 'breadcrumb-back-link')
    BUY_NOW_BUTTON = (By.ID, 'buy-now-button')
    PRODUCT_TITLE = (By.ID, 'productTitle')
    CART_COUNT = (By.ID, 'nav-cart-count')

    cart_count = '1'

    def is_add_to_cart_clickable(self):
        # 'Sepete Ekle' butonunun tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.ADD_TO_CART_BUTTON)

    def is_add_to_cart_visible(self):
        # 'Sepete Ekle' butonunun görünür olup olmadığını doğrular.
        return self.is_element_visible(self.ADD_TO_CART_BUTTON)

    def click_add_to_cart_button(self):
        # 'Sepete Ekle' butonuna tıklar.
        self.click_element(*self.ADD_TO_CART_BUTTON)

    def is_back_breadcrumb_present(self):
        # Sonuçlara dön metninin var olup olmadığını kontrol eder.
        return self.find(*self.BACK_BREADCRUMB)

    def is_back_breadcrumb_clickable(self):
        # Sonuçlara dön tıklanabilir olup olmadığını kontrol eder.
        return self.is_element_clickable(self.BACK_BREADCRUMB)

    def is_buy_now_button_visible(self):
        # 'Şimdi Al' butonunun görünür olup olmadığını kontrol eder.
        return self.is_element_visible(self.BUY_NOW_BUTTON)

    def is_buy_now_button_clickable(self):
        # 'Şimdi Al' butonunun tıklanılabilir olup olmadığını kontrol eder.
        return self.is_element_clickable(self.BUY_NOW_BUTTON)

    def get_product_page_title(self):
        # Ürün sayfasındaki başlığı alır ve yazdırır.
        product_page_title = self.get_text(self.PRODUCT_TITLE)
        print(f"Ürün Başlığı: {product_page_title}")
        return product_page_title

    def is_product_added(self):
        # Ürünün headerda sepete eklenip eklenmediğini kontrol eder.
        return self.get_text(self.CART_COUNT)
