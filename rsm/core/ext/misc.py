"""misc.py

Miscellaneous, but important, additions to RSM.

"""

import re
from os import path, listdir
from docutils import nodes
from sphinx.util.fileutil import copy_asset_file


def substitute_turnstile(app, docname, source):
    # This function changes any occurrence of the string "|-" to the turnstile symbol
    # ⊢. This substitution is made just after the source file is read, before any RST
    # formatting has happened. In theory, we could achieve this using RST's substitution
    # syntax, but the syntax involves the use of vertical bars and therefore does not
    # work with our string "|-".

    # Per official documentation of the source-read event, the source argument contains
    # a single element that must be changed in place.
    source[0] = re.sub(r'\|-', '⊢', source[0])

    # # The following substitution *could* be made using RST's substitution syntax, but it
    # # would create a lot of substitution-reference nodes which slows down the build. It
    # # is much faster and cleaner to just do it now.
    # source[0] = re.sub(r'\bQED\b', '■', source[0])


def mark_up_claims(app, docname, source):
    # This puts dummy role nodes :claim-start:`x` and :claim-end:`x` surrounding a claim
    # (which always starts with a turnstile symbol). It would be easier to just mark-up
    # the turstile symbol itself, as :claim-start:`⊢`, but ReST roles cannot be nested
    # and the turstile will eventually be surrounded by a keyword role. Note the claim
    # roles are not empty, they contain an 'x' (this could in fact be any other
    # non-whitespace character). This is done because the double consecutive backticks
    # have a different meaning in ReST and a purely empty role won't be parsed
    # correctly.
    #
    # This MUST execute after substituting |- to ⊢.
    #
    idx = 0
    inside_claim = False
    while idx < len(source[0]):
        if inside_claim:
            if source[0][idx] == '.':
                # if we have found a period '.' inside of a claim, it can be one of two
                # cases: we are at the end of the claim, or at the start of a
                # directive. If it is a math directive, include it in the claim. Note
                # there may be periods inside the directive, we need to ignore all of
                # them.
                if source[0][idx:].startswith('.. math::'):
                    print('Claim includes a .. math:: directive... we need to fix this...')
                    inside_claim = False

                else:           # end of claim
                    source[0] = source[0][:idx+1] + ' :claim-end:`x`' + source[0][idx+1:]
                    inside_claim = False
            elif source[0][idx] == '⊢':
                context = source[0][idx-50:idx+50]
                raise ValueError('Cannot have claim within claim: \n"' + context + '"')
            idx += 1

        else:
            if source[0][idx] == '⊢':
                inside_claim = True
                source[0] = source[0][:idx] + ':claim-start:`x` ' + source[0][idx:]

                # After adding the dummy role in the previous line, the characters after
                # the current index are ":claim-start:`x`⊢" (note the turnstile symbol
                # at the end). Thus, if we keep on naively, eventually we will hit said
                # turnstile and think that we have found a turnstile within a
                # turnstile. To avoid this, we simply skip that entire sub-string by
                # jumping ahead the necessary amount of characters.
                idx += len(':claim-start:`x` ⊢')
            else:
                idx += 1


class claim_start(nodes.TextElement): pass
class claim_end(nodes.TextElement): pass
num_claims = 0


def claim_start_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    global num_claims
    start = claim_start('', '')
    start['ids'] = [f'claim-{num_claims}']
    num_claims += 1
    return [start], []


def claim_end_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    return [claim_end('', '')], []


def setup(app):
    app.connect('source-read', substitute_turnstile)
    app.connect('source-read', mark_up_claims)
    app.add_role('claim-start', claim_start_role)
    app.add_role('claim-end', claim_end_role)
    app.add_node(claim_start)
    app.add_node(claim_end)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
