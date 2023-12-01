import zhipuai,json,re

zhipuai.api_key = "cdc96e172da543a30c1923cc2c95f3ca.otuozN0TTHjgKmd3"


def IsJson(jsonStr):
    try:
       	jsonMap = json.loads(json.dumps(jsonStr))
    except ValueError:
        return False
    return jsonMap


def invoke_example():
    imgText = "An 80s driving pop song with heavy drums and synth pads in the background"
    musicMpt = "我给你输入一段文字,帮我描述成一首MusicGen音乐prompt，包含音乐风格、情绪、参与演奏的乐器、音乐意境等元素。prompt 样例: “An 80s driving pop song with heavy drums and synth pads in the background”。输出的 prompt控制在30字内，不需要寒暄、打招呼等语气，直接输出prompt。输出Json格式: {\"title\":\"结果标题\", \"prompt\":\"结果prompt\"} 我输入的内容是“"+imgText+"”，没有更多信息可以提供，请创作,你只给我一个json格式内容就好，不需要额外信息, prompt内容用英文返回"

    response = zhipuai.model_api.invoke(
        model="chatglm_turbo",
        prompt=[{"role": "user", "content": musicMpt}],
        top_p=0.7,
        temperature=0.9,
    )
    return response
    #return json.dumps(res, indent=4)



res = invoke_example()

input_str = res["data"]["choices"][0]["content"]

input_str = re.findall(r'{.*?}', input_str)
input_str = input_str[0].replace("\\", "")

data = json.loads(input_str)

print(data["prompt"])
# 将数据转换为标准 JSON 格式
#output_json = json.dumps(data, indent=4)

#print(output_json)