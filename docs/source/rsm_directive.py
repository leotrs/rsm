"""
rsm_directive.py
----------------

Highlight and render RSM code blocks.

"""

from docutils import nodes
from docutils.parsers.rst import Directive

import rsm


class rsm_example(nodes.Element):
    pass


class rsm_body(nodes.Element):
    def __init__(self, body):
        super().__init__()
        self.body = body


class RSMDirective(Directive):
    has_content = True

    def run(self):
        content = "\n".join(self.content)
        n1 = nodes.literal_block(content, content)
        n1["language"] = "text"
        n1["classes"].append("rsm-example-code")
        n2 = rsm_body(rsm.render(content, handrails=True))
        rsm_node = rsm_example()
        rsm_node.append(n1)
        rsm_node.append(n2)
        return [rsm_node]


def visit_rsm_body_node(self, node):
    # strip the enclosing <body> tag
    from_idx = node.body.index(startstr := "<body>") + len(startstr)
    upto_idx = node.body.rindex(finalstr := "</body>")
    body = node.body[from_idx:upto_idx]
    body = body.replace(
        'class="manuscriptwrapper"', 'class="manuscriptwrapper embedded"'
    )
    self.body.append(body)


def depart_rsm_body_node(self, node):
    pass


def visit_rsm_example_node(self, node):
    self.body.append('<div class="rsm-example">')


def depart_rsm_example_node(self, node):
    self.body.append("</div>")


def add_rsm_static_path(app):
    parent = Path(__file__).parent
    doc_static_dir = parent / "_static"
    rsm_static_dir = parent.parent.parent / "rsm" / "static"
    app.config.html_static_path.append(str(doc_static_dir.absolute()))
    app.config.html_static_path.append(str(rsm_static_dir.absolute()))


def setup(app):
    app.connect("builder-inited", add_rsm_static_path)
    app.add_css_file("rsm.css")
    app.add_css_file("tooltipster.bundle.css")
    app.add_js_file("tooltipster.bundle.js")
    app.add_js_file(
        None,
        type="module",
        body="import { onload } from '../_static/onload.js'; window.addEventListener('load', (ev)=>{onload(true)});",
    )

    app.add_directive("rsm", RSMDirective)
    app.add_node(rsm_example, html=(visit_rsm_example_node, depart_rsm_example_node))
    app.add_node(rsm_body, html=(visit_rsm_body_node, depart_rsm_body_node))
