from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
   return render_template('index.html')

@app.route('/mypage', methods=['GET', 'POST'])
def mypage():  
   return 'This is My Page!'

@app.route('/test', methods=['GET'])
def test_get():
    title = request.args['title_give'] # == request.args.get('title_give')
    return jsonify({'result': 'success', 'msg': 'GET 입니다.'})

@app.route('/test', methods=['POST'])
def test_post():
    title = request.form['title_give']
    return jsonify({'result': 'success', 'msg': 'POST 입니다.'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)