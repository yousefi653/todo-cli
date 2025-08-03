import storage
import re

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