# icodeuplay/openai_client.py

import os
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
import time
from gtts import gTTS

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
 raise OpenAIError("The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable")

client = OpenAI(api_key=OPENAI_API_KEY)

def call_completion(prompt, model='gpt-3.5-turbo', max_tokens=300):
 completion = client.chat.completions.create(
  model=model,
  messages=[
   {
    'role': 'user',
    'content': prompt,
   }
  ], max_tokens=max_tokens
 )

 return completion.choices[0].message.content

def text2speech(text, lang='en', output=f'{time.time()}-output.mp3'):
  tts = gTTS(text=text, lang=lang)
  tts.save(output)
  return output