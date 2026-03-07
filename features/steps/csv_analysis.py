from behave import given, when, then

@given('I am on the login page')
def step_impl(context):
 #   context.login_page = LoginPage(context.driver)
    context.login_page.navigate_to()

@when('I enter valid credentials')
def step_impl(context):
    context.login_page.enter_credentials('user@example.com', 'password123')
    context.login_page.click_login()

@then('I should be logged in successfully')
def step_impl(context):
    welcome_message = context.login_page.get_welcome_message()
    assert 'Welcome' in welcome_message