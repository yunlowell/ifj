from django.shortcuts import render

def main(request):
    return render(request, 'main.html')  # main.html 템플릿을 렌더링
