// tooltips.js
//
// Setup tooltips on <a> tags.
//

export function createTooltips() {
    $(".manuscriptwrapper a.reference").tooltipster({
        theme: ['tooltipster-shadow', 'tooltipster-shadow-rsm'],
	minWidth: 100,
	maxWidth: 500,
        functionInit: function(instance, helper) {
            let target = $(helper.origin).attr("href");

            // make sure to escape any '.' in the id, otherwise jquery will think we are
            // trying to select a class instead!
            target = target.replaceAll(".", "\\.");
            target = target.replaceAll(":", "\\:");
            let tag = $(target).prop('tagName');
            let classes = $(target)[0].classList;
	    let clone = undefined;
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
                clone = $(target).clone();
                clone.children().slice(2).remove();
		clone.find(".hr-collapse-zone").remove();
		clone.find(".hr-menu-zone").remove();
		clone.find(".hr-border-zone").remove();
		clone.find(".hr-info-zone").remove();
                clone.css('font-size', '0.7rem');
                content = clone.html();
            } else if (tag == "A") {
		content = $(target).parent().html();
                content = `<div>${content}</div>`;
            } else if (tag == "DIV") {
                switch(true) {
                case classes.contains("step"):
		    clone = $(target).find(".statement").clone();
		    clone.find(".hr-collapse-zone").remove();
		    clone.find(".hr-menu-zone").remove();
		    clone.find(".hr-border-zone").remove();
		    clone.find(".hr-info-zone").remove();
                    clone.css('font-size', '0.7rem');
                    content = clone.html();
                    break;
		case ["theorem", "proposition"].some(cls => classes.contains(cls)):
		    clone = $(target).clone();
		    clone.find(".hr-collapse-zone").remove();
		    clone.find(".hr-menu-zone").remove();
		    clone.find(".hr-border-zone").remove();
		    clone.find(".hr-info-zone").remove();
                    clone.css('font-size', '0.7rem');
                    content = clone.html();
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
		case classes.contains("paragraph"):
		    clone = $(target).clone();
		    clone.find(".hr-collapse-zone").remove();
		    clone.find(".hr-menu-zone").remove();
		    clone.find(".hr-border-zone").remove();
		    clone.find(".hr-info-zone").remove();
		    content = $(clone).html();
		    break;
                case true:
                    console.log("tooltip target DIV with unknown class: ")
                    console.log(classes);
                }
            } else {
		console.log(`tooltip target with unknown tag ${tag}`);
	    }

	    content = `<div class="manuscriptwrapper">${content}</div>`
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
