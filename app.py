import services.imgToMusic
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

#开启调试
if __name__ == '__main__':
    app.run(debug=True)

CORS(app, resources=r'/*')

@app.route("/hello")
def hello_world():
    return "<p>Hello ~</p>"

@app.route("/image_to_text", methods=['POST'])
def image_to_text():
    reqData = request.json.get("data")
    resData = services.imgToMusic.imageBase64ToText(reqData)
    return resData


@app.route("/imgtext_to_mpt", methods=['POST'])
def imgtext_to_mpt():
    reqData = request.json.get("imgText")
    resData = services.imgToMusic.imgtextToMpt(reqData)
    return resData


@app.route("/mpt_to_music", methods=['POST'])
def imgmpt_to_music():
    reqData = request.json.get("img_mpt")
    resData = services.imgToMusic.imgMptToMusic(reqData)
    return resData


@app.route("/usertxt_to_music", methods=['POST'])
def user_txt_to_music():
    reqData = request.json.get("user_txt")
    resData = services.imgToMusic.imgMptToMusic(reqData)
    return resData


@app.route("/mp3_to_music", methods=['POST'])
def mp3_txt_to_music():
    mp3Url = request.json.get("mp3_url")
    userTxt = request.json.get("user_txt")
    resData = services.imgToMusic.Mp3TxtToMusic(mp3Url, userTxt)
    return resData


@app.route("/imageurl_to_text", methods=['POST'])
def imageurl_to_text():
    imgUrl = request.json.get("img_url")
    resData = services.imgToMusic.ImageUrlToText(imgUrl)
    return resData