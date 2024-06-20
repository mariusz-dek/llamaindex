import os
import openai

key = 'sk-xxxx'
os.environ["OPENAI_API_KEY"] = key

openai.api_key = key
