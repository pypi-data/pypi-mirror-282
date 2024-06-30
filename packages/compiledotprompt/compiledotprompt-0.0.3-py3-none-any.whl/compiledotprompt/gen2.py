import os
import re
import click
from langchain_aws import ChatBedrock

# This file was produced by AI from a prompt and shouldn't be edited directly.

def expand_directives(content, base_path):
    def replace_directive(match):
        directive, filename = match.groups()
        file_path = os.path.join(base_path, filename)
        
        if directive == 'raw':
            with open(file_path, 'r') as f:
                return f.read()
        elif directive == 'prompt':
            return expand_directives(read_prompt_file(file_path), os.path.dirname(file_path))
        
    pattern = r'@(raw|prompt)\((.*?)\)'
    return re.sub(pattern, replace_directive, content)

def read_prompt_file(prompt_file):
    with open(prompt_file, 'r') as f:
        return f.read()

def generate_code(prompt):
    chat = ChatBedrock(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
        region_name="us-east-1"
    )
    
    messages = [
        {"role": "system", "content": "Output just the file content, nothing else. Do not print any introductory text before the code. Do not enclose the code in triple quotes. Include a comment in the code saying that this file was produced by AI from a prompt and shouldn't be edited directly, unless generating json or other file formats that don't support comments."},
        {"role": "human", "content": "Hello world in python"},
        {"role": "assistant", "content": "print('Hello world')"},
        {"role": "human", "content": prompt}
    ]
    
    response = chat.invoke(messages)
    return response.content

@click.command()
@click.argument('prompt_file', type=click.Path(exists=True))
def main(prompt_file):
    base_path = os.path.dirname(prompt_file)
    prompt_content = read_prompt_file(prompt_file)
    expanded_prompt = expand_directives(prompt_content, base_path)
    
    generated_code = generate_code(expanded_prompt)
    
    output_file = prompt_file.rsplit('.prompt', 1)[0]
    with open(output_file, 'w') as f:
        f.write(generated_code)
    
    click.echo(f"Generated code saved to {output_file}")

if __name__ == '__main__':
    main()