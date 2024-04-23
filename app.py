from os import name
from flask import Flask, redirect, url_for, request, Response, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'testing123'
app.config['MYSQL_PASSWORD'] = 'pwd'
app.config['MYSQL_DB'] = 'electoral_bonds'

mysql = MySQL(app)

def get_data():
    cursor=mysql.connection.cursor()
    cursor.execute('select distinct name_of_purchaser from purchase_details')
    name_of_purchaser=list(cursor.fetchall())
    name_of_purchaser.sort()
    cursor.close()
    cursor=mysql.connection.cursor()
    cursor.execute('select distinct name_of_party from redemption_details')
    name_of_party=list(cursor.fetchall())
    name_of_party.sort()
    cursor.close()
    return name_of_purchaser,name_of_party

@app.route('/', methods = ["POST", "GET"])
def main_page():
    name_of_purchaser,name_of_party=get_data()
    return render_template("index.html",name_of_purchaser=name_of_purchaser,name_of_party=name_of_party)
bond_number=0
@app.route('/a_2', methods = ["POST", "GET"])
def a_2():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        table_name=request.form['tablename']
        cursor.execute(f"select * from {table_name} where bond_number = %s",(request.form['box'],))
        data=cursor.fetchall()
        bond_number=request.form['box']
    if len(data)==0:
        return render_template('index.html',a_2_data = [['Not Found']])
    print(data)
    return render_template("e_1.html", a_2_data = data,filter=['Name of Purchaser','Name of Party'],bond_number=bond_number,table_name=table_name) 
@app.route('/e_1',methods=['POST','GET'])
def e_1():
    if request.method == "POST":
        cursor=mysql.connection.cursor()
        column_name=request.form['filter_type'].split()[0]
        table_name=request.form['filter_type'].split()[2]
        cursor.execute(f"select * from {table_name} where {column_name} = %s",(request.form['filter_value'],))
        print(column_name,request.form['filter_value'],table_name)
        data=cursor.fetchall()
        # print(data)
        data_final=[]
            # print(request.form['filter_type'][18:])
        for i in range(len(data)):
            if table_name=='purchase_details':
                if str(data[i][7])==request.form['filter_type'].split()[1]:
                    data_final.append(data[i])
            else:
                if str(data[i][5])==request.form['filter_type'].split()[1]:
                    data_final.append(data[i])
        print(data_final)
    return render_template('e_1.html',a_2_data = data_final,filter=['Name of Purchaser','Name of Party'])

@app.route('/e_2',methods=['POST','GET'])
def e_2():
    if request.method == "POST":
        cursor=mysql.connection.cursor()
        value=request.form['Company']
        print(value)
        cursor.execute("select bond_number,denominations,year from purchase_details where name_of_purchaser = %s",(request.form['Company'],))
        data=cursor.fetchall()
        d={}
        c=0
        for i in range(len(data)):
            d[data[i][2]]=d.get(data[i][2],0)+data[i][1]
            c+=1
        cursor.close()
    if len(data)==0:
        return render_template('index.html',e_2_data = [['Not Found']])
    print(d)
    years=list(d.keys())
    amount=list(d.values())
    number=[c]
    print(amount,number)
    name_of_purchaser,name_of_party=get_data()
    return render_template('e_2.html',e_2_data = data,years=years,amount=amount,company=value,number=number)
        
@app.route('/e_3',methods=['POST','GET'])
def e_3():
    if request.method == "POST":
        cursor=mysql.connection.cursor()
        value=request.form['party']
        print(value)
        cursor.execute("select bond_number,denominations,year from redemption_details where name_of_party = %s",(request.form['party'],))
        data=cursor.fetchall()
        d={}
        for i in range(len(data)):
            d[data[i][2]]=d.get(data[i][2],0)+data[i][1]
        cursor.close()
    print(data)
    print(d)
    years=list(d.keys())
    amount=list(d.values())
    if len(data)==0:
        return render_template('index.html',e_3_data = [['Not Found']])
    name_of_purchaser,name_of_party=get_data()
    return render_template('e_3.html',e_3_data = data,years1=years,amount1=amount)

@app.route('/e_4',methods=['POST','GET'])
def e_4():
    if request.method=="POST":
        cursor=mysql.connection.cursor()
        cursor.execute('select bond_number,name_of_purchaser,denominations from purchase_details where bond_number in (select bond_number from redemption_details where name_of_party = %s)',(request.form['party'],))
        data=cursor.fetchall()
        print(data)
        if len(data)==0:
            return render_template('index.html',e_4_data = [['Not Found']])
        name_of_purchaser,name_of_party=get_data()
        d={}
        for i in range(len(data)):
            d[data[i][1]]=d.get(data[i][1],0)+data[i][2]
        companies=list(d.keys())
        total_amount=list(d.values())
        return render_template('e_4.html',companies=companies,total_amount=total_amount,e_4_data = list(d.items()),party=request.form['party'])
@app.route('/e_5',methods=['POST','GET'])
def e_5():
    if request.method=="POST":
        cursor=mysql.connection.cursor()
        value=request.form['company']
        print(value)
        cursor.execute('select name_of_party,denominations from redemption_details where bond_number in (select bond_number from purchase_details where name_of_purchaser = %s)',(request.form['company'],))
        data=cursor.fetchall()
        if len(data)==0:
            return render_template('index.html',e_5_data = [['Not Found']])
        d={}
        for i in range(len(data)):
            d[data[i][0]]=d.get(data[i][0],0)+data[i][1]
        parties=list(d.keys())
        total_amount=list(d.values())
        total_denominations=sum(total_amount)
        name_of_purchaser,name_of_party=get_data()
        return render_template('e_5.html',e_5_data = list(d.items()),parties=parties,total_amount=total_amount,total_denominations=total_denominations,company=request.form['company'])

@app.route('/e_6',methods=['POST','GET'])
def e_6():
    if request.method=="POST":
        print(request.form['Pie Chart'])
        cursor=mysql.connection.cursor()
        cursor.execute('select denominations, name_of_party from redemption_details')
        data=cursor.fetchall()
        d={}
        for i in range(len(data)):
            d[data[i][1]]=d.get(data[i][1],0)+data[i][0]
        print(d)
        party=list(d.keys())
        total_donations=list(d.values())
    return render_template('e_6.html',party=party,total_donations=total_donations)
if __name__ == '__main__':
   app.run(host="0.0.0.0", port="80", debug = True) 
