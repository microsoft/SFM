from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
ret = generator("Nature Language Model is")

print(ret[0]['generated_text'])
