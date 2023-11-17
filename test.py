import requests,json

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
        print("ERROR")
        return False
    return jsonMap


#imgMptStr = '" Here is a MusicGen prompt based on the description you provided:\n\n\"Title\": \"Lost in Memories\",\n\"Prompt\": \"A gentle, melancholic piano melody with a hint of sadness, evoking a sense of nostalgia and longing. The music builds in intensity, with a subtle hint of resolution, as if the little girl is finding solace in her memories of her grandma. The overall mood is bittersweet, capturing the bittersweet nature of memories and the longing for those who are no longer with us.\"\n}\nI hope this MusicGen prompt captures the mood and emotion of the scene you described! Let me know if you have any other questions or if there\'s anything else I can help you with."'
imgMptStrOrigin = '''
, prompt:"a close up of a rain shower with a black background", response:"' Sure! Here is a description of a close-up of a rain shower with a black background:\n{\n"Raindrops dance on the black background, creating a mesmerizing display of light and shadow. The water droplets are large and plump, glistening in the dim light. The sound of the rain is loud and intense, creating a sense of isolation and tranquility. The black background provides a stark contrast to the vibrant colors of the raindrops, making them stand out even more. The scene is almost surreal, as if you are trapped in a dreamlike world. The rain shower creates a sense of mystery and wonder, drawing you in and refusing to let you go."\n}\nI hope this description captures the beauty and atmosphere of the rain shower with a black background! Let me know if you have any other questions.'
'''

imgMptStr = GetMusicPmt(imgMptStrOrigin)
if imgMptStr==None:
    mgMptMap = imgMptStrOrigin.split('prompt:"')[1].split('"')[0]
    print(mgMptMap)
elif '{' not in imgMptStr:
    imgMptStr = "{"+imgMptStr+"}"
    mgMptMap = IsJson(imgMptStr)
    print(mgMptMap)
