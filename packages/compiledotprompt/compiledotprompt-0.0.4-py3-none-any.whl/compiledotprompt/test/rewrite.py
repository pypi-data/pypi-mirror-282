# This file was produced by AI from a prompt and shouldn't be edited directly.

import argparse
from langchain_aws import ChatBedrock

def rewrite_text(input_text):
    chat = ChatBedrock(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
        region_name="us-east-1"
    )

    prompt = f"""
    Please rewrite the following text in professional American English:

    {input_text}

    Maintain the original meaning and intent, but improve the language, grammar, and style to make it more polished and suitable for a professional context.
    """

    response = chat.invoke(prompt)
    return response.content

def main():
    parser = argparse.ArgumentParser(description="Rewrite text in professional American English using an LLM.")
    parser.add_argument("input_text", help="The text to be rewritten")
    args = parser.parse_args()

    rewritten_text = rewrite_text(args.input_text)
    print("Rewritten text:")
    print(rewritten_text)

if __name__ == "__main__":
    main()