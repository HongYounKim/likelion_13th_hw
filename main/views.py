from django.shortcuts import render

# Create your views here.
def first_page(request):
    context = {
        'week': '2주차',
        'info': {'template': 'view에 작성된 data를 가져오고, 반복문 등 기능 수행', 'static': '웹페이지에서 사용되는 정적인 파일을 저장하는 디렉토리', 'note': '아기사자 화이팅!'},
        'shortKeys': [
            '들여쓰기: Tab',
            '내어쓰기: Shift + Tab',
            '주석 처리: 윈도우 - Ctrl + /, 맥 - command + /',
            '자동 정렬: Shift + Alt + F or Ctrl + K + F',
            '한 줄 이동: Alt + 방향키(위/아래)',
            '한 줄 삭제: Ctrl + Shift + k or Ctrl + x',
            '같은 단어 전체 선택: Ctrl + Shift + L'
        ]
}
    return render(request, 'main/first_page.html', context)

def second_page(request):
    return render(request, 'main/second_page.html')

