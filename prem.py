def code_generation(statements):
    code = []
    reg = "R0"
    for stmt in statements:
        left, right = map(str.strip, stmt.split("="))
        for op, instr in [("+", "ADD"), ("-", "SUB"), ("*", "MUL"), ("/", "DIV")]:
            if op in right:
                a, b = map(str.strip, right.split(op))
                code += [f"MOV {reg}, {a}", f"{instr} {reg}, {b}", f"MOV {left}, {reg}"]
                break
        else:
            code += [f"MOV {reg}, {right}", f"MOV {left}, {reg}"]
    return code

n = int(input("Enter the number of statements:\n"))
statements = [input().strip() for _ in range(n)]
for line in code_generation(statements):
    print(line)