app=Flask(_name_)
@app.route('/')
def home():
       return render_template('home.html1')
 @app.route('/predict')
 def index():
         return render_template("index.html")
         @app.route('/data_predict',methods=['POST'])
def predict():
       age =request.form['age']
       gender =request.form['gender']
       tb =request.form['tb']
       db =request.form['db']
       ap =request.form['ap']
       aa1 =request.form['aa1']
       aa2 =request.form['aa2']
       tp =request.form['tp']
       a =request.form['a']
       agr =request.form['agr']

        data= [[float(age),float(gender),float(tb),float(db),float(ap),float(aa1),float(aa2),float(tp),float(a),float(agr)]]
        model =pickle.load(open('liver_analysis.pkl','rb'))
        prediction=model.predict(data)[0]
        if(prediction==1):
            return render_template('noChance.html',prediction='You have a liver desease Problem,You must and
        else:
           return render_template('Chance.html',prediction='You dont have a liver desease Problem')
  if_name_=='_main_':
     app.run()