// onload.js
//
// Function to run when the entire document finishes loading
//

export function onload(path = "/static/") {
    import(path + 'libraries.js').then((libs) => {
        libs.loadMathJax().then(() => {
            console.log('MathJax loaded!');
            libs.loadPseudocode().then(() => {
	        console.log('pseudocode loaded!');
	        const elements = $("pre.pseudocode");
	        if (elements.length) {
                    pseudocode.renderElement(elements[0], {lineNumber: true, noEnd: true});
	        }
	        import(path + 'tooltips.js').then((tips) => {
                    tips.createTooltips();
                })
            }).catch((err) => {
	        console.error('Loading pseudocode FAILED!');
	        console.error(err);
            })
            import(path + 'classes.js').then((cls) => {
                cls.setupClassInteractions();
            })
        }).catch((err) => {
	    console.error('Loading MathJax FAILED!');
	    console.error(err);
        })
    })
}
