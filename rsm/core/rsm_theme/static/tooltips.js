loadTooltips = function() {
    $("a.reference.internal").tooltipster({
        theme: 'tooltipster-shadow',
        functionInit: function(instance, helper) {
            target = $(helper.origin).attr("href");

            // make sure to escape any '.' in the id, otherwise jquery will think we are
            // trying to select a class instead!
            target = target.replaceAll(".", "\\.");
            tag = $(target).prop('tagName');
            classes = $(target)[0].classList;
            content = "";

	    console.log(target, tag, classes);

            if (tag == "P") {
                content = $(target).html();
            } else if (tag == "SPAN") {
                content = $(target).parent().html();
	    } else if (tag == "DT") {
		content = $(target).next().html();
            } else if (tag == "DIV") {
                switch(true) {
                case classes.contains("step"):
                    content = $(target).children(".statement").html();
                    break;
		case classes.contains("theorem-env"):
		    content = $(target).children(".theorem-env-container").html();
		    break;
                }
            } else {
		console.log("tooltip target with unknown tag");
	    }

            instance.content($(content));
        }
    });
    MathJax.typeset();
}
