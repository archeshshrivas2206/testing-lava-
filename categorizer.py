import ollama 
import os 


model="llama3.2:latest"

input_file="./data/grocery_list.txt"
output_file="./data/outputfile.txt"


if not os.path.exists(input_file):
    print("input file not found")
    exit(1)

with open(input_file,"r") as f:
    items=f.read().strip() 


prompt="""you are an assistant that categorizes and sorts grocery itemss. 
here is a list of grocer items: 
{items}
plesae:
1. categorize these items into appropriate categories.
2.sort the items alphabetically within each category. 
3. present the categorised list in a clear and organised manner.

"""

res=ollama.generate(model=model,prompt=prompt)
generatedtext=res.get("response","")

with open(output_file,"w") as f:
    f.write(generatedtext.strip())

print(f"categorised lisee saved to {output_file} ")

