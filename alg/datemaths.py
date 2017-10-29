import math


def days_between(date_a, date_b):
    "number of days between 2 date strings"
    a = extract(date_a)
    b = extract(date_b)
    for k in ['year', 'month', 'day']:  # ensure a < b, swap if required
        if a[k] != b[k]:
            if a[k] < b[k]:
                break
            else:
                (a, b) = (b, a)
                break
    days = b['day'] - a['day']
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if a['month'] < b['month']:
        for m in range(a['month'], b['month']):
            days += months[m]
    else:
        for m in range(b['month'], a['month']):
            days -= months[m]
    days += 365 * (b['year'] - a['year'])
    days += leap_years_between(a, b)
    return days


def leap_years_between(a, b):
    # TODO
    return 0


def working_days(date_str, days):
    whole_weeks = math.floor(days/7)
    rem_days = days - whole_weeks*7
    res = whole_weeks*5
    w = weekday(date_str)  # make Mon = 0 ... Sat = 5, Sun = 6
    x = (w + rem_days) % 7
    if x < w:
        # gone over a weekend
        if w == 6:
            res += rem_days - 1  # half weekend (started on Sun)
        else:
            res += rem_days - 2  # full weekend
    else:
        res += rem_days
    if x == 6:
        # ends on a Sat
        res -= 1
    return res


def weekday(date_str):
    """
    Determine the day of the week using Gauss' method
    https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week
    Mon = 0 ... Sun = 6
    """
    date = extract(date_str)
    if date['month'] <= 2:
        Y = date['year'] - 1
        m = date['month'] + 10
    else:
        Y = date['year']
        m = date['month'] - 2
    c = int(Y / 100)
    y = Y - c * 100
    d = date['day']
    w = (d + math.floor(2.6*m - 0.2) + y + math.floor(y / 4)
           + math.floor(c / 4) - 2*c) % 7
    return (w - 1) % 7  # shift to make Mon=0 etc.


def extract(date_str):
    (d, m, y) = date_str.split("/")
    return {'day': int(d), 'month': int(m), 'year': int(y)}


def test_datemaths():
    # assert working_days decreases or stays the same as the period shortens
    start = "1/1/2010"
    end = "31/3/2010"
    days = days_between(start, end)
    weekdays = working_days(start, days)
    for i in range(31):
        end = datestr_sub1(end)
        w = working_days(start, days_between(start, end))
        assert(w <= weekdays)
        weekdays = w


def datestr_sub1(date_str):
    'for use in tests'
    t = extract(date_str)
    if t['day'] > 1:
        return "{}/{}/{}".format(t['day'] - 1, t['month'], t['year'])
    return date_str


def main():
    if len(sys.argv) != 3:
        print("USAGE: python3 datemaths DD/MM/YYYY DD/MM/YYYY")
        sys.exit(1)
    start = sys.argv[1]
    end = sys.argv[2]
    days = days_between(end, start)
    print("There are", days, "days between", start, "and", end)
    print(working_days(start, days), "of these are weekdays")


if __name__ == '__main__':
    import sys
    main()
