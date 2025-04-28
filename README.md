TITLE: Implementation of Code Generation Phase of Compiler

AIM:
Write a program to implement code generation for a given grammar using Python

Theory:
Code Generation:

After syntax analysis and semantic checking, code generation produces target code from the decorated abstract syntax tree (AST).

The generated code can be intermediate code (like LLVM IR) or final target code (assembly, machine code).

Registers and Descriptors:

Register Descriptor: Tracks what value is currently in each register (initially empty).

Address Descriptor: Tracks where (register or memory) the current value of a variable is stored.

Example:

For three-address code x := y + z, code generated:

MOV y, R0

ADD z, R0

MOV R0, x

Code Generation Algorithm:

For each statement a := b op c:

1.Use getreg() to find a register L for storing the result.

2.If b is not in L, generate MOV b, L.

3.Generate op c, L.

4.Update address descriptors to show a is now in L.

5.Free registers holding b and c if they are no longer needed.
