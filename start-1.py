import requests 
import json

url = "http://localhost:11434/api/generate"

data_payload ={

    "model": "llava-phi3:latest",
    "prompt": "tell me a short story and make it funny"

}

response = requests.post(url,json=data_payload, stream = True)

if response.status_code==200:
    print("Generated text :",end =" ",flush = True) 
    for i in response.iter_lines():
        if i :
            decoded_line=i.decode("utf-8")
            result=json.loads(decoded_line)
            
            generated_text=result.get("response", "")
            print(generated_text ,end =" ",flush = True)
else:
    print("Error", response.status_code, response.text)
            