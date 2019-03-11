var graph = new joint.dia.Graph;

var steps = JSON.parse($("#steps").text());

var paper = new joint.dia.Paper({
    el: document.getElementById('algorithm-wrapper'),
    model: graph,
    width: window.outerWidth,
    height: window.outerHeight,
    gridSize: 1
});

var rects = {};

for (var key in steps) {
    var step = steps[key];
    var rect = new joint.shapes.standard.Rectangle();
    var width;
    if (step.text.length > 100) {
        width = 250;
    }
    else {
        width = 150;
    }
    var text = joint.util.breakText(step.text, {
        width: width - 50
    });
    rect.position(100, 30);
    rect.resize(width, 100);
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
        link.router('manhattan');
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
