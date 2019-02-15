var questionIndex = 2;
var questions = [];
window.onload = function () {
    showIntroduction(questionIndex);
};

function showIntroduction() {
    var introduction = document.getElementsByClassName("question introduction")[0];
    introduction.style.display = "block";
}

function hideIntroduction() {
    var introduction = document.getElementsByClassName("question introduction")[0];
    console.log(introduction);
    introduction.style.display = "none";
    showQuestion(questionIndex);
}

// Next/previous controls
function updateQuestion(n) {
    showQuestion(questionIndex += n);
}

function showQuestion(n) {
    console.log("showing questions");
    var i;
    questions = document.getElementsByClassName("question");
    if (n > questions.length) {
        questionIndex = 2
    }
    if (n < 2) {
        questionIndex = questions.length
    }
    for (i = 0; i < questions.length; i++) {
        questions[i].style.display = "none";
    }
    questions[questionIndex-1].style.display = "block";
}

function showNext() {
    var next = questions[questionIndex-1].querySelector(".next-button");
    var submit = questions[questionIndex-1].querySelector(".submit-button");
    if (next != null) {
        next.disabled = false;
    }
    else if (submit != null) {
        submit.disabled = false;
    }
}