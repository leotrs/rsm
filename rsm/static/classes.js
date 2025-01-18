// classes.js
//
// Basic user interactions.
//

export function setupClassInteractions() {
    // Handrail menus
    document.querySelectorAll(".hr > .hr-menu-zone > .hr-menu").forEach(menu => {
	menu.addEventListener("mouseleave", function () {
	    this.parentElement.style.display = "none";
	});
    });
    document.querySelectorAll(".hr > .hr-border-zone > .hr-border-dots").forEach(dots => {
	dots.addEventListener("click", function () {
            const siblings = Array.from(this.parentElement.parentElement.children);
            const target = siblings.find(sibling => sibling.classList.contains("hr-menu-zone"));
            if (target) {
		target.style.display = "block";
            }
	});
    });

    // Set height of offset handrails' borders
    document.querySelectorAll('.hr.hr-offset > .hr-border-zone > .hr-border-rect').forEach(border => {
	console.log(border);
	const siblings = Array.from(border.parentElement.parentElement.children);
	const content = siblings.find(sibling => sibling.classList.contains("hr-content-zone"));
	if (content) {
	    border.style.height = `${content.offsetHeight}px`;
	}
    });

}
