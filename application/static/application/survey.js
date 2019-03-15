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
    introduction.style.display = "none";
    showQuestion(questionIndex);
}

// Next/previous controls
function updateQuestion(n) {
    showQuestion(questionIndex += n);
}

function showQuestion(n) {
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
    var question = questions[questionIndex - 1];
    question.style.display = "block";

    // set width of choices based on how many choices there are
    var choices = question.querySelector("#choice-container").children;
    var width = (100 / choices.length).toString() + "%";
    for (let choice of choices) {
        choice.style.width = width;
    }
}

function showNext() {
    var next = questions[questionIndex - 1].querySelector(".next-button");
    var submit = questions[questionIndex - 1].querySelector(".submit-button");
    if (next != null) {
        next.disabled = false;
    } else if (submit != null) {
        submit.disabled = false;
    }
}