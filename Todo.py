import storage, helper
import datetime


class Task:

    def add(self, task, deadline):
        all_tasks = storage.get_data()

        if all_tasks:
            id = all_tasks[-1]['id']
            tsk = {"id": id+1, "task": task, "deadline": deadline, "complete": False}
        else:
            tsk = {"id": 1, "task": task, "deadline": deadline, "complete": False}

        all_tasks.append(tsk)
        storage.write_json(all_tasks)


    def remove(self, id):
        all_tasks = storage.get_data()
        all_tasks.pop(id-1)
        storage.write_json(all_tasks)

    def edit(self, id):
        pass


    def List(self, desc):
        all_tasks = storage.get_data()
        helper.fix_id(all_tasks)
        
        if desc:
            all_tasks.reverse()
            for task in all_tasks:
                print(f'{task.get('id')}. {task.get('task')}  deadline( {task.get('deadline')} )  complete => {task.get('complete')}')

        else:
            for task in all_tasks:
                print(f'{task.get('id')}. {task.get('task')}  deadline( {task.get('deadline')} )  complete => {task.get('complete')}')


    def complete(self, id):
        all_tasks = storage.get_data()
        for i in range(len(all_tasks)):
            if all_tasks[i]['id']==id:
                all_tasks[i]['complete'] = True
                storage.write_json(all_tasks)
                break
