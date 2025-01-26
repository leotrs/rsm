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
            const cls = await import(`${path}classes.js`);
            cls.setup();
        } catch (err) {
            console.error("Loading classes.js FAILED!", err);
        }

        // Keyboard shortcuts
        try {
            const kbd = await import(`${path}shortcuts.js`);
            kbd.setup();
        } catch (err) {
            console.error("Loading shortcuts.js FAILED!", err);
        }
    } catch (err) {
        console.error("An error occurred during initialization:", err);
    }
}
