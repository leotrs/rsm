"""writer.py

Custom HTML writer for RSM.

"""

from docutils import nodes
from sphinx.writers.html5 import HTML5Translator

from thm_env import theorem_like
from proof_env import proof_env, step
from contents import contents_title


class RSMTranslator(HTML5Translator):

    options = {
        theorem_like: ['link', 'tree'],
        proof_env: ['steps', 'link', 'tree', 'source'],
        nodes.title: ['link', 'citation'],
        nodes.caption: ['foo', 'bar'],
        contents_title: ['table', 'tree'],
        step: ['narrow', 'goal', 'link'],
        nodes.label: ['bibtex'],
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._last_section_action = None
        self._current_section = None

    def visit_title(self, node):
        self.body.append(self.starttag(
            node,
            'div',
            CLASS='header handrail handrail--offset',
        ))
        self._append_handrail_button_container(node)
        super().visit_title(node)

    def depart_title(self, node):
        super().depart_title(node)
        self.body.append('</div>\n')
        self.body.append('<div class="section-container handrail__collapsible">')

    def visit_section(self, node):
        node['classes'].append(f'level-{self.section_level+1}')

        if self._current_section is None:
            node['ids'].insert(0, 'manuscript-root')
        super().visit_section(node) # this increases self.section_level
        if self._current_section is None:
            self._current_section = [1]
            node['ids'].insert(0, 'manuscript-root')
            return

        # if self._last_section_action is 'visit', then we are opening a sub-section.
        # if self._last_section_action is None, then this is the first section, and in
        # that case we set it to 'depart' which essentially means that there are no
        # sub-sections to close
        if self._last_section_action is None:
            self._last_section_action = 'depart'

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
        classes = 'step with-tombstone handrail handrail--offset handrail--nested handrail--hug'
        classes += ' '.join(node['classes'])

        attr = {}
        if node.goal_for_substeps is not None:
            attr = {'data-goal-for-substeps': node.goal_for_substeps['ids'][0]}

        self.body.append(self.starttag(node, 'div', CLASS=classes, **attr))
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
        classes = f'stars-{node.stars} clocks-{node.clocks}'
        classes += ' '.join(node['classes'])

        attr = {}
        if node.goal_for_substeps is not None:
            attr = {'data-goal-for-substeps': node.goal_for_substeps['ids'][0]}

        self.body.append(self.starttag(node, 'div', CLASS=classes, **attr))
        self._append_handrail_button_container(node)

        if node.stars or node.clocks:
            self.body.append('<div class=handrail__icons>')
            if node.stars:
                self.body.append('<div class=handrail__icons--stars>')
                self.body.append('<i class="fas fa-star"></i>' * (node.stars-1))
                self.body.append('<i class="fas fa-star handrail__icons-last"></i>')
                self.body.append('</div>')
            if node.clocks:
                self.body.append('<div class=handrail__icons--clocks>')
                self.body.append('<i class="fas fa-clock"></i>' * (node.clocks-1))
                self.body.append('<i class="fas fa-clock handrail__icons-last"></i>')
                self.body.append('</div>')
            self.body.append('</div>')

    def depart_theorem_like(self, node):
        self.body.append('</div>')

    def visit_claim_start(self, node):
        classes = 'claim goal' if node.goal_set_by is not None else 'claim'
        self.body.append(self.starttag(node, 'span', CLASS=classes))

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

    def visit_citation(self, node):
        super().visit_citation(node)

    def visit_label(self, node):
        # closed in depart_citation()
        self.body.append('<div class="handrail handrail--offset citation__item">')
        self._append_handrail_button_container(node)
        super().visit_label(node)

    def depart_citation(self, node):
        # overridden from _html_base:HTMLTranslator to close the handrail div
        self.body.append('</dd>\n')
        self.body.append('</div>\n') # opened in visit_label()
        if not isinstance(node.next_node(descend=False, siblings=True),
                          nodes.citation):
            self.body.append('</dl>\n')
            self.in_footnote_list = False




def setup(app):
    app.registry.add_translator('html', RSMTranslator)
