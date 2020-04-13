from behave import *
from calculadora import *

@given('a {values_add}')
def step_impl(context, values):
    context.calculadora = Calculadora()
    context.values_add = values_add.split(',')

@when('the calculator sums the values')
def step_impl(context):
    context.total_add = context.calculadora.sumar(int(context.values_add[0]),int(context.values_add[1]))

@then('the {total_add:d} is correct')
def step_impl(context, total_add):
    assert (context.total_add == total_add)

@given('a {values_sub}')
def step_impl(context, values):
    context.calculadora = Calculadora()
    context.values_sub = values_sub.split(',')

@when('the calculator substract the values')
def step_impl(context):
    context.total_sub = context.calculadora.restar(int(context.values_sub[0]),int(context.values_sub[1]))

@then('the {total_sub:d} is correct')
def step_impl(context, total_sub):
    assert (context.total_sub == total_sub)
