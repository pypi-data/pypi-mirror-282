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
        'model': 'gpt-4',
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
    asyncio.run(generate_text_on_script_no_command(text))

async def is_safe_text(text):
    data = {
        'model': 'gpt-4',
        'messages': [
            {
                'role': "system",
                'content': "Ты AI ассистент, который определяет, является ли текст 18+ или нет. Ответь одним словом без символов и букв верхнего регистра 'да' если текст безопасен и 'нет' если текст 18+."
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
            return result.strip().lower() == 'да'

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
    safe = asyncio.run(is_safe_text(text))
    if not safe:
        raise ValueError("Input text contains explicit content. Image generation aborted.")
    else:
        asyncio.run(generate_image_on_script_no_command(text))

all = ["generate", "image"]