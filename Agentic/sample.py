import requests

# 0...3 : AccountID
# c..d : TOKEN
API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/AccountID/ai/run/"
headers = {"Authorization": "Bearer TOKEN"}

def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()

inputs = [
    { "role": "system", "content": "You are a friendly assistan that helps write stories" },
    { "role": "user", "content": "what is today?"}
];
# output = run("@cf/moonshotai/kimi-k2.7-code", inputs)
output = run("@cf/qwen/qwen3.8-27b", inputs)
# print(output)
print(output['result']['choices'][0]['message']['content'])
