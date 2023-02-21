## Smol: a small Lexer/Parser/AST

*Smol* is a tiny lexer and parser over a language with the same name that only supports assignments and basic arithmetic operations.

Its grammar is presented in a flavor of EBNF in `smol.ebnf`:

```ebnf
(* Toy language grammar consisting only of assignment *)
Program = {Assignment};
Assignment = Identifier, '=', Expression, ';';
Expression = Unary, {[ "/" | "+" | "-" | "*" ], Expression};
Unary = Identifier | Number;
Identifier = Character, { Character | Digit };
Number = [ "-" ], Digit, { Digit } ;
Character = "A" | "B" | "C" | "D" | "E" | "F" | "G"
            | "H" | "I" | "J" | "K" | "L" | "M" | "N"
            | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
            | "V" | "W" | "X" | "Y" | "Z" | "a" | "b"
            | "c" | "d" | "e" | "f" | "g" | "h" | "i"
            | "j" | "k" | "l" | "m" | "n" | "o" | "p"
            | "q" | "r" | "s" | "t" | "u" | "v" | "w"
            | "x" | "y" | "z" ;
Digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
```

The next steps to produce something would be to implement a `visitor` that uses the meta-created methods `accept_<node_type>` defined in each `Node`.


The lex/parse passes can be triggered on the example `example.smol` using the command `python -m smol example.smol`

```
// First test!
a = 1200;
c = x * y + b;
d = x * y + c * n;
```
