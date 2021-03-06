"""proof_env.py

Definition of Proof environments.

"""

import re

from docutils import nodes
from docutils.statemachine import StringList
from sphinx.addnodes import pending_xref
from sphinx.util.docutils import SphinxDirective
from sphinx.roles import XRefRole
from sphinx.transforms import SphinxTransform

from thm_env import AutoNumberTheoremLike, theorem_like

from util import Targetable, LabeledDirective, NodeClassDirective, GoalDirective, parse_keywords
from misc import claim_start

INDENT_SIZE = 3


# -- Keywords ------------------------------------------------------------

class keyword(nodes.Inline, nodes.TextElement):
    pass


def keyword_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    return [keyword(rawtext, text)], []


# -- Nodes --------------------------------------------------------------

class _within_proof_env(nodes.Element):
    def __init__(self, _proof_env, *args, **kwargs):
        self._proof_env = _proof_env
        super().__init__(*args, **kwargs)

    @property
    def proof_env(self):
        return self._proof_env

    @proof_env.setter
    def proof_env(self, env):
        self._proof_env = env
        for c in self.children:
            c.proof_env = env


class proof_env(nodes.Element): pass
class proof(_within_proof_env): pass
class step_list(nodes.Sequential, _within_proof_env): pass
class statement(_within_proof_env): pass
class statement_proof(_within_proof_env): pass


class step(_within_proof_env, Targetable):
    def __init__(self, data, number=None, label=None, *args, **kwargs):
        super().__init__(data, *args, **kwargs)
        self.goal_for_substeps = None
        self.number = number
        self.label = label
        if self.label is not None:
            self['ids'] = [label]

    def has_statement_proof(self):
        for c in self.children:
            if isinstance(c, statement_proof):
                return True
        return False

    def default_link_text(self):
        return f'step {self.number}'


# -- Directives ------------------------------------------------------------

class StepDirective(SphinxDirective, LabeledDirective, GoalDirective):
    has_content = True
    optional_arguments = 1
    option_spec = {'label': str}

    def run(self):
        node = step(
            data='\n'.join(self.content),
            number=f'{self.arguments[0]}' if self.arguments else '',
        )
        self.state.nested_parse(self.content, self.content_offset, node)
        if self.label:
            node['ids'].append(self.label)
        self.find_goal(node)
        return [node]


class StatementDirective(NodeClassDirective):
    nodeclass = statement


class StatementProofDirective(NodeClassDirective):
    nodeclass = statement_proof


class ProofDirective(NodeClassDirective):
    nodeclass = proof


# -- Proof environment directive -------------------------------------------------------

def split_steps(content, indent=''):
    assert content.startswith(indent + ':step:'), 'Step list must start with :step:'
    steps = []
    lines = content.splitlines(keepends=True)

    # take the line, including the indentation, but not the ':step:'
    step = lines[0][:len(indent)] + lines[0][len(indent)+6:]

    # From the second line on, all lines have the right amount of indent PLUS an extra 6
    # whitespace characters that account for the ':step:' of the first line. We need to
    # get rid of those 6 characters so that the indentation lines up.
    within_statement = True
    for line in lines[1:]:
        assert (not line.strip()) or line.startswith(indent), 'Wrong indentation'

        if line.startswith(indent + ':step:'):
            steps.append(step)
            within_statement = True
            step = line[:len(indent)] + line[len(indent)+6:]
        else:
            if not line.strip():
                step += line
            elif line.lstrip().startswith(':'):
                within_statement = False
                step += line
            elif within_statement:
                step += line[:len(indent)] + line[len(indent)+7:]
            else:
                step += line
    steps.append(step)

    return steps


def process_step_list(source, indent='', number=''):
    new_content = ''
    for idx, step in enumerate(split_steps(source, indent)):
        next_number = f'{number}.{idx+1}' if number else f'{idx+1}'
        new_content += process_step(step, indent, number=f'{next_number}')
    return new_content


def process_step(source, indent, number=''):
    # -- Process :prev: tags ---------------------------------------------------
    # :prev: is the same as :prev:`<1>`
    source = re.sub(r':prev:([^`])', ':prev:`<1>' + r'`\1', source)
    # :prevn:`foo` is the same as :prev:`foo <n>`
    source = re.sub(r':prev([0-9]+):`(.+?)`', r':prev:`\2 <\1>`', source)
    # :prevn: is the same as :prev:`<n>`
    source = re.sub(r':prev([0-9]+):([^`])', r':prev:`<\1>`' + r'\2', source)

    # -- Find label ------------------------------------------------------------
    label = ''
    if source[len(indent)] == '`':
        for idx, char in enumerate(source[len(indent)+1:]):
            if char == '`':
                # keep the label in between the backticks
                label = source[len(indent)+1:len(indent)+1+idx]
                # delete the label AND THE BACKTICKS (and the space right after the
                # closing backtick), but keep the indent
                source = source[:len(indent)] + source[len(indent)+3+idx:]
                break
        else:
            raise ValueError('Malformed step label')

    lines = source.split('\n')
    next_indent = indent + ' ' * INDENT_SIZE

    # -- Find statement --------------------------------------------------------
    # The statement is everything up to the first line that starts with one more
    # level of indentation and either :p: or :step:.
    statement = []
    for idx, line in enumerate(lines):
        if (line.startswith(next_indent + ':p:')
            or line.startswith(next_indent + ':step:')):
            rest = lines[idx:]
            break
        statement.append(line)
    else:
        # The entire step is just the statement, there is no 'rest'
        rest = []

    # This fixes a bug where, if the statement is multi-line and is the last thing in
    # the entire proof environment, the final indentation would be wrong and it would
    # turn into a definition list (because definition lists only use indentation as mark
    # up...)
    if statement[-1] != '':
       statement.append('')

    # -- Add statement to new content--------------------------------------------
    new_content = indent + '.. step::'
    if number:
        new_content += f' {number}'
    new_content += '\n'
    indent += INDENT_SIZE * ' '
    if label:
        new_content += indent + f':label: {label}\n'
    new_content += '\n'
    new_content += indent + '.. statement::'
    new_content += '\n\n'
    indent += INDENT_SIZE * ' '
    new_content += '\n'.join([indent + l for l in statement])
    new_content += '\n'
    indent = indent[:-INDENT_SIZE]

    # -- Process the rest ------------------------------------------------------
    # There are three possibilities for the rest. i) it is empty, ii) it consists of a
    # single chunk that starts with :p:, or iii) it consists of a list of :step:.

    # i) empty, do nothing
    if not '\n'.join(rest).strip():
        pass

    # ii) there is a proof starting with :p:
    elif rest[0].strip().startswith(':p:'):
        # get rid of ':p: ' -- note the trailing space
        rest[0] = rest[0][:len(indent)] + rest[0][len(indent)+4:]
        new_content += indent + '.. statement-proof::\n\n'
        new_content += '\n'.join([indent + l for l in rest])
        new_content += '\n'

    # iii) there is a proof that is a list of steps
    else:
        new_content += indent + '.. statement-proof::\n\n'
        processed = process_step_list('\n'.join(rest), indent, number)
        processed = [indent + l for l in processed.splitlines(keepends=True)]
        new_content += ''.join(processed)

    return new_content


class ProofEnvironmentDirective(SphinxDirective):
    has_content = True

    def run(self):
        old_content = '\n'.join(self.content).strip()
        assert old_content[:6] == ':step:', 'A proof must start with :step:'

        # self.content has zero indentation, even though visually it is indented.
        new_content = process_step_list(old_content, indent='')

        # The last step added an unnecessary return, remove it.
        new_content = new_content[:-1]
        new_content = parse_keywords(new_content)

        self.content = StringList(
            new_content.split('\n'),
            parent=self.content.parent, parent_offset=self.content_offset
        )

        proof_node = proof_env('\n'.join(self.content))
        self.state.nested_parse(self.content, self.content_offset, proof_node)
        for child in proof_node.children:
            child.proof_env = proof_node

        return [proof_node]


# -- Transforms ----------------------------------------------------------------------------

class AutoNumberProofs(SphinxTransform):
    # always run after numbering theorems
    default_priority = AutoNumberTheoremLike.default_priority + 1

    def apply(self, **kwargs):
        for node in self.document.traverse(lambda n: isinstance(n, proof_env) or isinstance(n, step)):
            if isinstance(node, proof_env):
                idx = node.parent.children.index(node)
                prev = node.parent.children[idx-1]

                if isinstance(prev, theorem_like):
                    node.label = f'{prev.label}-pf'
                    node['ids'].append(node.label)
                else:
                    node.label = 'orphan'
                    node['classes'].append('orphan')

            elif isinstance(node, step):
                label = node.proof_env.label
                if label != 'orphan':
                    newid = f'{label}-{node.number}'
                    node['ids'].append(newid)
                    node.register_as_target(self.env)


class SetTheoremLikeGoals(SphinxTransform):
    # always run after proofs have been linked to their theorems
    default_priority = AutoNumberProofs.default_priority + 1

    def apply(self, **kwargs):
        for node in self.document.traverse(lambda n: isinstance(n, claim_start)):
            if node.goal_set_by is not None:
                label = f'{node.goal_set_by.label}-goal'
                node['ids'].append(label)


class ResolvePendingStepRefs(SphinxTransform):
    # from https://www.sphinx-doc.org/en/master/extdev/appapi.html:
    # 700 - 799: Post processing. Deadline to modify text and referencing.
    default_priority = 799

    def apply(self, **kwargs):
        for node in self.document.traverse(pending_step_xref):
            # :prev:`title <target>`
            title, target = node.astext(), node['reftarget']
            if title == target:
                if target.startswith('<') and target.endswith('>'):
                    # only a target was provided
                    title = ''
                    target = int(target[1:-1])
                else:
                    # only a title was provided, default to the step immediately before
                    target = 1
            else:
                # when both are provided, the '<' and '>' are not part of the target
                target = int(target)

            parent_step = node.parent
            while not isinstance(parent_step, step):
                parent_step = parent_step.parent
            step_list = parent_step.parent
            index = step_list.children.index(parent_step)
            assert target <= index, f'Trying to reference {target} steps behind {index}'
            prev_step = step_list[index - target]
            target = prev_step['ids'][0]

            if not title:
                title = prev_step.default_link_text()

            refnode = nodes.reference(title, title, internal=True)
            refnode['refid'] = target
            node.replace_self(refnode)


# -- Step reference nodes ------------------------------------------------------------
# See also the ResolvePendingStepRefs transform
class pending_step_xref(pending_xref): pass
class PrevRole(XRefRole):
    nodeclass = pending_step_xref
prev_role = PrevRole()


# -- Setup ---------------------------------------------------------------------------

def setup(app):
    app.add_transform(AutoNumberProofs)
    app.add_transform(ResolvePendingStepRefs)
    app.add_transform(SetTheoremLikeGoals)

    app.add_node(proof_env)
    app.add_node(step)
    app.add_node(statement)
    app.add_node(statement_proof)
    app.add_node(keyword)

    app.add_directive('proof', ProofEnvironmentDirective)
    app.add_directive('step', StepDirective)
    app.add_directive('statement', StatementDirective)
    app.add_directive('statement-proof', StatementProofDirective)

    app.add_role('kw', keyword_role)
    app.add_role('prev', prev_role)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
