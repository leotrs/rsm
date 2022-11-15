// tooltips.js
//
// Setup tooltips on <a> tags.
//

export function createTooltips() {
    $("a.reference").tooltipster({
        theme: 'tooltipster-shadow',
        functionInit: function(instance, helper) {
            let target = $(helper.origin).attr("href");

            // make sure to escape any '.' in the id, otherwise jquery will think we are
            // trying to select a class instead!
            target = target.replaceAll(".", "\\.");
            target = target.replaceAll(":", "\\:");
            let tag = $(target).prop('tagName');
            let classes = $(target)[0].classList;
            let content = "";

            if (tag == "P") {
                content = $(target).html();
                content = `<div>${content}</div>`;
            } else if (tag == "SPAN") {
                content = $(target).parent().html();
	    } else if (tag == "DT") {
		content = $(target).next().html();
            } else if (tag == "FIGURE") {
                content = $(target).html();
            } else if (tag == "SECTION") {
                let clone = $(target).clone();
                clone.children().slice(2).remove();
                clone.children().each(function () {$(this).css('transform', 'scale(0.75)');});
                clone.css('transform', 'scale(0.75)');
                content = clone.html();
            } else if (tag == "DIV") {
                switch(true) {
                case classes.contains("step"):
                    content = $(target).children(".statement").html();
                    break;
		case classes.contains("theorem"):
		    content = $(target).find(".theorem-contents").html();
		    break;
                case classes.contains("math"):
                    content = $(target).html();
                    break;
                case true:
                    console.log("tooltip target DIV with unknown class")
                }
            } else {
		console.log(`tooltip target with unknown tag ${tag}`);
	    }

            instance.content($(content));
        }
    });
    if (typeof MathJax !== 'undefined' && 'typeset' in MathJax) {
        MathJax.typeset();
    }
    else {
        console.log('updated but did not find Mathjax.typeset');
    }
}

// Modified from https://stackoverflow.com/a/53744331
export function loadMathJax() {
    let loadmjx = function() {
        const script = document.createElement('script');
        script.type = "text/javascript";
        script.id = "MathJax-script";
        script.src = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js";
        document.body.appendChild(script);

        return new Promise((res, rej) => {
	    script.onload = res;
	    script.onerror = rej;
        });
    };

    loadmjx()
        .then(() => {
	    console.log('Script loaded!');
	    createTooltips();
        })
        .catch(() => {
	    console.error('Script loading failed! Handle this error');
        });
}
