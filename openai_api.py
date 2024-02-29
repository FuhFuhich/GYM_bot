import openai
from config import load_config

config = load_config()
openai.api_key = config.get('openai_api_key')


def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=128,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
