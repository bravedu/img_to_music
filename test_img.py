from gradio_client import Client

client = Client("https://ws-eaefff98-4fc2-4c66-a75c-f5df074b74cb-debug.rde-ws.gic-sq.lanrui-ai.com/")
result = client.predict(
		"facebook/musicgen-large",	# str  in 'Model' Radio component
		"",	# str  in 'Model Path (custom models)' Textbox component
		"Default",	# str  in 'Decoder' Radio component
		"A somber piano melody plays in the background as an anime girl hugs her face in the snow, a distant picture of a man visible in the distance, the melancholy atmosphere evoking feelings of longing and loss.",	# str  in 'Input Text' Textbox component
		"",	# str (filepath on your computer (or URL) of file) in 'File' Audio component
		15,	# int | float (numeric value between 1 and 120) in 'Duration' Slider component
		250,	# int | float  in 'Top-k' Number component
		1,	# int | float  in 'Top-p' Number component
		1,	# int | float  in 'Temperature' Number component
		3,	# int | float  in 'Classifier Free Guidance' Number component
		fn_index=2
)
print(result)