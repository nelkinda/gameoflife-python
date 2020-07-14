from behave import *
from parser import parse_simplified_life1_05


@given(u'the following universe')
def step_impl(context):
    context.universe = parse_simplified_life1_05(context.text)


@then(u'the next generation MUST be')
def step_impl(context):
    context.universe += 1
    assert context.universe == parse_simplified_life1_05(context.text)
