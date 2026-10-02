import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions, call_function
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,  # type: ignore
    tools=available_functions,  # type: ignore
    temperature=0,
)

if response.usage is None:
    raise RuntimeError("API request failed or returned no usage data.")

if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")

message = response.choices[0].message
if message.tool_calls:
    for tool_call in message.tool_calls:
        function = getattr(tool_call, "function", None)
        if function is None:
            continue
        result_message = call_function(tool_call, args.verbose)
        if not result_message["content"]:
            raise RuntimeError("Function call returned no content")
        if args.verbose:
            print(f"-> {result_message['content']}")
else:
    print(message.content)
