import storage, helper
import jdatetime


class Task:

    def add(self, task, deadline):
        all_tasks = storage.get_data()

        if all_tasks:

            last_id = all_tasks[-1]["id"]
            all_tasks.append(
                {
                    "id": last_id + 1,
                    "task": task,
                    "deadline": deadline,
                    "complete": False,
                }
            )
        else:
            all_tasks.append(
                {"id": 1, "task": task, "deadline": deadline, "complete": False}
            )

        return storage.write_json(all_tasks)

    def remove(self, id):
        all_tasks = storage.get_data()
        target = [task for task in all_tasks if task["id"] == id]
        if target:
            all_tasks.remove(target[0])
            result = storage.write_json(all_tasks)
            if result:
                helper.fix_id(all_tasks)
            return result
        raise ValueError("id not found.")

    def edit(self, id, task, deadline, complete):
        all_tasks = storage.get_data()

        for i in range(len(all_tasks)):
            if all_tasks[i]["id"] == id:
                if task:
                    all_tasks[i]["task"] = task
                if deadline:
                    deadline = helper.check_date(deadline)
                    if deadline:
                        all_tasks[i]["deadline"] = deadline
                if complete:
                    all_tasks[i]["complete"] = complete
                result = storage.write_json(all_tasks)
                return result
        raise ValueError("id not found.")

    def List(self, desc, complete, incomplete, deadline):
        all_tasks = storage.get_data()
        data = []
        if all_tasks:

            if complete:
                for item in all_tasks:
                    if item["complete"] is True:
                        data.append(item)
                if not data:
                    raise Exception("There is no completed task")
            elif incomplete:
                for item in all_tasks:
                    if item["complete"] is False:
                        data.append(item)
                if not data:
                    raise Exception("There is no incompleted task")

            if not data:
                data = all_tasks

            if deadline:

                today = jdatetime.date.today()
                distances = []
                for item in data:
                    temp = (
                        jdatetime.datetime.strptime(item["deadline"], "%Y/%m/%d").date()
                        - today
                    ).days
                    distances.append({"id": item["id"], "dis": temp})

                for i in range(len(data)):
                    for j in range(len(data)):
                        if distances[i]["dis"] > distances[j]["dis"]:
                            data[i], data[j] = data[j], data[i]
            if desc:
                data.reverse()
                return data
            else:
                return data

    def complete(self, id):
        all_tasks = storage.get_data()

        for i in range(len(all_tasks)):
            if all_tasks[i]["id"] == id:
                all_tasks[i]["complete"] = True
                storage.write_json(all_tasks)
                return True

        raise Exception("Please Enter a valid id")
