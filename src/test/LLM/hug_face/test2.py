from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

custom_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")

classifier = pipeline('sentiment-analysis')

result = classifier ('I want to learn how to do AI Modal Benhmarking')

print(result)