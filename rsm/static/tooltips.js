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
            } else if (tag == "LI") {
                content = $(target).html();
                content = `<div>${content}</div>`;
	    } else if (tag == "SPAN" && classes.contains("math")) {
                content = $(target).html();
                content = `<div>${content}</div>`;
	    } else if (tag == "SPAN") {
                content = $(target).parent().html();
                content = `<div>${content}</div>`;
	    } else if (tag == "DT") {
		content = $(target).next().html();
            } else if (tag == "FIGURE") {
                content = $(target).html();
            } else if (tag == "TABLE") {
		content = $(target)[0].outerHTML;
            } else if (tag == "SECTION") {
                let clone = $(target).clone();
                clone.children().slice(2).remove();
                // clone.children().each(function () {$(this).css('transform', 'scale(0.75)');});
                // clone.children().each(function () {$(this).attr('onload', 'this.width*=0.25;');});
                // clone.css('transform', 'scale(0.75)');
                // clone.attr('onload', 'this.width*=0.25;')
                clone.css('font-size', '0.7rem');
                content = clone.html();
            } else if (tag == "A") {
		content = $(target).parent().html();
                content = `<div>${content}</div>`;
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
                case classes.contains("mathblock"):
                    content = $(target).find('mjx-container').clone();
                    break;
		case classes.contains("algorithm"):
                    content = $(target).html();
                    break;
                case true:
                    console.log("tooltip target DIV with unknown class: ")
                    console.log(classes);
                }
            } else {
		console.log(`tooltip target with unknown tag ${tag}`);
	    }

            instance.content($(content));
        }
    });

    $("a.note__link").tooltipster({
        theme: 'tooltipster-shadow',
        functionInit: function(instance, helper) {
            let content = $(helper.origin).parent().next().html();
            content = `<div>${content}</div>`;
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
