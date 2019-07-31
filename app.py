from flask import Flask, render_template, request,jsonify,redirect,url_for
import pymysql


app = Flask(__name__, static_url_path='/static')

def db_con():
    db = 'myDataBase'
    con = pymysql.connect(database=db,user="root",password="",host="localhost")
    con.autocommit(True)
    cursor = con.cursor()
    dict_cursor = con.cursor(pymysql.cursors.DictCursor)
    return (cursor,dict_cursor)

@app.route('/')
def home():
    cursor =db_con()[1]
    cursor.execute('SELECT id,crop_name FROM crops')
    data=cursor.fetchall()
    cursor.close()
    # return jsonify(crops)
    return render_template('index.html',crops=data)

@app.route('/crops/<int:id>')
def crops(id):
    cursor =db_con()[1]
    cursor.execute("SELECT * FROM CROPS WHERE id = %s", (id))
    data=cursor.fetchall()
    cursor.close()
    return render_template('crops_index.html',crop=data[0])  

@app.route('/')
def homepage():
    # cursor =db_con()[1]
    # cursor.execute("SELECT * FROM CROPS WHERE id = %s", (id))
    # data=cursor.fetchall()
    # cursor.close()
    return render_template('homepage_content.html') 

@app.route('/pests/<int:id>')
def pests(id):
    cursor =db_con()[1]
    cursor.execute("SELECT * FROM CROPS WHERE id = %s", (id))
    data=cursor.fetchall()
    cursor.execute("SELECT id, pests,cure,signs  FROM cropdiseases WHERE crop_id = %s", (id))
    cropdiseases=cursor.fetchall()
    cursor.close()
    # return jsonify(cropdiseases)
    return render_template('pests.html',crop=data,pests=cropdiseases)
    # return redirect(url_for('edit_crop',id=id))
     
@app.route('/diseases/<int:id>')
def diseases(id):
    cursor =db_con()[1]
    cursor.execute("SELECT * FROM CROPS WHERE id = %s", (id))
    data = cursor.fetchall()
    cursor.execute("SELECT id, diseases,cure,signs  FROM cropdiseases WHERE crop_id = %s", (id))
    cropdiseases = cursor.fetchall()
    cursor.close()
    # return jsonify(cropdiseases)
    return render_template('diseases.html',crop=data,diseases=cropdiseases)
    # return redirect(url_for('diseases',id=id),crop=data,diseases=cropdiseases)


# @app.route('/receive', methods=['POST'])
# def receive():
#         username = request.form.get('username')
#         password = request.form['password']

#         return ('You have entered a username-{}, and a password-{}'.format(username, password))
    ## if request.method == 'POST':
    #     return ('You instead sent a GET request')

if __name__ == '__main__':
    app.run(debug=True)