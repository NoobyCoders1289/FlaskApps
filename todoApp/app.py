from flask import Flask, redirect, render_template,request, url_for
import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    port = '5432',
    database = 'postgres',
    user = 'postgres',
    password ='123123123'
)

app = Flask(__name__)



@app.route('/')
def allTasks():
    cur = conn.cursor()
    cur.execute('select * from todo')
    tasks = cur.fetchall()
    return render_template('index.html',tasks=tasks)



@app.route('/tasks/edit/<string:id>',methods=['GET','POST'])
def editTask(id):
    if request.method=='GET':
        cur = conn.cursor()
        cur.execute('select * from todo where id=%s',(id))
        task = cur.fetchone()
        return render_template('edit.html',task=task)
    name = request.form['name']
    cur = conn.cursor()
    cur.execute('update todo set name = %s where id=%s',(name,id))
    conn.commit()
    return redirect(url_for('allTasks'))


@app.route('/tasks/add/',methods=['GET','POST'])
def addTask():
    if request.method=='GET':
        cur = conn.cursor()
        
        cur.execute('select distinct id from todo')
        rows = cur.fetchall()
        id = max(rows)[0]+1
        return render_template('addtask.html', id=id)
    id = request.form['id']
    name = request.form['name']

    cur = conn.cursor()
    cur.execute('insert into todo(id,name) values(%s,%s)',(id,name))
    conn.commit()
    return redirect(url_for('allTasks'))
    


@app.route('/tasks/delete/<string:id>')
def deleteTask(id):
    cur = conn.cursor()
    cur.execute('delete from todo where id=%s', (id,))
    conn.commit()
    return redirect(url_for('allTasks'))



if __name__ == '__main__':
    app.run(debug=True)