loadTooltips = function() {
    $("a.reference").tooltipster({
        theme: 'tooltipster-shadow',
        functionInit: function(instance, helper) {
            target = $(helper.origin).attr("href");

            // make sure to escape any '.' in the id, otherwise jquery will think we are
            // trying to select a class instead!
            target = target.replaceAll(".", "\\.");
            target = target.replaceAll(":", "\\:");
            tag = $(target).prop('tagName');
            classes = $(target)[0].classList;
            content = "";

            if (tag == "P") {
                content = $(target).html();
                content = `<div>${content}</div>`;
            } else if (tag == "SPAN") {
                content = $(target).parent().html();
	    } else if (tag == "DT") {
		content = $(target).next().html();
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
		console.log("tooltip target with unknown tag");
	    }

            instance.content($(content));
        }
    });
    MathJax.typeset();
}
