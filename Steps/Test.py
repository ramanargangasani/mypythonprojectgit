from behave import *


@given('A Test3')
def step_impl(context):
    print('STEP: Given A Test3')


@when('I Test4')
def step_impl(context):
    print('STEP: When I Test4')


@then('I Test5')
def step_impl(context):
    print('STEP: Then I Test5')
