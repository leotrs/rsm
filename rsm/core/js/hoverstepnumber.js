$(document).ready(function() {
    $(".step").hover(function() {
        tomb = $(this).children(".tombstone-container");
        tomb.removeClass("hide");
    }, function() {
        tomb = $(this).children(".tombstone-container");
        if (tomb.hasClass("no-ellipsis")) {
            tomb.addClass("hide");
        } else {
            tomb.removeClass("hide");
        };
    });

    $(".step-container").click(function() {
        toggle_step(this);
    });

    $(".proof-env").mouseleave(function () {
	console.log('leave');
	$(this).find(".options-container").addClass("hide");
    });

});

function toggle_proof(btn) {
    console.log(btn);
    div = $(btn).closest(".proof-env").children(".proof-container");
    if (div.hasClass("hide")) {
        div.removeClass("hide");
    } else {
        div.addClass("hide");
    };
};

function toggle_step(step) {
    div = $(step).children(".statement-proof");
    tomb = $(step).siblings(".tombstone-container");
    if (div.hasClass("hide")) {
	div.removeClass("hide");
        tomb.addClass("no-ellipsis");
        tomb.addClass("hide");
    } else {
        div.addClass("hide");
        tomb.removeClass("no-ellipsis");
        tomb.removeClass("hide");
    };
};

function toggle_all_steps(option) {
    proof_container = $(option).closest(".proof-env").find(".proof-container");
    steps = $(proof_container).children(".step").children(".step-container");
    steps.each(function() {toggle_step($(this))});
};

function show_all_options(btn) {
    options = $(btn).children(".options-container");
    options.each(function() {
        $(this).removeClass("hide");
    });
};

function copy_link(opt) {
    id = $(opt).closest(".proof-env").parent().attr("id");
    current_url = location.protocol+'//'+location.host+location.pathname;
    target_url = current_url + "#" + id;
    navigator.clipboard.writeText(target_url).then(function () {
	console.log('foo')
    });
};

function show_tree(opt) {
    proof = $(opt).closest(".proof-env").parent();
    parent = $(proof).parent();
    console.log(parent);
    parents = [];

    while (!parent.hasClass("body")) {
	parents.push(parent);
	parent = parent.parent();
    };
    console.log(parents);
};
