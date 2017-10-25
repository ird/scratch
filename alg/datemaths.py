def days_between(date_a, date_b):
    "number of days between 2 date strings"
    a = extract(date_a)
    b = extract(date_b)
    for k in ['year', 'month', 'day']:
        if a[k] != b[k]:
            if a[k] < b[k]:
                return sub_dates(b, a)
            else:
                return sub_dates(a, b)
    return 0  # same day


def sub_dates(end, start):
    "returns end - start in days. requires end > start"
    days_in = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(start['month']):
        start['day'] += days_in[i]
    for i in range(end['month']):
        end['day'] += days_in[i]
    r = end['day'] - start['day']
    r += 365 * (end['year'] - start['year'])
    r += leap_years_between(start, end)
    return r


def leap_years_between(a, b):
    # TODO
    return 0


def working_days(start_date, days):
    # TODO
    return days


def weekday(date_str):
    "1=Mon, 7=Sun"
    # TODO
    return 4


def extract(date_str):
    (d, m, y) = date_str.split("/")
    return {'day': int(d), 'month': int(m), 'year': int(y)}


if __name__ == '__main__':
    start_date = "19/9/18"
    end_date = "19/9/18"
    print(working_days(start_date, days_between(end_date, start_date)))
