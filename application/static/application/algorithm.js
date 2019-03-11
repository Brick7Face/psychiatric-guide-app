var graph = new joint.dia.Graph;

var steps = JSON.parse($("#steps").text());
var container = $("#algorithm-wrapper")[0];
var screen_width = container.offsetWidth;
var screen_height = container.offsetHeight;

var paper = new joint.dia.Paper({
    el: document.getElementById('algorithm-wrapper'),
    model: graph,
    width: screen_width,
    height: screen_height,
    gridSize: 1
});

var rects = {};

for (var key in steps) {
    var step = steps[key];
    var rect = new joint.shapes.standard.Rectangle();
    var width;
    var height = 100;
    if (step.description.length > 100) {
        width = 250;
    }
    else {
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
        link.router('metro');
        link.appendLabel({
            attrs: {
                text: {
                    text: step.transition
                }
            }
        });
        link.addTo(graph);
    }
}
