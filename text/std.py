from talon import app, clip, ui
from talon.voice import Context, Key

from ..utils import text, vocab, word


def copy_bundle(_):
    bundle = ui.active_app().bundle
    clip.set(bundle)
    app.notify("Copied app bundle", body="{}".format(bundle))


ctx = Context("input")
ctx.vocab = vocab
ctx.keymap(
    {
        "say <dgndictation> [over]": text,
        # "sentence <dgndictation> [over]": sentence_text,  # Formatters.
        "comma <dgndictation> [over]": [", ", text],
        "period <dgndictation> [over]": [". ", text],
        # "more <dgndictation> [over]": [" ", text],
        "word <dgnwords>": word,
        "slap": [Key("cmd-right enter")],
        "question [mark]": "?",
        "tilde": "~",
        "(bang | exclamation point | not)": "!",
        "dollar [sign]": "$",
        "downscore": "_",
        "colon": ":",
        "(paren | left paren)": "(",
        "(rparen | are paren | right paren)": ")",
        "(brace | left brace)": "{",
        "(rbrace | are brace | right brace)": "}",
        # Square Brackets are in basic_keys.py!
        # "(square | left square)": "[",
        # "(rsquare | are square | right square)": "]",
        "(angle | left angle | less than)": "<",
        "(rangle | are angle | right angle | greater than)": ">",
        "(star | asterisk)": "*",
        "(pound | hash [sign] | octo | thorpe | number sign)": "#",
        "(percent [sign] | modulo)": "%",
        "caret": "^",
        "at sign": "@",
        "(and sign | ampersand | amper)": "&",
        "pipe": "|",
        "(dubquote | double quote)": '"',
        "triple tick": "'''",
        "triple quote": '"""',
        "swipe": [Key("right"), ", "],
        "item": ", ",
        # "space": " ",  # basic_keys.py
        "(args | arguments)": ["()", Key("left")],
        "index": ["[]", Key("left")],
        "block": [" {}", Key("left enter")],
        "empty array": "[]",
        "(empty dict | empty dictionary)": "{}",
        "plus": "+",
        "arrow": "->",
        # "call": "()",
        "indirect": "&",
        "dereference": "*",
        "assign": " = ",
        "[op] set to": " := ",
        "op (minus | subtract)": " - ",
        "op (plus | add)": " + ",
        "op (times | multiply)": " * ",
        "op divide": " / ",
        "op mod": " % ",
        "[op] (minus | subtract) equals": " -= ",
        "[op] (plus | add) equals": " += ",
        "[op] (times | multiply) equals": " *= ",
        "[op] divide equals": " /= ",
        "[op] mod equals": " %= ",
        "(op | is) greater [than]": " > ",
        "(op | is) less [than]": " < ",
        "(op | is) equal": " == ",
        "(op | is) not equal": " != ",
        "(op | is) greater [than] or equal": " >= ",
        "(op | is) less [than] or equal": " <= ",
        "(op (power | exponent) | to the power [of])": " ** ",
        "op and": " && ",
        "op or": " || ",
        "[op] (logical | bitwise) and": " & ",
        "[op] (logical | bitwise) or": " | ",
        "op pipe": " | ",
        "(op | logical | bitwise) (ex | exclusive) or": " ^ ",
        "[(op | logical | bitwise)] (left shift | shift left)": " << ",
        "[(op | logical | bitwise)] (right shift | shift right)": " >> ",
        "(op | logical | bitwise) and equals": " &= ",
        "(op | logical | bitwise) or equals": " |= ",
        "(op | logical | bitwise) (ex | exclusive) or equals": " ^= ",
        "[(op | logical | bitwise)] (left shift | shift left) equals": " <<= ",
        "[(op | logical | bitwise)] (right shift | shift right) equals": " >>= ",
        "go next window": Key("cmd-`"),
        "go last window": Key("cmd-shift-`"),
        "go next app": Key("cmd-tab"),
        "go last app": Key("cmd-shift-tab"),
        "go next tab": Key("ctrl-tab"),
        "go last tab": Key("ctrl-shift-tab"),
        "create tab": Key("cmd-t"),
        "create window": Key("cmd-n"),
        "undo": Key("cmd-z"),
        # Moved to amethyst.py
        # "next space": Key("cmd-alt-ctrl-right"),
        # "last space": Key("cmd-alt-ctrl-left"),
        "copy active bundle": copy_bundle,
    }
)
