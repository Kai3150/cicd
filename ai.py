from lib2to3.fixes.fix_input import context
from transformers import pipeline

classifier = pipeline('sentiment-analysis')
classifier('We are very happy to introduce pipeline to the transformers repository.')



import requests
from PIL import Image
from transformers import pipeline

# Download an image with cute cats
url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/coco_sample.png"
image_data = requests.get(url, stream=True).raw
image = Image.open(image_data)

# Allocate a pipeline for object detection
question_answerer = pipeline(task="question-answering")

question_answerer(queation="Who are you", context="I am Anomary")
