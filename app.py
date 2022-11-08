from flask import Flask,render_template,redirect,request,url_for
import utill
app =  Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/diabetes.html')
def diabetes():
    return render_template('diabetes.html')

@app.route('/chd.html')
def chd():
    return render_template('chd.html')

@app.route('/parkinsons.html')
def parkinsons():
    return render_template('parkinsons.html')

@app.route('/breastcancer.html')
def breastcancer():
    return render_template('breastcancer.html')

# @app.route('/result/<str>')
# def result(str):
#     return render_template('result.html', status = str)




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
        return render_template("result.html", status = res )





 

    
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
        return render_template("result.html", status = res )

@app.route('/submitpar',methods = [ 'POST','GET'])
def submitpar():
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
        res = utill.par_prediction([age,sex,cig,sysBP,diaBP,totChol,hyp,dia,glucose,bloodpre])
        return render_template("result.html", status = res )



@app.route('/submitbre',methods = [ 'POST','GET'])
def submitbre():
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
        res = utill.bre_prediction([age,sex,cig,sysBP,diaBP,totChol,hyp,dia,glucose,bloodpre])
        return render_template("result.html", status = res )

















if __name__ == "__main__":
    app.run(debug=True)
    