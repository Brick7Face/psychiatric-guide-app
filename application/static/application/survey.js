var slideIndex = 1;
window.onload = function () {
    showQuestion(slideIndex);
};

// Next/previous controls
function updateQuestion(n) {
    showQuestion(slideIndex += n);
}

function showQuestion(n) {
    var i;
    var questions = document.getElementsByClassName("question");
    if (n > questions.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = questions.length
    }
    for (i = 0; i < questions.length; i++) {
        questions[i].style.display = "none";
        questions[i].className = questions[i].className.replace(" active", "");
    }
    questions[slideIndex-1].style.display = "block";
    questions[slideIndex-1].className += " active"
}
