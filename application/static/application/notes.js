var notes_button = $("#add-notes");
var text_box = $("#text-box");
console.log(text_box.text);

function showTextArea() {
    console.log("test");
    text_box.show();
    notes_button.hide();
}