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
	collapse.addEventListener("click", collapseHandrail);
    });
    document.querySelectorAll(".hr.step > .hr-menu-zone > .hr-menu > .hr-menu-item.collapse-subproof:not(.disabled)").forEach(collapse => {
	collapse.addEventListener("click", collapseHandrail);
    });

    // Set height of offset handrails' borders
    const resizeObserver = new ResizeObserver(updateHeight);
    document.querySelectorAll('.hr.hr-offset > .hr-content-zone').forEach(el => resizeObserver.observe(el));

    // Contents
    const items = document.querySelectorAll('ul.contents li.item');
    const num_items = items.length;
    items.forEach((item, idx) => {
	item.addEventListener('mouseenter', () => {
	    let percent = (idx + 1) / num_items * 100;
            document.getElementById("stop-follow-mouse-1").setAttribute("offset", `${percent}%`);
	    document.getElementById("stop-follow-mouse-2").setAttribute("offset", `${percent}%`);
	});
    });

    // Floating minimap
    window.addEventListener('scroll', () => {
	const toc_mm = document.querySelector(".toc-wrapper > .minimap");
	const float_mm = document.querySelector(".float-minimap-wrapper > .minimap");
	if (withinView(toc_mm, false)) {
	    float_mm.classList.add("hide");
	} else {
	    float_mm.classList.remove("hide");
	};
    });

    window.addEventListener('scroll', () => {
	const mm = document.querySelector(".float-minimap-wrapper > .minimap");
	if (mm.classList.contains("hide")) return;

	const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
	const sections = document.querySelectorAll('section');
	const lastInViewport = Array.from(sections).findLast(sec => withinView(sec, true));
	const circle = document.querySelector(`#mm-${lastInViewport?.id}`)

	let percent;
	if (circle && mm) {
	    const circle_rect = circle.getBoundingClientRect();
	    const mm_rect = mm.getBoundingClientRect();
	    percent = (circle_rect.bottom - mm_rect.top + 12) / mm.offsetHeight * 100;
	} else {
	    percent = 0;
	};
	document.getElementById("stop-follow-scroll-1").setAttribute("offset", `${percent}%`);
	document.getElementById("stop-follow-scroll-2").setAttribute("offset", `${percent}%`);
    });

}

function withinView(el, top = true) {
    const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
    const rect = el.getBoundingClientRect();
    if (top) {
	return rect.top < viewportHeight / 2 && rect.bottom > 0;
    } else {
	return rect.top < viewportHeight && rect.bottom > 0;
    };
}

function updateHeight(entries) {
    for (const entry of entries) {
	const hr = entry.target.parentElement;
	const elementsToResize = hr.querySelectorAll('& > .hr-border-zone, & > .hr-spacer-zone');
	elementsToResize.forEach(el => { el.style.height = `${entry.contentRect.height}px`; })
    }
};


function collapseHandrail() {
    const hr = this.closest(".hr");
    let rest;
    if (hr.classList.contains("hr-labeled")) {
	rest = hr.querySelectorAll("& > .hr-content-zone > :not(.hr-label)");
    } else if (hr.classList.contains("step")) {
	rest = hr.querySelectorAll("& > .hr-content-zone > :not(.statement)");
    } else {
	rest = Array.from(hr.parentElement.children).filter(el => {return el !== hr});
    };

    if (!hr.classList.contains("hr-collapsed")) {
	hr.classList.add("hr-collapsed");
	rest.forEach(el => { el.classList.add("hide"); });
	const icon = hr.querySelector("& .icon-wrapper.collapse");
	if (icon) {
	    icon.classList.remove("collapse");
	    icon.classList.add("uncollapse");
	    icon.innerHTML = `
                    <svg width="14" height="8" viewBox="0 0 14 8" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                      <path d="M1 1L7 7L13 1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    `;
	    const menu_item = icon.nextElementSibling;
	    if (menu_item && menu_item.classList.contains("hr-menu-item-text")) { menu_item.textContent = "Expand" };
	}
    } else {
	hr.classList.remove("hr-collapsed");
	rest.forEach(el => { el.classList.remove("hide"); });
	const icon = hr.querySelector("& .icon-wrapper.uncollapse");
	if (icon) {
	    icon.classList.remove("uncollapse");
	    icon.classList.add("collapse");
	    icon.innerHTML = `
                    <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                      <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    `;
	    const menu_item = icon.nextElementSibling;
	    if (menu_item && menu_item.classList.contains("hr-menu-item-text")) { menu_item.textContent = "Collapse" };
	}
    };

}
