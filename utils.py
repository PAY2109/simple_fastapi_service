from datetime import datetime as dt


def convert_date_string_to_date(date_string):
    return (
        dt.strptime(date_string, "%d.%m.%Y").date()
    )


def validate_payload(payload):
    try:
        convert_date_string_to_date(payload['date'])
    except ValueError:
        return False

    if payload['periods'] < 1 or payload['periods'] > 60:
        return False

    if payload['amount'] < 10000 or payload['amount'] > 3000000:
        return False

    if payload['rate'] < 1.0 or payload['rate'] > 8.0:
        return False

    return True
