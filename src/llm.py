import os
import time
from tqdm import tqdm
import openai

# Use standard OpenAI API with system environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Model to use (can be changed to gpt-4, gpt-4-turbo, etc.)
MODEL = os.environ.get("TASQL_MODEL", "gpt-4o-mini")


def connect_gpt4(message, prompt):
    response = openai.ChatCompletion.create(
                    model=MODEL,
                    messages = [{"role":"system","content":f"{message}"},
                                {"role":"user", "content":f"{prompt}"}],
                    temperature=0,
                    max_tokens=800,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                    stop = None)
    return response['choices'][0]['message']['content']


def collect_response(prompt, max_tokens = 800, stop = None):
    while 1:
            flag = 0
            try:
                response = openai.ChatCompletion.create(
                    model=MODEL,
                    messages = [{"role":"system","content":"You are an AI assistant that helps people find information."},
                                {"role":"user", "content":f"{prompt}"}],
                    temperature=0,
                    max_tokens=max_tokens,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                    stop = stop)
                response = response['choices'][0]['message']['content']
                flag = 1
                
            except Exception as e:
                print(e)
                time.sleep(1)
            if flag == 1:
                break
    return response

