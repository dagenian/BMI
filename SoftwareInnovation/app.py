from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/main',methods=['GET','POST'])
def main():
    height=float(request.form['height'])
    weight=float(request.form['weight'])
    BMI=weight/(height*height)
    if BMI<18.5:
        note="偏瘦"
    elif BMI>=18.5 and BMI<=23.9:
        note="正常"
    elif BMI>23.9 and BMI<=27.9:
        note="偏胖"
    else:
        note="肥胖"
    return render_template("main.html",BMI=BMI,note=note)



if __name__ == '__main__':
    app.run(host='192.168.1.24',post=3000,debug=True)
