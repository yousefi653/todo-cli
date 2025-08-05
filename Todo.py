import storage, helper
import jdatetime


class Task:

    def add(self, task, deadline):
        all_tasks = storage.get_data()

        if all_tasks:
            id = all_tasks[-1]["id"]
            tsk = {"id": id + 1, "task": task, "deadline": deadline, "complete": False}
        else:
            tsk = {"id": 1, "task": task, "deadline": deadline, "complete": False}

        all_tasks.append(tsk)
        storage.write_json(all_tasks)


    def remove(self, id):
        all_tasks = storage.get_data()
        target = [task for task in all_tasks if task['id']==id]
        if target:
            all_tasks.remove(target[0])
            storage.write_json(all_tasks)
            return True
        print(f'>please enter valid id.')


    def edit(self, id, task, deadline, complete):
        all_tasks = storage.get_data()

        for i in range(len(all_tasks)):
            if all_tasks[i]["id"] == id:
                
                if task:
                    all_tasks[i]["task"] = task
                
                if deadline:
                    deadline = helper.change_format(deadline)
                    all_tasks[i]["deadline"] = deadline
                
                if complete!=None:
                    all_tasks[i]["complete"] = complete
                storage.write_json(all_tasks)
                return True
        print('>please enter valid id.')


    def List(self, desc):

        all_tasks = storage.get_data()
        helper.fix_id(all_tasks)

        if desc:
            all_tasks.reverse()
            for task in all_tasks:
                print(
                    f"{task.get('id')}. {task.get('task')}  deadline( {task.get('deadline')} & {helper.left_day(task['deadline'])} days left.)  complete => {task.get('complete')}\n"
                )

        else:
            for task in all_tasks:
                print(
                    f"{task.get('id')}. {task.get('task')}  deadline( {task.get('deadline')} & {helper.left_day(task['deadline'])} days left.)  complete => {task.get('complete')}\n"
                )


    def complete(self, id):
        all_tasks = storage.get_data()
        
        for i in range(len(all_tasks)):
            if all_tasks[i]["id"] == id:
                all_tasks[i]["complete"] = True
                storage.write_json(all_tasks)
                return True
            
        print('>please enter valid id.')


    def today(self):
        all_tasks = storage.get_data()
        today = helper.change_format(jdatetime.datetime.now().date().strftime('%Y/%m/%d'))
        for task in all_tasks:
            if  task['deadline'] == today:
                print(
                    f"{task.get('id')}. {task.get('task')}  deadline( {task.get('deadline')} )  complete => {task.get('complete')}"
                )
