from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, 'application/login.html', {'title': 'Login'})  # Renders login.html


def survey(request):
    questions = [
        "Little interest or pleasure in doing things?",
        "Feeling down, depressed or hopeless?",
        "Trouble falling or staying asleep, or sleeping too much?",
        "Feeling tired or having little energy?",
        "Poor appetite or overeating?",
        "Feeling bad about yourself — or that you are a failure or have let yourself or your family down?",
        "Trouble concentrating on things, such as reading the newspaper or watching television?",
        "Moving or speaking so slowly that other people could have noticed? Or so fidgety or restless that you have been moving a lot more than usual?",
        "Thoughts that you would be better off dead, or thoughts of hurting yourself in some way?",
        "How difficult have these problems made it for you to do your work, take care of things at home, or get along with other people?"
    ]
    return render(request, 'application/survey.html', {'questions': questions})
