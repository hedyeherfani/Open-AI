import os
import openai
import config
openai.api_key = config.OPENAI_API_KEY


def openAI(query):
    response = openai.Completion.create(
        model='text-davinci-002',
        prompt=query,
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        )

    if 'choices' in response:
         if len(response['choices']) > 0:
             answer = response['choices'][0]['text']
         else:
             answer = 'oops'
    else:
      answer = 'oops'

    return answer
