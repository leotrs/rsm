// classes.js
//
// Add or remove classes of DOM elements in response to user interaction.
//

export function setupClassInteractions() {
    $(".step").hover(function() {
        let tomb = $(this).siblings(".halmos");
        tomb.removeClass("hide");
    }, function() {
        let tomb = $(this).siblings(".halmos");
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
        let options = $(this).children(".options");
        options.each(function() {
            $(this).removeClass("hide");
        });
    });

    $(".handrail__btn-toggle").click(function() {
        let block = $(this).closest(".handrail");
        let div = block.children(".handrail__collapsible");
        if (div.length == 0) {
            div = block.siblings(".handrail__collapsible");
        };
        let tomb = $(div).siblings(".halmos");

        if (div.hasClass("children-hidden")) {
	    block.removeClass("collapsed");
	    tomb.removeClass("with-ellipsis");
            div.removeClass("children-hidden");
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

    $(".proof .handrail__btn-toggle").click(function() {
        let handrail = $(this).closest('.handrail')
        let buttons = $(this).closest('.proof').find('.proof__tabs > button')
        if (handrail.hasClass("collapsed")) {
            buttons.each(function() {
                $(this).removeClass("active")
            })}
        else {
            $(buttons[0]).addClass("active")
        }
    });

    $(".proof__tabs > button").click(function() {
        if (!$(this).hasClass('active')) {
            $(this).siblings("button").each(function() {
                $(this).removeClass("active")
            })
            $(this).addClass("active")
        };

        let contents = $(this).closest('.proof').find('.proof-contents');
        let show = null;
        let hide = null;
        if ($(this).hasClass('sketch')) {
            show = contents.children('.sketch');
            hide = contents.children(':not(.sketch)');
        } else if ($(this).hasClass('full')) {
            show = contents.children(':not(.sketch)');
            hide = contents.children('.sketch');
        };
        hide.children().each(function(){
            $(this).addClass("hide")
        });
        show.children().each(function(){
            $(this).removeClass("hide")
        })
    });

    $(".option__assumptions").click(function() {
	let parents = $(this).parentsUntil("body");
	let step = $(this).closest(".handrail");
	let next_steps = $(step).nextAll();
	parents.find(".construct.assumption").addClass("hilite");
	next_steps.find(".construct.assumption").removeClass("hilite");
    });

    $(".option__steps").click(function() {
        let proof_container = $(this).closest(".proof").find(".proof-container");
        let steps = $(proof_container).children(".step");
        steps.each(function() {toggle_step($(this))});
    });

    $(".option__link").click(function() {
        let id = $(this).closest(".proof").attr("id");
        let current_url = location.protocol+'//'+location.host+location.pathname;
        let target_url = current_url + "#" + id;
        navigator.clipboard.writeText(target_url).then(function () {
	    console.log('foo')
        });
    });

    $(".option__tree").click(function() {
        let proof = $(opt).closest(".proof");
        let parent = $(proof).parent();
        let parents = [];

        while (!parent.hasClass("body")) {
	    parents.push(parent);
	    parent = parent.parent();
        };
        console.log(parents);
    });

    $(".option__goal").on("click", function(){
	let step = $(this).closest(".step");
	let parent = $(step).parent();

	if (parent.hasClass("proof-container")) {
	    let thm_id = $(parent).parent().attr("id").slice(0, -3);
	    let element = `#${thm_id}`
	} else {
	    let element = parent.closest(".step");
	};

	let goal_id = $(element).attr("data-goal-for-substeps");
	$(`#${goal_id}`).addClass("hilite");

    });

    $(".option__narrow").on("click", function() {
	let step = $(this).closest("div.step");
	let html = $(this).html();

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
        let options = $(this).children(".options");
        options.each(function() {
            $(this).addClass("hide");
        });
    });
}


function toggle_step(step) {
    let div = $(step).children(".statement__proof");
    let tomb = $(step).children(".halmos");
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
