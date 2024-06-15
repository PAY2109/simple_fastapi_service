from decimal import Decimal

from dateutil.relativedelta import relativedelta

from utils import convert_date_string_to_date


def calculate_deposit(payload):
    date = convert_date_string_to_date(payload['date'])
    periods = payload['periods']
    amount = Decimal(payload['amount'])
    rate = Decimal(payload['rate'])

    calculated_deposit_details = {}

    amount = amount * (1 + (rate / 1200))
    calculated_deposit_details[date.strftime('%d.%m.%Y')] = amount

    for month_num in range(1, periods):
        amount = amount * (1 + (rate / 1200))
        current_date = date + relativedelta(months=month_num)
        calculated_deposit_details[current_date.strftime('%d.%m.%Y')] = round(amount, 2)
    return calculated_deposit_details
