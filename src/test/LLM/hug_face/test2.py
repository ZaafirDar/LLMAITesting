from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

custom_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")

classifier = pipeline('sentiment-analysis', model=model, tokenizer=custom_tokenizer)

result = classifier ('I love to code in python with pytorch')

print(result)