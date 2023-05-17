from flask import Flask, render_template,request,redirect
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap



app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Naveen@95'
app.config['MYSQL_DB']='pyflaskmysql'

mysql=MySQL(app)
Bootstrap(app)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        userDetails=request.form
        name=userDetails['name']
        description=userDetails['description']
        price=userDetails['price']
        image=userDetails['image']

        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO products(name,description,price,image) VALUES(%s,%s,%s,%s)",(name,description,price,image))
        mysql.connection.commit()
        cur.close()
        return redirect ('/listproducts')
    return render_template('addproduct.html')

@app.route('/listproducts')
def users():
    cur=mysql.connection.cursor()
    resultValue=cur.execute('SELECT * FROM products')
    if resultValue>0:
        userDetails=cur.fetchall()
        return render_template('listproducts.html',userDetails=userDetails)

if __name__=='__main__':
    app.run(debug=True)