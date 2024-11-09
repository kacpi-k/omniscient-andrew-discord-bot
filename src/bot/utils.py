from groq.types.chat import ChatCompletion


def print_response_usage(chat_completion: ChatCompletion):
    prompt_tokens = chat_completion.usage.prompt_tokens
    completion_tokens = chat_completion.usage.completion_tokens
    total_tokens = chat_completion.usage.total_tokens
    prompt_time = chat_completion.usage.prompt_time
    completion_time = chat_completion.usage.completion_time
    total_time = chat_completion.usage.total_time

    print(f'Prompt tokens: {prompt_tokens}')
    print(f'Completion tokens: {completion_tokens}')
    print(f'Total tokens: {total_tokens}')
    print(f'Prompt time: {prompt_time}s')
    print(f'Completion time: {completion_time}s')
    print(f'Total time: {total_time}s')