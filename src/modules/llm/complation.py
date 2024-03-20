from openai import OpenAI

# ChatComplationMessageParam をインポート
from openai.types.chat import ChatCompletionMessageParam

client = OpenAI()


def simple_complation(
    content: str,
    system_prompt: str,
    messages_history: list[ChatCompletionMessageParam] = [],
) -> str | None:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            *messages_history,
            {
                "role": "user",
                "content": content,
            },
        ],
    )

    return completion.choices[0].message.content
