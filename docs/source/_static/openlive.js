// openlive.js
//
// Add a button to each rsm code block to open the code in the live edito
//

svg_icon = `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-external-link" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
  <path d="M11 7h-5a2 2 0 0 0 -2 2v9a2 2 0 0 0 2 2h9a2 2 0 0 0 2 -2v-5" />
  <line x1="10" y1="14" x2="20" y2="4" />
  <polyline points="15 4 20 4 20 9" />
</svg>`


const addbutton = () => {
    const elements = document.querySelectorAll(".rsm-example-code .highlight");
    elements.forEach((elem, index) => {
        const btn = `<button class="openlive o-tooltip--left" data-tooltip="Edit online">${svg_icon}</button>`
        elem.insertAdjacentHTML('beforeend', btn)
    })
}

window.addEventListener('load', addbutton);
