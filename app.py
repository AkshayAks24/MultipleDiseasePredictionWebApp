from flask import Flask,redirect,url_for,render_template,request
import utill
# from flask_bootstrap import Bootstrap

app = Flask(__name__)

# bootstrap = Bootstrap()
# bootstrap.init_app(app)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/result/<str>')
def result(str):
    return render_template('result.html', status = str)


@app.route('/resultt')
def resultt():
    return render_template('result.html')
# @app.route('/fail/<int:score>')
# def fail(score):
#     status = 'FAILED'
#     return render_template('result.html', finalScore = score,status = status)

@app.route('/diabetespred.html')
def diabetes():
    return render_template('diabetespred.html')

@app.route('/chd.html')
def chd():
    return render_template('chd.html')

@app.route('/parkinsons.html')
def parkinsons():
    return render_template('parkinsons.html')

@app.route('/breastcancer.html')
def breastcancer():
    return render_template('breastcancer.html')


@app.route('/inner-page.html')
def breastcancer_0():
    return render_template('inner-page.html')

@app.route('/inner-page-copy.html')
def breastcancer_02():
    return render_template('inner-page-copy.html')


@app.route('/submitdia',methods = [ 'POST','GET'])
def submitdia():
    if request.method == 'POST':
        age = float(request.form['age'])
        pregnancies = float(request.form['preg'])
        glucose = float(request.form['gluc'])
        bloodPressure = float(request.form['bp'])
        skinThickness = float(request.form['skin'])
        insulin = float(request.form['insu'])
        bmi = float(request.form['bmi'])
        DiaPredFunc = float(request.form['diapred'])
        res = utill.dia_prediction([pregnancies,glucose,bloodPressure,skinThickness,insulin,bmi,DiaPredFunc,age])
        return redirect(url_for("result", str = res ))   


@app.route('/submitchd',methods = [ 'POST','GET'])
def submitchd():
    if request.method == 'POST':
        age = float(request.form['age'])
        sex = float(request.form['sex'])
        cig = float(request.form['cig'])
        sysBP = float(request.form['sysBP'])
        diaBP = float(request.form['diaBP'])
        totChol = float(request.form['totChol'])
        hyp = float(request.form['hyp'])
        dia = float(request.form['dia'])
        glucose = float(request.form['glucose'])
        bloodpre = float(request.form['bloodpre'])
        res = utill.chd_prediction([age,sex,cig,sysBP,diaBP,totChol,hyp,dia,glucose,bloodpre])
        return redirect(url_for("result", str = res ))  

    



    

if __name__ ==  '__main__':
    app.run(debug=True)