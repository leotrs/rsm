// onload.js
//
// Function to run when the entire document finishes loading
//

export async function onload(path = "/static/") {
    try {
        const libs = await import(`${path}libraries.js`);

        // MathJax
        await libs.loadMathJax();
        console.log("MathJax loaded!");

        // Pseudocode
        try {
            await libs.loadPseudocode();
            console.log("Pseudocode loaded!");

            const elements = document.querySelectorAll("pre.pseudocode");
            if (elements.length) {
                pseudocode.renderElement(elements[0], {
                    lineNumber: true,
                    noEnd: true,
                });
            }
        } catch (err) {
            console.error("Loading pseudocode FAILED!", err);
        }

        // Tooltipster
        try {
            const tips = await import(`${path}tooltips.js`);
            tips.createTooltips();
        } catch (err) {
            console.error("Loading tooltips FAILED!", err);
        }

        // Classes
        try {
            const hr = await import(`${path}handrails.js`);
            hr.setup();
        } catch (err) {
            console.error("Loading handrails.js FAILED!", err);
        }

        // Keyboard interaction
        try {
            const kbd = await import(`${path}keyboard.js`);
            kbd.setup();
        } catch (err) {
            console.error("Loading keyboard.js FAILED!", err);
        }

        // Minimap
        try {
            const mm = await import(`${path}minimap.js`);
            mm.setup();
        } catch (err) {
            console.error("Loading minimap.js FAILED!", err);
        }
    } catch (err) {
        console.error("An error occurred during initialization:", err);
    }
}
