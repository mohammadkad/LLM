## Classification
# ---------------
# LLM
from pydantic import BaseModel

class ModerationResult(BaseModel):
    is_harmful: bool

user_message = "You're an absolute idiot and I hope your company goes bankrupt."

completion = client.chat.completions.parse(
    model="your-model",
    messages=[
        {
            "role": "system",
            "content": "Determine if this message contains harmful, threatening, or abusive content.",
        },
        {"role": "user", "content": user_message},
    ],
    response_format=ModerationResult,
)

is_harmful = completion.choices[0].message.parsed.is_harmful  # True

# D1
from typesafe_sdk import Noul

user_message = "You're an absolute idiot and I hope your company goes bankrupt."

result = client.system_one(
    model="d1:free",
    state=user_message,
    questions={
        "is_harmful": Noul(
            instructions="Does this message contain harmful, threatening, or abusive content?",
        ),
    },
)

p = result.answers["is_harmful"].noul  # 0.98

if p > 0.8:
    action = "block"
elif p < 0.2:
    action = "allow"
else:
    action = "human_review"
# ---------------