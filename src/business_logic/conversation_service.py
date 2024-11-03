import os
from openai import AzureOpenAI
from dotenv import load_dotenv


def get_conversation():
    # MDと同じ書き方
    load_dotenv()
    model_deploy_name = os.getenv("MODEL_DEPLOY_NAME")
    aoai_endpoint = os.getenv("AOAI_ENDPOINT")
    api_version = os.getenv("API_VERSION")
    api_key = os.getenv("OPENAI_API_KEY")

    client = AzureOpenAI(
        azure_endpoint=aoai_endpoint, api_version=api_version, api_key=api_key
    )

    messages = [
        {
            "role": "system",
            "content": "あなたは私のAIアシスタントです。できるだけ簡潔に回答してください。",
        },
        {"role": "user", "content": "ビジネスで謝罪するメールの文例。"},
        {
            "role": "assistant",
            "content": "会議に遅れてしまったことを謝罪するメール文面を書いてください",
        },
        # {
        #     "role": "system",
        #     "content": "あなたは私のAIアシスタントです。できるだけ簡潔に回答してください。",
        # },
        # {"role": "user", "content": "同窓会の紹介状の文例。"},
        # {
        #     "role": "assistant",
        #     "content": "尊敬するXXさんへ\n\nお元気でお過ごしでしょうか。私たちは、XX年に同じ学校で学んだ仲間たちで、このたび同窓会を開催することになりました。\n\n日時：XX年XX月XX日（土）XX時から\n場所：XXホテル 2階 パーティールーム\n\n当日は、",
        # },
    ]

    response = client.chat.completions.create(
        model=model_deploy_name,
        messages=messages,
        temperature=0.5,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content


get_conversation()

