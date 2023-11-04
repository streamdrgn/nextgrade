from django.shortcuts import render

def save(request):
    # 작성한 데이터를 가져옵니다.
    name = request.POST['name']
    neis = request.POST['neis']
    career = request.POST['career']
    department = request.POST['department']
    year = request.POST['year']
    subject = request.POST['subject']

    # Survey 모델의 인스턴스를 생성합니다.
    survey = Survey(
        name=name,
        neis=neis,
        career=career,
        department=department,
        year=year,
        subject=subject,
    )

    # Survey 모델의 인스턴스를 데이터베이스에 저장합니다.
    survey.save()

    return render(request, 'save.html')


def index(request):
    # Survey 모델의 모든 인스턴스를 가져옵니다.
    surveys = Survey.objects.all()

    # Survey 모델의 모든 인스턴스를 템플릿에 전달합니다.
    context = {
        'surveys': surveys,
    }

    return render(request, 'index.html', context)