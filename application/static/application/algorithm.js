var button = $("#set-button")[0];
button.addEventListener("click", setLayout);

var graph = new joint.dia.Graph;

var steps = JSON.parse($("#steps").text());
var container = $("#canvas-wrapper");
var canvas_width = container.innerWidth();
var canvas_height = container.innerHeight() - 50;

var paper = new joint.dia.Paper({
    el: document.getElementById('canvas'),
    model: graph,
    width: 1000,
    height: 1000,
    gridSize: 1,
    restrictTranslate: true
});

var scale = Math.min(canvas_width / 1000, canvas_height / 1000);
paper.scale(scale, scale);

var size = Math.min(canvas_width, canvas_height);
paper.setDimensions(size, size);

var rects = {};

draw();

function draw() {
    for (var key in steps) {
        var step = steps[key];
        var rect = new joint.shapes.standard.Rectangle();
        var width;
        var height = 100;
        if (step.description.length > 100) {
            width = 250;
        } else {
            width = 150;
        }
        var text = joint.util.breakText(step.description, {
            width: width - 50
        });
        rect.position(step.x, step.y);
        rect.resize(width, height);
        rect.attr({
            body: {
                fill: '#2699FB'
            },
            label: {
                text: text,
                fill: 'white',
                fontSize: 12
            }
        });
        rects[key] = rect;
        rect.addTo(graph);

        if (step.previous_step != null) {
            var link = new joint.shapes.standard.Link();
            link.source(rects[step.previous_step]);
            link.target(rects[key]);
            link.router('normal');
            link.appendLabel({
                attrs: {
                    text: {
                        text: step.transition,
                        fontSize: 12
                    }
                }
            });
            link.addTo(graph);
        }
    }
}

function setLayout() {
    console.log("setting layout");
    for (var key in steps) {
        var new_step = steps[key];
        var position = rects[key].get('position');
        new_step.x = position.x;
        new_step.y = position.y;
        steps[key] = new_step;
    }
    var new_steps = JSON.stringify(steps)

    var form = $("#form");

    var field = $('<input></input>');

    field.attr("type", "hidden");
    field.attr("name", "steps");
    field.attr("value", new_steps);

    form.append(field);

    // The form needs to be a part of the document in
    // order for us to be able to submit it.
    form.submit();
}
