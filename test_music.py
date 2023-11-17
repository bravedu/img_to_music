from gradio_client import Client

client = Client("https://ws-d1622ba7-8291-4c04-82fd-9f58d6d0d8d4-debug.rde-ws.gic-sq.lanrui-ai.com/")
result = client.predict(
				"melody",	# str in 'Model' Radio component
				"add piano elements",	# str in 'Input Text' Textbox component
				"https://oss.pengyin.vip/ff547f51f3019e57cf5feecb9ff97fd50510f6a4bf88140222cdbdef57177b30.mp3",	# str (filepath or URL to file) in 'File' Audio component
				15,	# int | float (numeric value between 1 and 120) in 'Duration' Slider component
				250,	# int | float in 'Top-k' Number component
				1,	# int | float in 'Top-p' Number component
				1,	# int | float in 'Temperature' Number component
				3,	# int | float in 'Classifier Free Guidance' Number component
				fn_index=1
)
print(result)