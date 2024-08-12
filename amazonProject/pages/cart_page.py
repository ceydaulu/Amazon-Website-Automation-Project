from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    PROCEED_BUTTON_CHECKOUT = (By.CLASS_NAME, 'sc-without-multicart')
    MAIN_LOGO = (By.ID, 'nav-logo-sprites')
    CART_BUTTON = (By.CSS_SELECTOR, 'span.a-button-inner > a.a-button-text')
    SIGNIN_TEXT = (By.CSS_SELECTOR, "#sw-atc-buy-box-sign-in-message a.a-link-normal")

    expected_proceed_button_text = 'Alışverişi Tamamla'
    expected_cart_button_text = 'Sepete Git'
    expected_sign_in_text = 'hesabınızda oturum açın'

    def is_proceed_button_present(self):
        # 'Alışverişi Tamamla' butonunun metninin var olup olmadığını kontrol eder.
        return self.get_text(self.PROCEED_BUTTON_CHECKOUT)

    def is_proceed_button_clickable(self):
        # 'Alışverişi Tamamla' butonunun tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.PROCEED_BUTTON_CHECKOUT)

    def is_proceed_button_visible(self):
        # 'Alışverişi Tamamla' butonunun görünür olup olmadığını doğrular.
        return self.is_element_visible(self.PROCEED_BUTTON_CHECKOUT)

    def is_signin_text_present(self):
        # 'hesabınızda oturum açın' metninin var olup olmadığını kontrol eder. (Guest User)
        return self.get_text(self.SIGNIN_TEXT)

    def is_signin_text_clickable(self):
        # 'hesabınızda oturum açın' metninin tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.SIGNIN_TEXT)

    def is_signin_text_visible(self):
        # 'hesabınızda oturum açın' metninin görünür olup olmadığını doğrular.
        return self.is_element_visible(self.SIGNIN_TEXT)

    def is_cart_button_clickable(self):
        # Sepete Git butonunun tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.CART_BUTTON)

    def is_cart_button_visible(self):
        # Sepete git butonunun görünür olup olmadığını kontrol eder.
        return self.is_element_visible(self.CART_BUTTON)

    def is_cart_button_present(self):
        # Sepete git butonunun metninin var olup olmadığını kontrol eder.
        return self.get_text(self.CART_BUTTON)

    def click_main_header_logo(self):
        # Ana başlık logosuna tıklar.
        self.click_element(*self.MAIN_LOGO)

    def is_main_header_logo_visible(self):
        # Ana başlık logosunun görünür olup olmadığını kontrol eder.
        return self.is_element_visible(self.MAIN_LOGO)

    def is_main_header_logo_clickable(self):
        # Ana başlık logosunun tıklanabilir olup olmadığını doğrular.
        return self.is_element_clickable(self.MAIN_LOGO)
