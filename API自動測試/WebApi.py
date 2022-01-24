from flask import Flask ,render_template,request
app=Flask(__name__)
@app.route('/')
def defaulpage():
    return render_template('index.html')
@app.route('/login',methods=['get','post'])
def loginpage():
    A=int(request.values['A'])
    B=int(request.values['B'])
    return str(A+B)
    #if request.args.get('A') is "1":
    #    return render_template('sucess.html')
    #else:
    #    return render_template('failed.html')
if __name__=='__main__':
    app.run(debug=True,use_reloader=True)
