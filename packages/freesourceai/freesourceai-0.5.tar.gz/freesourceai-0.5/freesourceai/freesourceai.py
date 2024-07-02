import aiohttp
import asyncio
import json

models = ["pastel-mix-anime", "dreamshaper-8", "anything-v5", "realistic-vision-v5", "am-i-real-v4.1", "openjourney-v4"]
models1 = ["gpt-3.5-turbo", "gpt-4", "gpt-4o"]

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

async def generate_text_on_script_no_command(model, text):
    if model in models1:
        data = {
            'model': model,
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
    else:
        raise ValueError("Model is not valid for FreeSourceAI. Work has been stopped.")

def generate(model, *, text):
    return asyncio.run(generate_text_on_script_no_command(model, text))

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

async def generate_image_on_script_no_command(model, text):
    if model in models:
        data1 = {
            'model': model,
            'prompt': text
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(api_url1, json=data1, headers=headers1) as response:
                json_data = await response.json()
                result = json_data['data'][0]['url']
                return result
    else:
        raise ValueError("Model is not valid for FreeSourceAI. Work has been stopped.")

def image(model, *, text):
    safe = asyncio.run(is_safe_text(text))
    if not safe:
        raise ValueError("Input text contains explicit content. Image generation aborted.")
    else:
        return asyncio.run(generate_image_on_script_no_command(model, text))

all = ["generate", "image"]