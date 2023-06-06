from flask import Flask, render_template, request
import random

app = Flask(__name__)


# 奖品列表
prizes = ["特等奖", "一等奖", "二等奖", "三等奖", "四等奖"]

# 每个奖品对应的图片路径
prize_images = {
    "特等奖": "static/0.png",
    "一等奖": "static/1.png",
    "二等奖": "static/2.png",
    "三等奖": "static/3.png",
    "四等奖": "static/4.png"
}

# 每个奖品对应的祝贺信息
prize_congrats = {
    "特等奖": "恭喜您获得特等奖！在池塘里挖呀挖呀挖",
    "一等奖": "恭喜您获得一等奖！我想养只小狗",
    "二等奖": "恭喜您获得二等奖！小猪佩奇最可爱了",
    "三等奖": "恭喜您获得三等奖！面对疾风吧孩子",
    "四等奖": "恭喜您获得四等奖！最少也是有第四名的"
}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lottery')
def perform_lottery():
    # 模拟抽奖过程
    # 这里使用随机数生成抽奖结果，您可以根据实际需求进行修改
    winning_prize = random.choices(prizes, weights=[1, 10, 20, 30, 39], k=1)[0]

    # 显示奖品图片
    image_path = prize_images.get(winning_prize)

    # 输出祝贺信息
    congrats_message = prize_congrats.get(winning_prize)

    return render_template('result.html', prize=winning_prize, image_path=image_path, congrats_message=congrats_message)




if __name__ == '__main__':
    app.run(debug=True)

