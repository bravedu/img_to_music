import requests,json,os,base64,zhipuai,re
from gradio_client import Client
from PIL import Image
from io import BytesIO

#图片识别成文本URL
ImgToTextUrl = "http://127.0.0.1:8881/run/predict"
ImgToTextUrlV2 = "http://127.0.0.1:8881/"
ImgTextToMptUrl = "http://127.0.0.1:8882/"
#ImgTextToMptUrl = "https://ws-45278d2f-b1ee-4619-b0a0-8bd979f96562-debug.rde-ws.gic-sq.lanrui-ai.com/llama2_api/"
#ImgMptToMusicUrl = "https://ws-eaefff98-4fc2-4c66-a75c-f5df074b74cb-debug.rde-ws.gic-sq.lanrui-ai.com/"
ImgMptToMusicUrl = "http://127.0.0.1:8883/"

zhipuai.api_key = "cdc96e172da543a30c1923cc2c95f3ca.otuozN0TTHjgKmd3"


#根据图片内容调用模型识别图片内容
def imageBase64ToText(imgBase64):
	response = requests.post(ImgToTextUrl, json={
	  "data": [
	    "data:image/jpeg;base64,"+imgBase64
	]}).json()
	imgData = response["data"][0]
	error = ""

	if imgData == "":
		error = "cant not trans img content! error!"

	return {
		"imgText" : imgData,
		"error" : error
	}

def imgMptToMusic(musicPmt):
	client = Client(ImgMptToMusicUrl)
	musicGenRes = client.predict(
				"large",	# str in 'Model' Radio component
				musicPmt, # str  in 'Input Text' Textbox component
				"",
				30,	# int | float (numeric value between 1 and 120) in 'Duration' Slider component
				250,	# int | float in 'Top-k' Number component
				1,	# int | float in 'Top-p' Number component
				1,	# int | float in 'Temperature' Number component
				3,	# int | float in 'Classifier Free Guidance' Number component
				fn_index=1
    )
	return {
		"musicPath" : musicGenRes,
		"error" : ""
	}

#解析音乐内容
def GetMusicPmt(result):
  lines = result.split('\n')
  for line in lines:
    if '"prompt"' in line:
      return line

def IsJson(jsonStr):
    try:
       	jsonMap = json.loads(jsonStr)
    except ValueError:
        return False
    return jsonMap

#图片内容生成prompt
def imgtextToMpt(imgText):
	musicMpt = "我给你输入一段文字,帮我描述成一首MusicGen音乐prompt，包含音乐风格、情绪、参与演奏的乐器、音乐意境等元素。prompt 样例: “An 80s driving pop song with heavy drums and synth pads in the background”。输出的 prompt控制在30字内，不需要寒暄、打招呼等语气，直接输出prompt。输出Json格式: {\"title\":\"结果标题\", \"prompt\":\"结果prompt\"} 我输入的内容是“"+imgText+"”，没有更多信息可以提供，请创作,你只给我一个json格式内容就好，不需要额外信息, prompt内容用英文返回"
	response = zhipuai.model_api.invoke(
		model="chatglm_turbo",
		prompt=[{"role": "user", "content": musicMpt}],
		top_p=0.7,
		temperature=0.9,
	)
	if 200 == response["code"] and 'data' in response and 'choices' in response["data"]["choices"] and response["data"]["choices"][0]["content"]:
		input_str = response["data"]["choices"][0]["content"]
		input_str = re.findall(r'{.*?}', input_str)
		input_str = input_str[0].replace("\\", "")
		imgMptMap = json.loads(input_str)
		return {
			"imgMpt" : imgMptMap["prompt"],
			"error" : "",
			"tag" : "right",
		}
	else:
		return {
			"imgMpt" : imgText,
			"error" : "",
			"tag" : response["msg"],
		}

def Mp3TxtToMusic(mp3PathUrl, userTxt):
	client = Client(ImgMptToMusicUrl)
	musicGenRes = client.predict(
				"melody",	# str in 'Model' Radio component
				userTxt,
				mp3PathUrl,	# str (filepath or URL to file) in 'Melody Condition (optional)' Audio component
				15,	# int | float (numeric value between 1 and 120) in 'Duration' Slider component
				250,	# int | float in 'Top-k' Number component
				1,	# int | float in 'Top-p' Number component
				1,	# int | float in 'Temperature' Number component
				3,	# int | float in 'Classifier Free Guidance' Number component
				fn_index=1
    )
	return {
		"musicPath" : musicGenRes,
		"error" : ""
	}

#根据图片URL下载图片内容,获取图片压缩base64信息
def ImageUrlToText(imgUrl):
	#下载文件获取文件内容进行base64内容读取
	#获取图片内容转为base64内容
	# 将这个图片保存在内存
	#response = requests.get(imgUrl) 
	# 将这个图片从内存中打开，然后就可以用Image的方法进行操作了
	#image = Image.open(BytesIO(response.content))
	# 得到这个图片的base64编码
	#imageBase64 = str(base64.b64encode(BytesIO(response.content).read()), 'utf-8')
	#print(imageBase64)
	# 打印出这个base64编码
	#return imageBase64ToText(imageBase64)

	client = Client(ImgToTextUrlV2)
	result = client.predict(
		imgUrl, # str (filepath on your computer (or URL) of image) in 'image' Image component
		api_name="/predict"
	)
	return {
		"imgText" : result,
		"error" : ""
	}

