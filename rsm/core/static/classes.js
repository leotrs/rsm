// classes.js
//
// This file contains code pertaining to adding and removing classes of DOM elements in
// response to user interaction.
//

$(document).ready(function() {

    $(".step").hover(function() {
        tomb = $(this).children(".tombstone");
        tomb.removeClass("hide");
    }, function() {
        tomb = $(this).children(".tombstone");
        if (tomb.hasClass("with-ellipsis")) {
            tomb.removeClass("hide");
        } else {
            tomb.addClass("hide");
        };
    });

    $(".handrail").mouseleave(function () {
	$(this).find(".options").addClass("hide");
    });

    $(".handrail__btn-menu").click(function() {
        options = $(this).children(".options");
        options.each(function() {
            $(this).removeClass("hide");
        });
    });

    $(".handrail__btn-toggle").click(function() {
        block = $(this).closest(".handrail");
        div = block.children(".handrail__collapsible");
        if (div.length == 0) {
            div = block.siblings(".handrail__collapsible");
        };
        tomb = $(div).siblings(".tombstone");

        if (div.hasClass("children-hidden")) {
	    block.removeClass("collapsed");
	    tomb.removeClass("with-ellipsis");
            div.addClass("children-hidden");
            div.children().each(function() {
                if (! $(this).hasClass("do-not-hide")) {
                    $(this).removeClass("hide");
                }
            });
        } else {
	    block.addClass("collapsed");
            tomb.addClass("with-ellipsis");
            div.addClass("children-hidden");
            div.children().each(function() {
                if (! $(this).hasClass("do-not-hide")) {
                    $(this).addClass("hide");
                }
            });
        };

    });

    $(".option__steps").click(function() {
        proof_container = $(this).closest(".proof").find(".proof-container");
        steps = $(proof_container).children(".step");
        steps.each(function() {toggle_step($(this))});
    });

    $(".option__link").click(function() {
        id = $(this).closest(".proof").attr("id");
        current_url = location.protocol+'//'+location.host+location.pathname;
        target_url = current_url + "#" + id;
        navigator.clipboard.writeText(target_url).then(function () {
	    console.log('foo')
        });
    });

    $(".option__tree").click(function() {
        proof = $(opt).closest(".proof");
        parent = $(proof).parent();
        console.log(parent);
        parents = [];

        while (!parent.hasClass("body")) {
	    parents.push(parent);
	    parent = parent.parent();
        };
        console.log(parents);
    });

    $(".option__goal").on("click", function(){
	step = $(this).closest(".step");
	parent = $(step).parent();

	if (parent.hasClass("proof-container")) {
	    thm_id = $(parent).parent().attr("id").slice(0, -3);
	    element = `#${thm_id}`
	} else {
	    element = parent.closest(".step");
	};

	goal_id = $(element).attr("data-goal-for-substeps");
	$(`#${goal_id}`).addClass("hilite");

    });

    $(".option__narrow").on("click", function() {
	step = $(this).closest("div.step");
	html = $(this).html();

	if (html == "narrow") {
	    step.siblings().addClass("hide");
	    $(this).html("widen");

	    if (step.prev(".step").length > 0) {
		step.addClass("narrow-before");
	    };
	    if (step.next(".step").length > 0) {
		step.addClass("narrow-after");
	    };
	}
	else if (html == "widen"){
	    step.siblings().removeClass("hide");
	    step.removeClass("narrow-before");
	    step.removeClass("narrow-after");
	    $(this).html("narrow");
	};

    });

    $(".options").mouseleave(function() {
        options = $(this).children(".options");
        options.each(function() {
            $(this).addClass("hide");
        });
    });

});


function toggle_step(step) {
    div = $(step).children(".statement__proof");
    tomb = $(step).children(".tombstone");
    if (div.hasClass("hide")) {
	div.removeClass("hide");
        tomb.removeClass("with-ellipsis");
        tomb.addClass("hide");
    } else {
        div.addClass("hide");
        tomb.addClass("with-ellipsis");
        tomb.removeClass("hide");
    };
};
