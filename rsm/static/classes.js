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

    // Collapse
    document.querySelectorAll(".hr > .hr-collapse-zone > .hr-collapse").forEach(collapse => {
	collapse.addEventListener("click", function () {
            const hr = this.parentElement.parentElement;
	    if (hr.classList.contains("hr-labeled")) {
		const label = hr.querySelectorAll(".hr-content-zone > .hr-label");
		const rest = hr.querySelectorAll(".hr-content-zone > :not(.hr-label)");
		const icon = hr.querySelector(".hr-collapse-zone > .hr-collapse > .icon-wrapper");
		if (!hr.classList.contains("hr-collapsed")) {
		    hr.classList.add("hr-collapsed");
		    rest.forEach(el => { el.classList.add("hide"); });
		    icon.classList.remove("collapse");
		    icon.classList.add("uncollapse");
		    icon.innerHTML = `
                    <svg width="14" height="8" viewBox="0 0 14 8" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                      <path d="M1 1L7 7L13 1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    `;
		} else {
		    hr.classList.remove("hr-collapsed");
		    rest.forEach(el => { el.classList.remove("hide"); });
		    icon.classList.remove("uncollapse");
		    icon.classList.add("collapse");
		    icon.innerHTML = `
                    <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                      <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    `;
		};
	    };
	});
    });

    // Set height of offset handrails' borders
    document.querySelectorAll('.hr.hr-offset > .hr-border-zone > .hr-border-rect').forEach(border => {
	const siblings = Array.from(border.parentElement.parentElement.children);
	const content = siblings.find(sibling => sibling.classList.contains("hr-content-zone"));
	if (content) {
	    border.style.height = `${content.offsetHeight}px`;
	}
    });

    // Minimap
    const items = document.querySelectorAll('ul.contents li.item');
    const num_items = items.length;
    items.forEach((item, idx) => {
	item.addEventListener('mouseenter', () => {
	    let percent = (idx + 1) / num_items * 100;
            document.getElementById("stop-follow-mouse-1").setAttribute("offset", `${percent}%`);
	    document.getElementById("stop-follow-mouse-2").setAttribute("offset", `${percent}%`);
	});
    });

}
