import sqlite3
connection=sqlite3.connect('taskdata.db')
cursor=connection.cursor()
create_table_query="CREATE TABLE IF NOT EXISTS REGISTERED_TASK (ID INTEGER PRIMARY KEY AUTOINCREMENT , TASKNAME VARCHAR ,ENDDATE DATE ,ISCOMPLETE BOOLEAN )"
cursor.execute(create_table_query)
connection.commit()
connection.close()

class Task:
    def __init__(self,_id, taskname, enddate , iscomplete):
        self.id=_id
        self.taskname=taskname
        self.enddate=enddate
        self.iscomplete=iscomplete

    @classmethod
    def find_by_name(cls,name):
        connection=sqlite3.connect('taskdata.db')
        cursor=connection.cursor()
        select_query="SELECT * FROM REGISTERED_TASK WHERE TASKNAME=?"
        result=cursor.execute(select_query,(name,))
        print(result.fetchall())
        row=result.fetchone()
        if row:
            task=cls(*row)
        else:
            task=None
        connection.close()
        return task

    @classmethod
    def find_by_id(cls , id):
        connection=sqlite3.connect('taskdata.db')
        cursor=connection.cursor()
        select_query="SELECT * FROM REGISTERED_TASK WHERE ID=?"
        result=cursor.execute(select_query,(id,))
        print(type(result))

        row=result.fetchone()
        if row:
            task=cls(*row)
        else:
            task=None
        connection.close()
        return task
    @classmethod
    def put_task(cls,task):
        connection=sqlite3.connect('taskdata.db')
        cursor=connection.cursor()
        insert_query="INSERT INTO REGISTERED_TASK VALUES(NULL, ? , ? , ?)"
        cursor.execute(insert_query,( task.taskname , task.enddate , task.iscomplete))
        connection.commit()
        connection.close()
    @staticmethod
    def get_all_tasks():
        connection=sqlite3.connect('taskdata.db')
        cursor=connection.cursor()
        select_query="SELECT * FROM REGISTERED_TASK"
        result=cursor.execute( select_query )
        result=result.fetchall()
        if result :
            return result
        else:
            return None

    @classmethod
    def update_task(cls,task):
        connection=sqlite3.connect('taskdata.db')
        cursor=connection.cursor()
        update_query="UPDATE REGISTERED_TASK SET TASKNAME=? , ENDDATE=? ,ISCOMPLETE=? WHERE ID=?"
        cursor.execute(update_query , (task.taskname,task.enddate ,task.iscomplete , task.id))
        connection.commit()
        connection.close()

    @staticmethod
    def delete_task( id ):
        connection=sqlite3.connect('taskdata.db')
        cursor=connection.cursor()
        delete_query="DELETE FROM REGISTERED_TASK WHERE ID=?"
        cursor.execute( delete_query , ( id ,))
        connection.commit()
        connection.close()


    @classmethod
    def find_like_name(cls,name):
        connection=sqlite3.connect('taskdata.db')
        cursor=connection.cursor()
        select_query="SELECT * FROM REGISTERED_TASK WHERE TASKNAME LIKE ?"
        result=cursor.execute(select_query,("%"+name+"%",))
        result=result.fetchall()

        if result :
            return result
        else:
            return None



# print(Task.find_like_name("Fla")[0][0])
# print(Task.get_all_tasks())
# Task.delete_task(3)
# print(Task.get_all_tasks())




# Task.put_task( Task(1 ,"Complete flask" , "13/5/2022" , 0))
# print(Task.find_by_id(3).taskname)
# print(Task.find_by_name("Learn Node js").enddate)