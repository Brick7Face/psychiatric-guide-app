var edit_button = $("#edit-button");
var save_button = $("#save-button");
var cancel_button = $("#cancel-button");
var link_button = $("#link-dropdown #dropdown-button");
var link_dropdown = $("#link-dropdown");
var algorithm_button = $("#algorithm-dropdown #dropdown-button");
var algorithm_dropdown = $("#algorithm-dropdown");
var loading_icon = $("#loading-icon");

var container = $("#canvas-wrapper");
var canvas_width = container.innerWidth();
var canvas_height = container.innerHeight() - 50;

var graph = new joint.dia.Graph;

var paper = new joint.dia.Paper({
    el: document.getElementById('canvas'),
    model: graph,
    width: 1000,
    height: 1000,
    gridSize: 1,
    background: {
        color: "#F1F9FF"
    },
    restrictTranslate: true,
    interactive: false
});

var scale = Math.min(canvas_width / 1000, canvas_height / 1000);
paper.scale(scale, scale);

var size = Math.min(canvas_width, canvas_height);
paper.setDimensions(size, size);

var rects = {};
var links = [];

draw();

function draw() {
    for (var key in steps) {
        var step = steps[key];
        var rect = new joint.shapes.standard.Rectangle();
        var width = 200;
        var height = 100;
        if (step.description.length > 70) {
            width = 250;
            height = 150;
        }
        var text = joint.util.breakText(step.description, {
            width: width - 50
        });

        rect.position(step.x, step.y);
        rect.resize(width, height);

        // highlight current step
        var fill = '#2699FB';
        if (step.current) {
            fill = 'green';
        }
        rect.attr({
            body: {
                fill: fill
            },
            label: {
                text: text,
                fill: 'white',
                fontSize: 14
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
            links.push(link);
            link.addTo(graph);
        }
    }
}

function editLayout() {
    edit_button.hide();
    algorithm_button.hide();
    cancel_button.show();
    save_button.show();
    link_button.show();
    paper.setInteractivity(true);
}

function cancelLayout() {
    cancel_button.hide();
    save_button.hide();
    link_button.hide();
    link_dropdown.hide();
    algorithm_dropdown.hide();
    loading_icon.show();
    location.reload();
}

function setLayout() {
    paper.setInteractivity(false);
    save_button.hide();
    cancel_button.hide();
    link_button.hide();
    link_dropdown.hide();
    algorithm_dropdown.hide();
    loading_icon.show();
    for (var key in steps) {
        var new_step = steps[key];
        var position = rects[key].get('position');
        new_step.x = position.x;
        new_step.y = position.y;
        steps[key] = new_step;
    }
    var new_steps = JSON.stringify(steps);

    var form = $("#form");

    var field = $('<input></input>');

    field.attr("type", "hidden");
    field.attr("name", "steps");
    field.attr("value", new_steps);

    form.append(field);

    form.submit();
}

function setRouter(type) {
    links.forEach(function (link) {
        link.router(type);
    });
}

function changeAlgorithm(algorithm) {
    var form = $("#form");
    form.attr("method", "get");

    var field = $('<input></input>');

    field.attr("type", "hidden");
    field.attr("name", "algorithm");
    field.attr("value", algorithm);

    form.append(field);

    form.submit();
}
