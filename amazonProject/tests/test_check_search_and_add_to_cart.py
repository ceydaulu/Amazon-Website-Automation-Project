import time

from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from tests.base_test import BaseTest


""" Amazon Add To Cart Functionality(Guest User)
1-Amazon anasayfasının Url gidilir. -> Expected result: Anasayfanın açıldığı doğrulanır. Sayfa elementlerin tıklanılabilir ve görünür olduğu doğrulanır.
2-Çerez pop-up'ında 'Kabul et' butonuna tıklanır. -> Expected result: çerez butonunda kabul et butonunun görünür ve tıklanılır olduğu, 'Kabul et' butonuna basıldıktan sonra pop-up'ın kaybolduğu doğrulanır.
3-Search alanına tıklanır. -> Search alanın tıklanılır olduğu doğrulanır.
4-Search alanına 'samsung' yazılır. -> 'samsung' kelimesinin doğru yazıldığı ve arama kutusunda göründüğü doğrulanır.
5-Arama ikonuna tıklanır. -> Arama ikonun görünür ve tıklanılır olduğu doğrulanır. Kategori sayfasına gidildiği doğrulanır. Kategori sayfasına geçildiği ve arama sonucunda 'Samsung' ürünlerinin listelendiği doğrulanır.
6-Sayfanın alt kısmında bulunan '2' sayısına tıklanır. -> 2.Sayfaya gelindiği doğrulanır.
7-5.satır 1.sütundakıo ürün tıklanır. -> Ürüne başarılı bir şekilde tıklanır, product sayfasına yönlendirilir ve kategori sayfasındaki ürün başlığı ile product sayfasındaki başlıkların aynı olduğu doğrulanır.
8-Sepete ekle butonuna tıklanır. -> Sepete Ekle butonunun çalıştığı, ürünün sepete eklendiği ve sepet sayfasına yönlendirildiği doğrulanır. Sepetteki ürün sayısının güncellendiği doğrulanır.
9-Logo'ya tıklanır. -> Logonun görünür ve tıklanılır olduğu doğrulanır ve anasayfaya yönlendirdiği doğrulanır.

"""

class TestAmazonSearchAndCart(BaseTest):
    def test_check_amazon_add_to_cart(self):
        home_page = HomePage(self.driver)
        self.assertEqual(self.base_url, home_page.get_current_url(), "Amazon Anasayfa Açılmadı")
        self.assertEqual(self.driver.title, self.expected_title, "Sayfa başlığı beklendiği gibi değil")
        home_page.is_cookie_button_visible()
        home_page.is_cookie_button_clickable()
        home_page.click_cookie_button()
        time.sleep(3)
        self.assertEqual(home_page.expected_account_text, home_page.is_account_text_display(),
                         "Hesap girişi metni beklendiği gibi değil veya bulunamadı.")
        home_page.is_cart_visible()
        home_page.is_cart_clickable()
        self.assertIn(home_page.expected_cart_text, home_page.is_cart_text_display(),
                      "Sepet yazısı yanlış.")
        home_page.is_orders_visible()
        home_page.is_orders_clickable()
        self.assertIn(home_page.expected_orders_text, home_page.is_orders_text_display(),
                      "İadeler yazısı yanlış.")
        home_page.is_best_sellers_visible()
        home_page.is_best_sellers_clickable()
        self.assertEqual(home_page.expected_best_sellers_text, home_page.is_best_sellers_text_display(),
                         "Çok Satanlar yazısı yanlış.")
        home_page.is_todays_deals_visible()
        home_page.is_todays_deals_clickable()
        self.assertEqual(home_page.expected_todays_deals_text, home_page.is_todays_deals_text_display(),
                         "Günün Fırsatları yazısı yanlış.")
        home_page.is_new_releases_visible()
        home_page.is_new_releases_clickable()
        self.assertEqual(home_page.expected_new_releases_text, home_page.is_new_releases_text_display(),
                         "Yeni Çıkanlar yazısı yanlış.")
        home_page.is_search_textbox_visible()
        home_page.is_search_textbox_clickable()
        home_page.click_search_textbox()
        home_page.send_search_textbox("samsung")
        home_page.is_search_icon_visible()
        home_page.is_search_icon_clickable()
        home_page.click_search_icon()

        category_page = CategoryPage(self.driver)
        time.sleep(3)
        self.assertEqual(category_page.expected_results_text, category_page.is_results_text_display(),
                         "Kategori sayfası açılamadı.")
        self.assertEqual(category_page.expected_search_text, category_page.is_search_text_display(),
                         "Kategori sayfasına aratılan ürün doğru aratılmadı.")
        category_page.is_quickfilter_visible()
        category_page.is_quickfilter_clickable()
        category_page.is_second_page_visible()
        category_page.is_second_page_clickable()
        category_page.click_second_page()
        category_page.is_second_page_visible()
        category_page.is_second_page_clickable()
        category_page.is_product_title_visible()
        category_page.is_product_title_clickable()
        category_page_title = category_page.click_product_and_get_title()

        time.sleep(3)
        product_page = ProductPage(self.driver)
        self.assertTrue(product_page.is_back_breadcrumb_present(),
                        "Product sayfasında değilsin.")
        product_page.is_back_breadcrumb_clickable()
        product_page_title = product_page.get_product_page_title()
        self.assertEqual(category_page_title, product_page_title, "Ürün başlıkları eşleşmiyor.")
        product_page.is_buy_now_button_visible()
        product_page.is_buy_now_button_clickable()
        product_page.is_add_to_cart_visible()
        product_page.is_add_to_cart_clickable()
        product_page.click_add_to_cart_button()
        self.assertIn(product_page.cart_count, product_page.is_product_added(),
                      "Sepete ürün doğru eklenmedi.")

        cart_page = CartPage(self.driver)
        self.assertIn(cart_page.expected_proceed_button_text, cart_page.is_proceed_button_present(),
                      "Sepet sayfasında değilsin.")
        cart_page.is_proceed_button_visible()
        cart_page.is_proceed_button_clickable()
        cart_page.is_cart_button_visible()
        cart_page.is_cart_button_clickable()
        self.assertIn(cart_page.expected_cart_button_text, cart_page.is_cart_button_present(),
                      "Sepete Git yazısı hatalı.")
        cart_page.is_signin_text_visible()
        cart_page.is_signin_text_clickable()
        self.assertIn(cart_page.expected_sign_in_text, cart_page.is_signin_text_present(),
                      "En iyi deneyim için hesabınızda oturum açın yazısı bulunmuyor.")
        cart_page.is_main_header_logo_visible()
        cart_page.is_main_header_logo_clickable()
        cart_page.click_main_header_logo()
        time.sleep(3)
