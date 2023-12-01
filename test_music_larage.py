from gradio_client import Client

client = Client("https://ws-eaefff98-4fc2-4c66-a75c-f5df074b74cb-debug.rde-ws.gic-sq.lanrui-ai.com/")
result = client.predict(
		"facebook/musicgen-stereo-large",
		"",
		"Default",
		"Create a ambient electronic track inspired by Vincent van Gogh's 'Starry Night'. Imagine the swirling clouds and stars in the night sky as a sonic journey through space and time. Incorporate elements of space and cosmic themes, with a focus on creating a dreamy and ethereal atmosphere. Use a mix of synth pads, ambient textures, and subtle rhythmic elements to create a sense of floating and weightlessness. The track should evoke a sense of wonder and awe at the beauty of the universe, as seen through the eyes of van Gogh's painting",
		"",	# str (filepath on your computer (or URL) of file) in 'File' Audio component
		10,	# int | float (numeric value between 1 and 120) in 'Duration' Slider component
		250,	# int | float  in 'Top-k' Number component
		1,	# int | float  in 'Top-p' Number component
		1,	# int | float  in 'Temperature' Number component
		3,	# int | float  in 'Classifier Free Guidance' Number component
		fn_index=2
)
print(result)