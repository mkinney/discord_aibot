from pygpt4all.models.gpt4all_j import GPT4All_J

def new_text_callback(text):
    print(text, end="")

model = GPT4All_J('ggml-gpt4all-j-v1.3-groovy.bin')
model.generate("Once upon a time, ", n_predict=55, new_text_callback=new_text_callback)
