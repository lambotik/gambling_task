from main_page import MainPage


def test_task(driver):
    page = MainPage(driver, MainPage.link)
    page.open()
    page.login_user()
    page.check_user_icon_name()
    widget_title = page.select_game()
    assert widget_title == 'Astro Wild', 'Should be open game Astro Wild.'
