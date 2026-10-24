# Ruby-backed bibliography helpers (bead rsm-ddx.5.6 follow-up).
#
# Uses the gems AnyStyle already installs: bibtex-ruby parses a real .bib
# (quotes, bare values, @string) into clean fields, and latex-decode turns LaTeX
# accents and symbols into plain text. rsm/bibtools.py calls this.
#
#   ruby bibtools.rb bib <path>      -> JSON [{type, key, fields}]
#   ruby bibtools.rb decode          -> clean one reference string per stdin line

require 'bibtex'
require 'latex/decode'
require 'json'

# Turn a LaTeX string into plain text: keep the content of semantic commands
# latex-decode ignores (\url, \href), decode accents and symbols, then drop any
# leftover command names and grouping braces.
def clean(s)
  s = s.to_s.dup
  s.gsub!('~', ' ')
  s.gsub!(/\\url\{([^}]*)\}/, '\1')
  s.gsub!(/\\href\{([^}]*)\}\{([^}]*)\}/, '\2 (\1)')
  s = LaTeX.decode(s)
  s.gsub!(/\\[a-zA-Z@]+\*?/, '')
  s.gsub!(/[{}]/, '')
  s.gsub!(/[[:space:]]+/, ' ')
  s.strip
end

case ARGV[0]
when 'bib'
  bib = BibTeX.open(ARGV[1])
  bib.replace_strings
  out = bib.select { |x| x.is_a?(BibTeX::Entry) }.map do |e|
    fields = {}
    e.each_pair { |k, v| fields[k.to_s] = clean(v) }
    { 'type' => e.type.to_s, 'key' => e.key.to_s, 'fields' => fields }
  end
  puts JSON.generate(out)
when 'decode'
  STDIN.each_line { |line| puts clean(line) }
end
