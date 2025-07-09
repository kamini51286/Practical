from pages.login_page import LoginPage
from utils.screenshot_util import take_screenshot

def test_title(browser):
    print("Page title is:", browser.title)
    assert "Test Login | Practice Test Automation" in browser.title

# def test_valid_login(browser,request):
#     test_name = request.node.name
#     login_page = LoginPage(browser)
#     login_page.login("student", "Password123")
#     take_screenshot(browser, test_name)

#     assert "Logged In Successfully" in browser.page_source

# def test_invalid_username(browser):
#     login_page = LoginPage(browser)
#     login_page.login("wronguser", "Password123")
#     assert login_page.get_error_message() == "Your username is invalid!"

# def test_invalid_password(browser):
#     login_page = LoginPage(browser)
#     login_page.login("student", "wrongpass")
#     assert login_page.get_error_message() == "Your password is invalid!"

# def test_logout(browser):
#     login_page = LoginPage(browser)
#     login_page.logout("student", "Password123")
#     assert "Test login" in browser.page_source 

