"""writer.py

Custom HTML writer for RSM.

"""

from docutils import nodes
from sphinx.writers.html5 import HTML5Translator

from envs import theorem_like
from proof_env import proof_env, step
from contents import contents_title


class RSMTranslator(HTML5Translator):

    options = {
        theorem_like: ['link', 'tree'],
        proof_env: ['steps', 'link', 'tree', 'source'],
        nodes.title: ['link', 'citation'],
        nodes.caption: ['foo', 'bar'],
        contents_title: ['table', 'tree'],
        step: ['narrow', 'link'],
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._last_section_action = None
        self._current_section = None

    def visit_title(self, node):
        self.body.append('<div class="handrail handrail--offset handrail--hug">')
        self._append_handrail_button_container(node)
        super().visit_title(node)

    def depart_title(self, node):
        super().depart_title(node)
        self.body.append('</div>')

    def visit_section(self, node):
        node['classes'].append(f'level-{self.section_level+1}')

        if self._current_section is None:
            node['ids'].insert(0, 'manuscript-root')

        # NOTE: this call increases self.section_level by 1
        super().visit_section(node)

        if self._current_section is None:
            self._current_section = [1]
            node['ids'].insert(0, 'manuscript-root')
            return

        section_title = node.children[0]
        is_numbered = not section_title.astext().startswith(':no-num:')
        if is_numbered:
            if self._last_section_action == 'visit':
                self._current_section.append(1)
            elif self._last_section_action == 'depart':
                if self._current_section:
                    self._current_section[-1] += 1

            section_number = nodes.Text(
                '.'.join(str(i) for i in self._current_section)
                + ' '
            )
            section_title.insert(0, section_number)
        else:
            text = section_title.pop().astext()
            section_title.append(nodes.Text(text[8:]))

        self._last_section_action = 'visit'

    def depart_section(self, node):
        section_title = node.children[0]
        is_numbered = not section_title.astext().startswith(':no-num:')
        if is_numbered:
            if self._last_section_action == 'depart' and self._current_section:
               self._current_section.pop()

        super().depart_section(node)
        self._last_section_action = 'depart'

    def visit_proof_env(self, node):
        self.body.append(self.starttag(
            node,
            'div',
            CLASS=('proof with-tombstone handrail handrail--offset')
            )
        )

        self._append_handrail_button_container(node)

        self.body.append('''
        <div class="proof__title"><strong>Proof.</strong></div>
        <div class="proof-container handrail__collapsible">
        ''')

    def _append_handrail_button_container(self, node):
        self.body.append('''
        <div class="handrail__btn-container">
            <div class="handrail__btn handrail__btn-menu handrail__btn--relative">
                <span>⋮</span>
                <div class="options hide">
        ''')

        options = self.options.get(type(node), [])
        if not options:
            for cls in self.options:
                if isinstance(node, cls):
                    options = self.options[cls]
                    break
        for opt in options:
            self.body.append(f'<span class="option option__{opt}">{opt}</span>')

        self.body.append('</div>')  # options
        self.body.append('</div>')  # handrail__btn-menu

        self.body.append('''
        <div class="handrail__btn handrail__btn-toggle">
            <span>〉</span>
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
            CLASS=('step with-tombstone handrail handrail--offset handrail--nested handrail--hug')
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
        self.body.append(self.starttag(node, 'div', CLASS='statement'))

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
        self.body.append(self.starttag(
            node,
            'div',
            CLASS=f'stars-{node.stars} clocks-{node.clocks}',
        ))
        self._append_handrail_button_container(node)

        if node.stars or node.clocks:
            self.body.append('<div class=handrail__icons>')
            if node.stars:
                self.body.append('<div class=handrail__icons--stars>')
                self.body.append('<i class="fas fa-star"></i>' * node.stars)
                self.body.append('</div>')
            if node.clocks:
                self.body.append('<div class=handrail__icons--clocks>')
                self.body.append('<i class="fas fa-clock"></i>' * node.clocks)
                self.body.append('</div>')
            self.body.append('</div>')

    def depart_theorem_like(self, node):
        self.body.append('</div>')

    def visit_claim_start(self, node):
        self.body.append(self.starttag(node, 'span', CLASS='claim'))

    def depart_claim_start(self, node):
        # the span will be closed when departing the corresponding claim_end
        pass

    def visit_claim_end(self, node):
        # the span was opened when visiting the corresponding claim_start
        pass

    def depart_claim_end(self, node):
        self.body.append('</span>')

    def visit_caption(self, node):
        if isinstance(node.parent, nodes.figure):
            self.body.append(self.starttag(
                node,
                'figcaption',
                CLASS='handrail handrail--offset handrail--hug'
            ))
        self._append_handrail_button_container(node)
        self.body.append(self.starttag(node, 'p', ''))
        self.add_fignumber(node.parent)




def setup(app):
    app.registry.add_translator('html', RSMTranslator)
