// onload.js
//
// Function to run when the entire document finishes loading
//

import { loadMathJax, loadPseudocode } from '/static/libraries.js';
import { createTooltips } from '/static/tooltips.js';
import { setupClassInteractions } from '/static/classes.js';

export function onload() {
    console.log("hi");
    loadMathJax().then(() => {
        console.log('MathJax loaded!');
        loadPseudocode().then(() => {
	    console.log('pseudocode loaded!');
	    const elements = $("pre.pseudocode");
	    if (elements.length) {
                pseudocode.renderElement(elements[0], {lineNumber: true, noEnd: true});
	    }
	    createTooltips();
        }).catch((err) => {
	    console.error('Loading pseudocode FAILED!');
	    console.error(err);
        })
        setupClassInteractions();
    }).catch((err) => {
        console.error('Loading MathJax FAILED!');
        console.error(err);
    })
}
