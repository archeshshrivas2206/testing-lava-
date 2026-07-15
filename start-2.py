import ollama

response=ollama.list()

res= ollama.chat(
    model="llama3.2:latest",
    messages=[
        {"role": "user", "content":"why is sky blue?"},
        ],
        stream=True,
)
for chunk in res:

    print(chunk["message"]["content"],end="", flush=True)


# this shows everything about the ollama model that has been selcted
# res2=ollama.generate( 
#     model="llama3.2",
#     prompt="why is the ocean salty",
    
# )

# print(ollama.show("llama3.2"))


