import requests,json,os,base64
from gradio_client import Client
from PIL import Image
from io import BytesIO

#图片识别成文本URL
ImgToTextUrl = "http://127.0.0.1:8881/run/predict"
ImgToTextUrlV2 = "http://127.0.0.1:8881/"
ImgTextToMptUrl = "http://127.0.0.1:8882/"
ImgMptToMusicUrl = "https://ws-eaefff98-4fc2-4c66-a75c-f5df074b74cb-debug.rde-ws.gic-sq.lanrui-ai.com/"

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
				musicPmt,	
				"",	# str (filepath or URL to file) in 'Melody Condition (optional)' Audio component
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

#解析音乐内容
def GetMusicPmt(result):
  lines = result.split('\n')
  for line in lines:
    if '"Prompt"' in line:
      return line

def IsJson(jsonStr):
    try:
       	jsonMap = json.loads(jsonStr)
    except ValueError:
        return False
    return jsonMap

#图片内容生成prompt
def imgtextToMpt(imgText):
	response = requests.post(ImgTextToMptUrl, json={
	"prompt" : imgText,
	"history": [
	    [
	        "<<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\n            If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.\n<</SYS>>\n\n我给你输入一段文字,帮我描述成一首MusicGen音乐prompt，包含音乐元素。prompt 样例: “An 80s driving pop song with heavy drums and synth pads in the background”。输出的 prompt控制在30字内，不需要寒暄、打招呼等语气，直接输出prompt。输出Json格式: {Title: 结果标题, prompt : 结果prompt} 我输入的内容是“anime girl hugging her face in the snow with a picture of a man in the background”，没有更多信息可以提供，请创作即可,结尾不需要任何反问，不合适我会重新询问。",
	        " Understood! Based on the input you provided, here is a MusicGen prompt for you:\n{Title: \"Wistful Winter Embrace\", prompt: \"An ethereal anime girl hugging her face in the snow, with a hazy picture of a man in the background, evoking a sense of longing and nostalgia.\"}\nI hope this prompt captures the mood and atmosphere you were looking for! Let me know if you have any other questions or if there's anything else I can help you with."
	    ],
	    [
	        "在prompt字段中内容应该是一段musicGen可生成音乐的描述，根据输入的内容来创造出来的",
	        " Ah, I see! In that case, here's a MusicGen prompt based on your input:\n{Title: \"Snowy Serenity\", prompt: \"A gentle, atmospheric piece with a soothing melody and a subtle rhythm, evoking a sense of peacefulness and tranquility, perfect for a winter wonderland scene with an anime girl hugging her face in the snow.\"}\nI hope this prompt helps generate a beautiful and fitting piece of music for your anime girl in the snow scene! Let me know if you have any other questions or if there's anything else I can help you with."
	    ],
	    [
	        "你这个回答非常不错,prompt 不需要重复输入的关键词内容,可以替换为乐器、风格等元素",
	        " Ah, I see! Yes, you're right. The `prompt` field in the MusicGen prompt can be replaced with more specific elements such as instruments, genres, or moods to help generate a more tailored piece of music. Here's an updated prompt based on your input:\n{Title: \"Winter's Embrace\", prompt: \"A delicate piano melody with a hint of melancholy, evoking a sense of longing and nostalgia, perfect for a snowy landscape with an anime girl hugging her face in the snow.\"}\nI hope this updated prompt helps generate a beautiful and fitting piece of music for your anime girl in the snow scene! Let me know if you have any other questions or if there's anything else I can help you with."
	    ],
	    [
	        "非常棒, 请在回答中仅输出 MusicGen prompt 的 json格式内容即可",
	        " Of course! Here is the MusicGen prompt in JSON format:\n{\n\"Title\": \"Winter's Embrace\",\n\"Prompt\": \"A delicate piano melody with a hint of melancholy, evoking a sense of longing and nostalgia, perfect for a snowy landscape with an anime girl hugging her face in the snow.\"\n}\n\nI hope this helps! Let me know if you have any other questions."
	    ],
	    [
	        "以后我给出任何音乐描述都按照我们前面的约定格式返回",
	        " Understood! I will always return the MusicGen prompt in the format we agreed upon, regardless of the music description you provide in the future. Please feel free to give me any music description, and I will generate the corresponding MusicGen prompt for you."
	    ]
	]}).json()
	imgMptStr = GetMusicPmt(response["response"])
	if imgMptStr == None:
		imgMptStr = response["response"].split('prompt:"')[1].split('"')[0]
		return {
				"imgMpt" : imgMptStr,
				"error" : ""
			}
	elif '{' not in imgMptStr:
			imgMptStr = "{"+imgMptStr+"}"
			imgMptMap = IsJson(imgMptStr)
			if imgMptMap == False:
				return {
					"imgMpt" : "",
					"error" : "图片识别失败~，请更换重试"
				}
			#imgMptMap = json.loads(imgMptStr)
			return {
				"imgMpt" : imgMptMap["Prompt"],
				"error" : ""
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

