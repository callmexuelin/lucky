from flask import Flask, render_template, request
import random

app = Flask(__name__)

def draw_lottery():
    prizes = {
        "特等奖": 0.01,
        "一等奖": 0.1,
        "二等奖": 0.2,
        "三等奖": 0.3,
        "四等奖": 0.39
    }

    lottery_num = random.random()
    cumulative_prob = 0.0
    for prize, prob in prizes.items():
        cumulative_prob += prob
        if lottery_num < cumulative_prob:
            return prize

    return "未中奖"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lottery', methods=['GET', 'POST'])
def lottery():
    if request.method == 'GET':
        result = draw_lottery()
        print(result)
        return render_template('result.html', result=result)
    else:
        return render_template('error.html', error="Method Not Allowed")




if __name__ == '__main__':
    app.run(debug=True)

