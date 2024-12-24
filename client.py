from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named neura like Alexa and  Google Cloud."},
        {
            "role": "user",
            "content": "what is programming?"
        }
    ]
)

print(completion.choices[0].message)