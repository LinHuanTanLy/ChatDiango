from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
import openai
from chat.utils.result_utils import django_jsonResponse_success, django_jsonResponse_error

openai.api_key = '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'


def text_chat(request):
    issue = '你是谁？'
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=issue,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6
    )
    result = response.choices[0].text
    print(result)

    return django_jsonResponse_success({}, result_message="hi")
