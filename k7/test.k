/ Unit Tests for the k7 Base-Ä implementation

\l baseA.k
assert: {$[x;;` 0:,:y]}

/ tests
c: 1+.baseA.m       / count
i: !c               / indices
n: .baseA.encode i  / names

assert[c~#?n;"encoding must be injective."]
assert[i~.baseA.decode n;"encoding must be bijective."]
assert[(2#,15#" ")~.baseA.encode -1 8514;"invalid encodes"]
assert[0N 0N 0N~.baseA.decode("";"Gipsy";"1 2");"invalid decodes"]
assert[1 0 0~.baseA.valid("Gipsy Danger";"Gipsy Doofus";"Goatse Danger");"validity checks failed."]

` 0:,:"all tests passed.";
.baseA.encode@!15
\\
