from litellm import completion
import os

## set ENV variables
os.environ["gemini_API_KEY"] = "AIzaSyDkK_3dx9IafgTQzuPn9Ov18zqfr9PT_Zo"
def call_gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{ "content": "Did you know about pakistan?","role": "user"}]
    )
    print(response["choices"][0]["message"]["content"])