"""
******************************************************************************
*    CAR PARTS INVENTORY MANAGEMENT SYSTEM                                   *
*    Python Flask Implementation                                                                         *
******************************************************************************
"""



from flask import Flask, render_template, request, redirect, url_for,flash
import urllib.request, json
import sqlite3
app = Flask(__name__)
# Global variables
dataToUpdate=[]
make=""
total=0
total_products=0
@app.route('/',methods=['POST', 'GET'])
def index():
    '''
    returns : page to render (index.html)

    '''
    global total, total_products
    total = 0
    total_products = 0
    data2 = ""
    query = """Select * from tblCarPartsInventory;"""
    query1 = """Select count(*) from tblCarPartsInventory;"""
    query2 = """Select price,quantity from tblCarPartsInventory;"""
    conn = sqlite3.connect('InventoryDB.db')
    cur1 = conn.cursor()
    cur1.execute(query)
    data1 = cur1.fetchall() # Fetching query for all products

    total_records = len(data1)
    prices = []
    index1 = 0
    while index1 < total_records:
        prices.append("{:10.2f}".format(float(data1[index1][6])))
        index1 += 1

    cur2 = conn.cursor()
    cur2.execute(query1)  # count all the products present in table
    data2 = cur2.fetchall()

    cur3 = conn.cursor()
    cur3.execute(query2)
    data4 = cur3.fetchall()  # select price , quantity for cumulative sum
    conn.close()

    for row in data4:
        total = total+(float(row[0])*float(row[1]))

    strings = [str(data2) for data2 in data2]
    a_string = "".join(strings)

    a_string = a_string.replace(',', '')
    a_string = a_string.replace('(', '')
    a_string = a_string.replace(')', '')
    a_string = str(a_string)
    print(a_string)

    # value3 is total inventory, value2 is total products
    return render_template("index.html", data1=data1, value2=a_string, value3="{:10.2f}".format(total), prices=prices, total=len(data1))


# Add Product view page 
@app.route('/gotoaddproduct', methods=['POST', 'GET'])
def gotoAddProduct():
    return render_template("AddProduct.html") 


# Add Product Post Request Function 
@app.route('/addProduct', methods=['POST', 'GET'])
def AddProduct():
    dt=()
    if request.method=="POST":
        make = request.form["make"]
        year = request.form["year"]
        engine = request.form["engine"]
        part = request.form["part"]
        quantity = request.form["quantity"]
        price = request.form["price"]
        model = request.form["model"]
        partno = request.form["partno"]
        if(make!="" and year!="" and engine!="" and part!="" and quantity!="" and price!="" and model!="" and partno!=""):
            query = """INSERT INTO tblCarPartsInventory(make,year,engine,part,quantity,price,model,partNumber) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);""" 
            dt = (make, year,engine,part,quantity,price,model,partno)
            conn = sqlite3.connect('InventoryDB.db') # create database connection 
            cur = conn.cursor()
            cur.execute(query, dt)
            conn.commit()
            value=""
            return redirect("/") # redirecting to home page 
        else: # return to add product form if in case of failure 
            value="Data not Inserted"
            return render_template("AddProduct.html",value=value)


# Delete product post function 
@app.route("/deletepart", methods=["GET", "POST"])
def delete():
    res_id1=""
    if request.method == "POST":
        res_id1=request.form["res_id1"]
        print(res_id1)
        conn = sqlite3.connect('InventoryDB.db')
        cur4 = conn.cursor()
        query = 'Delete from tblCarPartsInventory where id=?'
        cur4.execute(query,[res_id1])
        conn.commit()
        cur4.close()
        return redirect("/")  # redirecting to home page


# Update part view page render 
@app.route("/updatepart",methods=["GET","POST"])
def updatePageOpen():
    global dataToUpdate
    res_id=""
    if request.method == "POST":
        res_id=request.form["res_id1"]
        conn = sqlite3.connect('InventoryDB.db')
        cur5 = conn.cursor()
        query = 'Select * from tblCarPartsInventory where id=?'
        cur5.execute(query,[res_id])
        dataToUpdate = cur5.fetchone()
        conn.commit()
        cur5.close()
        return render_template("UpdateProduct.html",data5=dataToUpdate)
# Update product post function 
@app.route("/update",methods=["GET","POST"])
def update():
    dt1=()
    if request.method == "POST":
        make = request.form["make"]
        year = request.form["year"]
        engine = request.form["engine"]
        part = request.form["part"]
        quantity = request.form["quantity"]
        price = request.form["price"]
        model = request.form["model"]
        partno = request.form["partno"]
        sql = ''' UPDATE tblCarPartsInventory
                     SET make = ? ,
                         year = ? ,
                         engine = ?,
                         part = ?,
                         quantity = ?,
                         price=?,
                         model=?,
                         partNumber=?
                         
                     WHERE id = ?'''
        dt1 = (make, year, engine, part, quantity, price,model,partno,dataToUpdate[0])
        conn8 = sqlite3.connect('InventoryDB.db')
        cur8 = conn8.cursor()
        cur8.execute(sql, dt1)
        conn8.commit()
        return redirect("/")


# Run Main function of flask app 
if __name__ == '__main__':
    app.run(debug=True)