from transformers import pipeline

classifier = pipeline('sentiment-analysis')

result = classifier ('I love to code in python with pytorch')

print(result)