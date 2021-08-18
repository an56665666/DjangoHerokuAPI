from django.http.response import JsonResponse
from django.shortcuts import render
import json
from django.http import HttpResponse
# Create your views here.


def APITest(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('UTF-8'))
        res = int(postData['num1']) + int(postData['num2'])
        ores = {"result": res}
        # jres = json.dumps(ores)
        # lres = json.loads(jres)

    # return HttpResponse(json.dumps(f'API Test Success: {num1}+{num2}={num1+num2}'), content_type="application/json")
    # return HttpResponse(json.dumps(f'API Test Success: {num1}'), content_type="application/json")
    return JsonResponse(ores)
