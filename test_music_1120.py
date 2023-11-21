from gradio_client import Client

client = Client("https://ws-eaefff98-4fc2-4c66-a75c-f5df074b74cb-debug.rde-ws.gic-sq.lanrui-ai.com/")
result = client.predict(
		"large",	# str  in 'Model' Radio component
		"An 80s driving pop song with heavy drums and synth pads in the background",	# str  in 'Input Text' Textbox component
		"",	# str (filepath on your computer (or URL) of file) in 'File' Audio component
		10,	# int | float (numeric value between 1 and 120) in 'Duration' Slider component
		250,	# int | float  in 'Top-k' Number component
		1,	# int | float  in 'Top-p' Number component
		1,	# int | float  in 'Temperature' Number component
		3,	# int | float  in 'Classifier Free Guidance' Number component
		fn_index=1
)
print(result)