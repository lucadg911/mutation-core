REGEX_OPERATORS = [[r"--(\b\w+\b)", r"++\1"],
                   [r"(\b\w+\b)--", r"\1++"],
                   [r"CAmount\s+(\w+)\s*=\s*([0-9]+)", r"CAmount \1 = \2 + 1"],
                   [r"CAmount\s+(\w+)\s*=\s*([0-9]+)", r"CAmount \1 = \2 - 1"],
                   ["continue", "break"],
                   ["std::all_of", "std::any_of"],
                   ["std::any_of", "std::all_of"],
                   ["std::min", "std::max"],
                   ["std::max", "std::min"],
                   ["std::begin", "std::end"],
                   ["std::end", "std::begin"],
                   ["true", "false"],
                   ["false", "true"],
                   [" / ", " * "],
                   [" > ", " < "],
                   [" > ", " >= "],
                   [" < ", " > "],
                   [" >= ", " <= "],
                   [" >= ", " > "],
                   [" > ", " <= "],
                   [r"&&", "||"],
                   [r"'\|\|'", "&&"],
                   [" == ", " != "],
                   [" != ", " == "],
                   [r" - ", " + "],
                   [r"\+", "-"],
                   [" < ", " <= "],
                   [" < ", " > "],
                   [" < ", " >= "],
                   [r".*\berase\(.+", r""],
                   [r"^.*if\s*\(.*\)\s*continue;.*$", r""],
                   [r"^.*if\s*\(.*\)\s*return;.*$", r""],
                   [r"^.*if\s*\(.*\)\s*return.*;.*$", r""],
                   [r"^(.*for\s*\(.*;.*;.*\)\s*\{.*)$", r"\1break;"],
                   [r"^(.*while\s*\(.*\)\s*\{.*)$", r"\1break;"],
                   [r"\b(int64_t|uint64_t|int32_t|uint32_t)\s+(\w+)\s*=\s*(.*?);$", r"\1 \2 = (\3) + 1;"],
                   [r"\b(int64_t|uint64_t|int32_t|uint32_t)\s+(\w+)\s*=\s*(.*?);$", r"\1 \2 = (\3) - 1;"],
                   ["return 0", "return 1"],
                   [r"static\s+const\s+size_t\s+(\w+)\s*=\s*([^;]+);", r"static const size_t \1 = \2 - 1;"],
                   [r"static\s+const\s+size_t\s+(\w+)\s*=\s*([^;]+);", r"static const size_t \1 = \2 + 1;"],
                   [r"int64_t\s+(\w+)\s*=\s*([0-9]+)", r"int64_t \1 = \2 + 1"],
                   [r"int64_t\s+(\w+)\s*=\s*([0-9]+)", r"int64_t \1 = \2 - 1"],
                   [r"bool\s+([a-zA-Z_]\w*)\s*\{\s*([^{}]*)\s*\}", r"bool \1{false}"],
                   [r"bool\s+([a-zA-Z_]\w*)\s*\{\s*([^{}]*)\s*\}", r"bool \1{true}"],
                   [r"bool\s+([a-zA-Z_]\w*)\s*=\s*([^;]+)", r"bool \1 = true"],
                   [r"bool\s+([a-zA-Z_]\w*)\s*=\s*([^;]+)", r"bool \1 = false"],
                   [r"NodeClock::now\(\)", r"NodeClock::now() - 1"],
                   [r"NodeClock::now\(\)", r"NodeClock::now() + 1"],
                  ]

# Might be caught by fuzz tests
SECURITY_OPERATORS = [
    ["==", "="],
    [r" - ", " + "],
    [r"\s\+\s", "-"],
    [r"std::array<\s*([\w:]+)\s*,\s*(\d+)\s*>", r"std::array<\1, \2 - 2>"],
    [r"\b(if|while)\s*\(([^)]+)\)", r"\1 (!(\2))"],
    # [r"^\s*[a-zA-Z_][a-zA-Z_0-9]*\s*=\s*[^=][^;]*;\s*$", ""],
    [r"\b((?:int16_t|uint16_t|int32_t|uint32_t|int64_t|uint64_t|int)\s*[\(\{])([^\)\}]*)[\)\}]", "\2"],
    [r"ignore\((\s*(\d+)\s*)\)", r"ignore(\2 + 100)"],
    [r"(\w+)\[(\w+)\]", r"\1[\2 + 5]"],
    [r"if\s*\(\s*(.*?)\s*\|\|\s*(.*?)\s*\)", r"if(\2||\1)"],
    [r"GetSelectionAmount\(\)", r"GetSelectionAmount() + std::numeric_limits<CAmount>::max() - 1"],
    [r"resetBlock\(\);", ""],
    [r"\w+(\.|->)GetMedianTimePast\(\)", "std::numeric_limits<int64_t>::max()"],
    ["break", ""]
]

FUNCTIONAL_TEST_OPERATORS = [
    [r"self\.nodes\s*=\s*(\d+)", r"self.nodes = \1 - 1"],
    [r"^.*\b(?!assert\w*)\w+\s*\(.*\).*$", r""]
]
