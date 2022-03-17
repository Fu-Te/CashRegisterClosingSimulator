from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    
    credit=request.form.get('web_input1')
    ic=request.form.get('web_input2')
    point=request.form.get('web_input3')
    denshi=request.form.get('web_input4')
    jiun_uriage=request.form.get('web_input5')
    sou_uriage=request.form.get('web_input6')
    genkin_uriage=request.form.get('web_input7')
    tax=request.form.get('web_input8')
    kyakusu=request.form.get('web_input9')
    gift=request.form.get('web_input10')
    kake_uriage=request.form.get('web_input11')
    
    return render_template('main.html')
    
@app.route('/CAT')
def cat():


    
    
    return render_template('CAT.html')





#サーバーを動かす
if __name__ == "__main__":
    app.run(debug=True)