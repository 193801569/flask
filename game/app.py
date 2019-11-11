from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # return render_template("../templates/ball.html")
    return render_template("home.html")


@app.route('/game/ball')
def gameball():
    # return render_template("../templates/ball.html")
    return render_template("弹球.html")


@app.route('/game/王思聪接热狗')
def jie_re_gou():
    # return render_template("../templates/ball.html")
    return render_template("接热狗.html")


@app.route('/game/别踩白块/普通模式')
def whitetblock1():
    # return render_template("../templates/ball.html")
    return render_template("别踩白块.html")


@app.route('/game/别踩白块/移动模式')
def whiteblock2():
    # return render_template("../templates/ball.html")
    return render_template("别踩白块(移动).html")


@app.route('/game/拼数字')
def pin_shu_zi():
    # return render_template("../templates/ball.html")
    return render_template("拼数字.html")


@app.route('/game/飞机大战')
def aircraft_war():
    # return render_template("../templates/ball.html")
    return render_template("飞机大战.html")

@app.route('/game/贪吃蛇')
def snake():
    # return render_template("../templates/ball.html")
    return render_template("贪吃蛇.html")

@app.route('/game/五子棋')
def gobang():
    # return render_template("../templates/ball.html")
    return render_template("五子棋.html")


@app.route('/game/跳跳龙')
def tiao_tiao_long():
    # return render_template("../templates/ball.html")
    return render_template("google小恐龙.html")

@app.route('/game/特效')
def animation():
    # return render_template("../templates/ball.html")
    return render_template("特效.html")

@app.route('/animation/樱花飘落')
def sakura():
    # return render_template("../templates/ball.html")
    return render_template("樱花飘落.html")


@app.route('/animation/穿越星空')
def through_space():
    # return render_template("../templates/ball.html")
    return render_template("穿越星空.html")


@app.route('/animation/核心价值观')
def corevalue():
    # return render_template("../templates/ball.html")
    return render_template("核心价值观.html")


@app.route('/animation/雪花飘落')
def snowdown():
    # return render_template("../templates/ball.html")
    return render_template("雪花飘落.html")




if __name__ == '__main__':
    # app.run(port=5000,host='0.0.0.0')

    app.run(port=5000, debug=False,host='0.0.0.0')
