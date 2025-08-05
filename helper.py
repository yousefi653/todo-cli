import storage
import re
import jdatetime


def fix_id(tasks):
    
    n = 0
    for i in range(len(tasks)):
        n+=1
        tasks[i]['id'] = n
    storage.write_json(tasks)


def check_date(date):
    pattern = r"^\d{4}/\d{1,2}/\d{1,2}$"
    result = re.match(pattern, date)
    if result:
        return True
    

def change_format(date):
    date = jdatetime.datetime.strptime(date, "%Y/%m/%d").date()
    return date.strftime("%A - %Y/%m/%d")


def left_day(deadline):
    deadline = jdatetime.datetime.strptime(deadline, "%A - %Y/%m/%d").date()
    today = jdatetime.date.today()
    return (deadline - today).days
