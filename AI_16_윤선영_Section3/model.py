
########## 역피클링
import sklearn
import math
from sklearn.linear_model import LinearRegression
import pickle


model1 = None
model2 = None
model3 = None
model4 = None
model5 = None
model6 = None
model7 = None

with open('model1.pkl', 'rb') as p_file:
    model1 = pickle.load(p_file)

with open('model2.pkl', 'rb') as p_file:
    model2 = pickle.load(p_file)

with open('model3.pkl', 'rb') as p_file:
    model3 = pickle.load(p_file)

with open('model4.pkl', 'rb') as p_file:
    model4 = pickle.load(p_file)

with open('model5.pkl', 'rb') as p_file:
    model5 = pickle.load(p_file)

with open('model6.pkl', 'rb') as p_file:
    model6 = pickle.load(p_file)

with open('model7.pkl', 'rb') as p_file:
    model7 = pickle.load(p_file)

X_test = [[250]]

y_pred1 = int(model1.predict(X_test))
y_pred2 = int(model2.predict(X_test))
y_pred3 = int(model3.predict(X_test))
y_pred4 = int(model4.predict(X_test))
y_pred5 = int(model5.predict(X_test))
y_pred6 = int(model6.predict(X_test))
y_pred7 = int(model7.predict(X_test))

print(f"{X_test}회의 예상 조 번호는 {y_pred1} 이며, 나머지 여섯 번호는 {[y_pred2, y_pred3, y_pred4, y_pred5, y_pred6, y_pred7]}입니다.")