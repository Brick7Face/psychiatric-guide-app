var questionIndex = 1;
var questions = [];
window.onload = function () {
    showQuestion(questionIndex);
};

// Next/previous controls
function updateQuestion(n) {
    showQuestion(questionIndex += n);
}

function showQuestion(n) {
    var i;
    questions = document.getElementsByClassName("question");
    if (n > questions.length) {
        questionIndex = 1
    }
    if (n < 1) {
        questionIndex = questions.length
    }
    for (i = 0; i < questions.length; i++) {
        questions[i].style.display = "none";
    }
    questions[questionIndex-1].style.display = "block";
}

function showNext() {
    questions[questionIndex-1].querySelector("#next-button").style.display = "block";
}