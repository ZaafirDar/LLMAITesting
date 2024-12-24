from transformers import pipeline

qa_pipline = pipeline('question-answering', model='deepset/roberta-base-squad2')

result = qa_pipline(question="What is Hugging Face?", context='Hugging Face is platform for NLP and ML and Engineers and anyone that likes AI/ML')
print(result)