from flask import Flask , request , render_template 
# import sqlite3
from data import Task

app=Flask(__name__)

@app.route('/add/' , methods=['POST','GET'])
def add_task():
    Task.put_task(Task(1,request.form.get("taskname"),request.form.get("enddate"),0))
    print("Added successfully")
    tasks=Task.get_all_tasks()
    return render_template('table.html', tasks=tasks)
        

@app.route('/' , methods=['POST','GET'])
def get_tasks():
    tasks=Task.get_all_tasks()
    print(tasks) 
    
    return render_template('table.html' , tasks=tasks)

@app.route('/edit_task/<int:id>', methods=['GET', 'POST'])
def edit_task( id ):
    result=Task.find_by_id( id )
    print(result.taskname)
    print( id)
    return render_template('edit_task.html', taskname=result.taskname , enddate=result.enddate , id=result.id)

@app.route('/update_task/<int:id>', methods=['POST'])
def update_task( id ):
    Task.update_task( Task(id , request.form.get('taskname') , request.form.get('enddate') , 0))
    tasks=Task.get_all_tasks()
    return render_template('table.html' , tasks=tasks)
    
    
@app.route('/delete_task/<int:id>',methods=['POST','GET'])
def delete_task( id ):
    Task.delete_task(id)
    tasks=Task.get_all_tasks()
    return render_template('table.html' , tasks=tasks)

@app.route('/completed_task/<int:id>', methods=['POST' ,'GET'])
def completed_task( id ):
    result=Task.find_by_id( id )
    Task.update_task( Task(id , result.taskname , result.enddate, 1))
    tasks=Task.get_all_tasks()
    return render_template('table.html' , tasks=tasks)

@app.route('/search/',methods=['POST','GET'])
def search():
    result=Task.find_like_name(request.form.get('taskname'))
    return render_template('table.html' ,tasks=Task.get_all_tasks(),searched_data=True , searched_tasks=result)


app.run()