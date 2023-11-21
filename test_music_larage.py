from gradio_client import Client

client = Client("https://ws-eaefff98-4fc2-4c66-a75c-f5df074b74cb-debug.rde-ws.gic-sq.lanrui-ai.com/")
result = client.predict(
		"facebook/musicgen-large",	# str  in 'Model' Radio component
		"Default",	# str  in 'Decoder' Radio component
		"Howdy!",	# str  in 'Input Text' Textbox component
		"",	# str (filepath on your computer (or URL) of file) in 'File' Audio component
		1,	# int | float (numeric value between 1 and 120) in 'Duration' Slider component
		5,	# int | float  in 'Top-k' Number component
		5,	# int | float  in 'Top-p' Number component
		5,	# int | float  in 'Temperature' Number component
		5,	# int | float  in 'Classifier Free Guidance' Number component
		fn_index=2
)
print(result)