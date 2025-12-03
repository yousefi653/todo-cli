import storage
import re
import jdatetime


def fix_id(tasks):

    n = 0
    for i in range(len(tasks)):
        n += 1
        tasks[i]["id"] = n
    storage.write_json(tasks)


def check_date(date):

    pattern = r"^\d{4}/\d{1,2}/\d{1,2}$"
    result = re.match(pattern, date)
    if result is None:
        raise ValueError("deadline must be like yyyy/mm/dd")

    try:
        date = jdatetime.datetime.strptime(date, "%Y/%m/%d").date()
    except ValueError:
        raise ValueError("\nmonth must be in range (1-12).\nday must be in range(1-31)")
    else:
        return date.strftime("%Y/%m/%d")


def time_left(deadline):
    today = jdatetime.date.today()
    deadline = jdatetime.datetime.strptime(deadline, "%Y/%m/%d").date()
    distance = deadline - today
    if distance.days > 0:
        return distance.days
    elif distance.days < 0:
        return "task is expired"
    else:
        time = jdatetime.datetime.now().time()
        return f"You have {24 - time.hour}:{60 - time.minute} time."


def get_today():
    today = jdatetime.datetime.now().strftime("%Y/%m/%d")
    return today
