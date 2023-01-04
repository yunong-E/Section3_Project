from flask import Flask, render_template, request, jsonify
import json
import pickle



# 메인 모델 가져오기
model1 = pickle.load(open('model1.pkl','rb'))
model2 = pickle.load(open('model2.pkl','rb'))
model3 = pickle.load(open('model3.pkl','rb'))
model4 = pickle.load(open('model4.pkl','rb'))
model5 = pickle.load(open('model5.pkl','rb'))
model6 = pickle.load(open('model6.pkl','rb'))
model7 = pickle.load(open('model7.pkl','rb'))

# 보너스 모델 가져오기
model_b1 = pickle.load(open('b_model1.pkl','rb'))
model_b2 = pickle.load(open('b_model2.pkl','rb'))
model_b3 = pickle.load(open('b_model3.pkl','rb'))
model_b4 = pickle.load(open('b_model4.pkl','rb'))
model_b5 = pickle.load(open('b_model5.pkl','rb'))
model_b6 = pickle.load(open('b_model6.pkl','rb'))



# 플라스크 모듈 시작
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    id = request.form["id"]

    X_test = [[id]]

    y_pred1 = round(float(model1.predict(X_test)))
    y_pred2 = round(float(model2.predict(X_test)))
    y_pred3 = round(float(model3.predict(X_test)))
    y_pred4 = round(float(model4.predict(X_test)))
    y_pred5 = round(float(model5.predict(X_test)))
    y_pred6 = round(float(model6.predict(X_test)))
    y_pred7 = round(float(model7.predict(X_test)))

    return render_template('result.html', id=id, y_pred1=y_pred1, y_pred2=y_pred2, y_pred3=y_pred3, y_pred4=y_pred4, y_pred5=y_pred5, y_pred6=y_pred6, y_pred7=y_pred7)
    

@app.route('/result_b', methods=['GET', 'POST'])
def result_b():
    id = request.form["id_b"]

    X_test = [[id]]

    y_pred1 = round(float(model_b1.predict(X_test)))
    y_pred2 = round(float(model_b2.predict(X_test)))
    y_pred3 = round(float(model_b3.predict(X_test)))
    y_pred4 = round(float(model_b4.predict(X_test)))
    y_pred5 = round(float(model_b5.predict(X_test)))
    y_pred6 = round(float(model_b6.predict(X_test)))

    return render_template('result_b.html', id=id, y_pred1=y_pred1, y_pred2=y_pred2, y_pred3=y_pred3, y_pred4=y_pred4, y_pred5=y_pred5, y_pred6=y_pred6)





# 실행
if __name__ ==  '__main__':
    app.run(debug=True)



