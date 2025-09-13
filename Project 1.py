def is_formula(s):
    """
    Check if the string s is a well-formed formula in propositional logic.
    Atoms are single uppercase letters.
    Connectives: ¬, ∧, ∨, →, ↔
    Every non-atomic formula must be enclosed in parentheses.
    """
    s = s.replace(" ", "")  # Remove all spaces
    n = len(s)

    if n == 0:
        return False
    # Atom case
    if n == 1:
        return s.isalpha() and s.isupper()

    # Check if enclosed in parentheses
    if s[0] == '(' and s[-1] == ')':
        inner = s[1:-1]
        # Unary formula: (¬φ)
        if inner.startswith('¬'):
            return is_formula(inner[1:])
        # Binary formula: (φ ◦ ψ)
        else:
            count = 0  # Parenthesis count
            for i in range(len(inner)):
                if inner[i] == '(':
                    count += 1
                elif inner[i] == ')':
                    count -= 1
                # When count is 0, we are at top level
                if count == 0:
                    # Check if current character is a binary connective
                    if i + 1 < len(inner) and inner[i] in ['∧', '∨', '→', '↔']:
                        left_part = inner[:i]
                        right_part = inner[i + 1:]
                        return is_formula(left_part) and is_formula(right_part)
            # If no connective found at top level, invalid
            return False
    else:
        return False


# Test the given expressions
expressions = [
    "((¬(A ∨ B)) ∧ C)",
    "(A ∧ B) ∨ C",
    "A → (B ∧ C)",
    "((A ↔ B) → (¬A))",
    "((¬A) → B ∨ C)",
    "(((C ∨ B ∧ A) ↔ D)",
    "((∨A) ∧ (¬B))",
    "(A ∧ (B ∧ C)))"
]

for expr in expressions:
    result = is_formula(expr)
    print(f"Expression: {expr} -> {'Valid' if result else 'Invalid'}")