# Bibliography import flow

How `rsm import` turns a LaTeX file, folder, or arXiv tarball into a rendered RSM
references block. The bibliography is handled outside pandoc (pandoc drops the
`\bibitem` keys), extracted from the raw source, and spliced in.

```mermaid
flowchart TD
  subgraph RSMIFY["rsmify"]
    R["fetch arXiv tarball"]
  end
  subgraph RSMLANG["rsm-lang"]
    IN["rsm import: file / folder / archive"] --> T{"input type?"}
    T -->|archive| EX["safe-extract to temp dir<br/>traversal / symlink / size guards"]
    T -->|folder| DIR["project dir"]
    T -->|file| FILE["single-file project"]
    EX --> MAIN{"find main .tex<br/>has documentclass"}
    DIR --> MAIN
    FILE --> MAIN
    MAIN -->|one, or conventional name| RES["resolve input/include<br/>flatten body"]
    MAIN -->|ambiguous| STOP["STOP: list candidates<br/>require --main"]
    RES --> BIB{"locate bibliography"}
    BIB -->|.bib| BIBF["parse bibtex<br/>cut to cited keys"]
    BIB -->|.bbl or inline thebibliography| PAIRS["extract key + reference-text pairs"]
    BIB -->|none| NONE["no references, done"]
    PAIRS --> HASP{"AnyStyle available?"}
    HASP -->|no| V1["verbatim + warn"]
    HASP -->|yes| PARSE["AnyStyle parses each reference"]
    PARSE --> FLOOR{"clears floor?<br/>title + author or year"}
    FLOOR -->|no| V2["verbatim + warn"]
    FLOOR -->|yes| MAP["map fields + kind"]
    BIBF --> EMIT["emit RSM references block<br/>pandoc copy suppressed"]
    MAP --> EMIT
    V1 --> EMIT
    V2 --> EMIT
    EMIT --> RENDER["render each bibitem:<br/>verbatim to raw text, else author. title. venue. year<br/>+ number, anchor, backlinks"]
    RENDER --> HTML["HTML"]
  end
  R --> IN
  classDef warn fill:#ffe0f0,stroke:#cc3399,color:#16202e;
  classDef stop fill:#ffdddd,stroke:#cc3333,color:#16202e;
  class V1,V2 warn;
  class STOP stop;
```

Pink nodes emit an RSM log warning; the red node is a hard stop.

## Notes

- **Parser.** `.bib` if present, parsed as bibtex and cut to cited keys, no
  parsing step needed. Otherwise AnyStyle, run as an optional tool rsm-lang
  detects (not a pip dependency), baked into the rsmify and Studio images. With
  no parser installed (a bare CLI install), the document still converts and the
  references render verbatim, with an RSM log warning.
- **Main-file detection.** The `.tex` that declares `\documentclass`. When
  several match and one is chosen by a conventional name (`main`, `ms`,
  `paper`), that choice is logged via the RSM logger so it is not silent. When
  it is still ambiguous, `rsm import` stops and asks for `--main <file>`.
- **Degrade warnings.** Every fall back to a verbatim entry (no parser, a parse
  below the floor, or a parse failure) emits an RSM log warning naming the
  entry's citation key.
