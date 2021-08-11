"""writer.py

Custom HTML writer for RSM.

"""

from docutils import nodes
from sphinx.writers.html5 import HTML5Translator

from proof_env import proof_env, step


class RSMTranslator(HTML5Translator):

    options = {
        proof_env: ['steps', 'link', 'tree', 'source'],
        nodes.title: ['link', 'citation'],
        step: ['foo', 'bar'],
    }

    def visit_title(self, node):
        self.body.append('<div class="handrail handrail--offset">')

        self._append_handrail_button_container(node)

        super().visit_title(node)

    def depart_title(self, node):
        super().depart_title(node)
        self.body.append('</div>')

    def visit_proof_env(self, node):
        self.body.append(self.starttag(
            node,
            'div',
            CLASS=('proof with-tombstone handrail')
            )
        )

        self._append_handrail_button_container(node)

        self.body.append('''
        <div class="proof__title"><strong>Proof.</strong></div>
        <div class="proof-container handrail__collapsible">
        ''')

    def _append_handrail_button_container(self, node):
        print(type(node))
        self.body.append('''
        <div class="handrail__btn-container">
            <div class="handrail__btn handrail__btn-menu handrail__btn--relative">
                <span>⋮</span>
                <div class="options hide">
        ''')

        for opt in self.options.get(type(node), []):
            self.body.append(f'<span class="option option__{opt}">{opt}</span>')

        self.body.append('</div>')  # options
        self.body.append('</div>')  # handrail__btn-menu

        self.body.append('''
        <div class="handrail__btn handrail__btn-toggle">
            <span>▹</span>
        </div>
        ''')

        self.body.append('</div>') # handrail__btn-container

    def depart_proof_env(self, node):
        self.body.append('</div>')  # proof-container
        self.body.append('<div class="tombstone"></div>')
        self.body.append('</div>')  # proof

    def visit_step(self, node):
        self.body.append(self.starttag(
            node,
            'div',
            CLASS=('step with-tombstone handrail handrail--offset handrail--hug')
        ))
        self._append_handrail_button_container(node)

    def depart_step(self, node):
        self.body.append('<div class="tombstone hide"></div>')
        self.body.append('</div>')   # step

    def visit_keyword(self, node):
        self.body.append(self.starttag(node, 'span', CLASS=('keyword')))

    def depart_keyword(self, node):
        self.body.append('</span>')

    def visit_statement(self, node):
        self.body.append(f'<div class="step__number">({node.parent.number})</div>')
        self.body.append(self.starttag(node, 'div', CLASS=('statement')))

    def depart_statement(self, node):
        self.body.append('</div>')   # statement

    def visit_statement_proof(self, node):
        self.body.append(self.starttag(
            node,
            'div',
            CLASS='statement__proof handrail handrail--hug handrail__collapsible'
        ))

    def depart_statement_proof(self, node):
        self.body.append('</div>')

    def visit_theorem_like(self, node):
        self.body.append(self.starttag(node, 'div'))

    def depart_theorem_like(self, node):
        self.body.append('</div>')

    def visit_claim_start(self, node):
        self.body.append(self.starttag(node, 'span', CLASS=('claim')))

    def depart_claim_start(self, node):
        # the span will be closed when departing the corresponding claim_end
        pass

    def visit_claim_end(self, node):
        # the span was opened when visiting the corresponding claim_start
        pass

    def depart_claim_end(self, node):
        self.body.append('</span>')


def setup(app):
    app.registry.add_translator('html', RSMTranslator)
