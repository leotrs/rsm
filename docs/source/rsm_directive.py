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


def setup(app):
    app.add_directive("rsm", RSMDirective)
    app.add_node(rsm_example, html=(visit_rsm_example_node, depart_rsm_example_node))
    app.add_node(rsm_body, html=(visit_rsm_body_node, depart_rsm_body_node))
