"""writer.py

Custom HTML writer for RSM.

"""

from sphinx.writers.html5 import HTML5Translator


class RSMTranslator(HTML5Translator):

    def visit_title(self, node):
        self.body.append('<div class="handrail handrail--offset">')
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
        self.body.append('''
        <div class="handrail__btn-container">
            <div class="handrail__btn handrail__btn--relative" onclick="show_all_options(this)">
                <span>⋮</span>
                <div class="options hide" onmouseleave="hide_all_options(this)">
                    <span class="option" onclick="toggle_all_steps(this)">steps</span>
                    <span class="option" onclick="copy_link(this)">link</span>
                    <span class="option" onclick="show_tree(this)">tree</span>
                    <span class="option">source</span>
                </div>
            </div>
            <div class="handrail__btn" onclick="toggle_proof(this)"><span>▹</span></div>
        </div>
        <div class="proof-env__title">
            <strong>Proof.</strong>
        </div>
        <div class="proof-container">
        ''')

    def depart_proof_env(self, node):
        self.body.append('</div>')  # proof-container
        self.body.append('<div class="tombstone"></div>')
        self.body.append('</div>')  # proof-env

    def visit_step(self, node):
        self.body.append(self.starttag(node, 'div', CLASS=('step with-tombstone')))

    def depart_step(self, node):
        self.body.append('<div class="tombstone hide"></div>')
        self.body.append('</div>')   # step

    def visit_keyword(self, node):
        self.body.append(self.starttag(node, 'span', CLASS=('keyword')))

    def depart_keyword(self, node):
        self.body.append('</span>')

    def visit_statement(self, node):
        self.body.append(self.starttag(node, 'div', CLASS=('statement-container')))
        self.body.append(f'<div class="step__number">({node.parent.number})</div>')
        self.body.append(self.starttag(node, 'div', CLASS=('statement')))

    def depart_statement(self, node):
        self.body.append('</div>')   # statement
        self.body.append('</div>')   # statement-container

    def visit_statement_proof(self, node):
        self.body.append(self.starttag(node, 'div', CLASS='statement__proof handrail handrail--hug'))

    def depart_statement_proof(self, node):
        self.body.append('</div>')



def setup(app):
    app.registry.add_translator('html', RSMTranslator)
