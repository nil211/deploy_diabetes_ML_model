#from crypt import methods
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/data', methods=["post"])
def show():
    preg_v= float(request.form.get('preg'))
    plas_v= float(request.form.get('plas'))
    pres_v= float(request.form.get('pres'))
    skin_v= float(request.form.get('skin'))
    y= float(request.form.get('x'))
    mass_v= float(request.form.get('mass'))
    pedi_v= float(request.form.get('pedi'))
    age_v= float(request.form.get('age'))
    print(preg_v,plas_v,pres_v ,skin_v, y, mass_v,pedi_v,age_v)
    print(type(preg_v))
    print(type(y))
    a=preg_v
    b=plas_v
    c=pres_v
    d=skin_v
    e=y
    f=mass_v
    g=pedi_v
    h=age_v
    model= joblib.load('predict_pima.pkl')
    #result= model.predict([[preg_v,plas_v,pres_v ,skin_v,test_v,mass_v,pedi_v,age_v]])
    result= model.predict([[a,b,c,d,e,f,g,h]])
    if result[0]==0:
        outcome="Not diabetic"
    else:
        outcome="Diabetic"
    print(result)
    return render_template('show.html', a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h, out= outcome)



app.run(debug=True)
