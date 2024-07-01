import aiohttp
import asyncio
import json

api_url = 'https://reverse.mubi.tech/v1/chat/completions'

api_url1 = 'https://reverse.mubi.tech/v1/images/generations'

headers = {
    'Content-Type': 'application/json',
    'Origin': 'https://gptcall.net/',
    'Referer': 'https://gptcall.net/'
}

headers1 = {
    'Content-Type': 'application/json',
}

async def generate_text_on_script_no_command(text):
    data = {
        'model': 'gpt-4o',
        'messages': [
            {
                'role': "assistant",
                'content': "Assistant",
            },
            {
                'role': "user",
                'content': text
            }
        ]
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, json=data, headers=headers) as response:
            json_data = await response.json()
            result = json_data['choices'][0]['message']['content']
            return result
            
def generate(text):
  return asyncio.run(generate_text_on_script_no_command(text))
  
async def generate_image_on_script_no_command(text):
    data1 = {
        'model': 'dreamshaper-8',
        'prompt': text
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(api_url1, json=data1, headers=headers1) as response:
            json_data = await response.json()
            result = json_data['data'][0]['url']
            return result
            
def image(text):
  return asyncio.run(generate_image_on_script_no_command(text))
  
__all__ = ["generate","image"]