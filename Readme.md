Base-Ä
======
Base-Ä is an encoding scheme for converting between small integers and names which would be appropriate for 260-foot tall, giant-monster-punching robots. The resulting names are fun, memorable, and readily distinguished over the phone. Appropriate uses might include giving names to machines in a cluster, or spicing up your error codes.

A few examples:

|Index |Name                 |
|------|---------------------|
| 0    |Atomic Absolute      |
| 1    |Ballistic Vigor      |
| 2    |Boxer Thunder        |
| 3    |Brawler Saber        |
| 4    |Challenger Redeemer  |
| 5    |Cherno Omega         |
| 6    |Cobra Judas          |
| 7    |Coyote Gauntlet      |

This repository offers bi-directional dependency-free Base-Ä converters in several popular languages (ES6, Java, C, K, Python), each with a robust test fixture.

The Encoding
============
Integers are represented with a pair of space-separated strings, each drawn from a table of 64 "fragments". As a result, a single Base-Ä name can distinguish 4096 distinct integers. See `words-first.txt` and `words-second.txt` for a complete listing of the fragment tables.

Since Base-Ä may be applied to small ranges of integers, a direct enumeration of the fragments is aesthetically undesirable; sequential names should not look overly similar to one another. To solve this problem, we employ a very simple reversible hash: multiply by 123 and then use the residue modulo 4096 to obtain an index. The least-significant 6 bits of the index and the next 6 most significant bits of the index are used to draw fragments from the tables of second and first halves, respectively.

For reversing the encoding, we perform case-insensitive lookups in each fragment table and calculate the corresponding index. Multiplying the index by 7859 and taking the residue modulo 4096 reproduces the original input.

Implementations
===============

ES6
---
Routines are stored in a global object `BaseÄ` with the following members:

- `max`: the maximum integer encodable in Base-Ä. (4095)
- `valid(x)`: returns true if `x` can be decoded in Base-Ä.
- `encode(x)`: convert an integer into a Base-Ä string. Throws an `Error` if `x` is less than 0 or greater than `max`.
- `decode(x)`: convert a Base-Ä string into an integer. Throws an `Error` if `x` is not `valid`.

Test script:

	> node es6/test.js

Java
----
Routines are housed in a static class `BaseÄ` with the following public members:

- `public static final int MAX`: the maximum integer encodable in Base-Ä. (4095)
- `public static boolean valid(String x)`: returns true if `x` can be decoded in Base-Ä.
- `public static String encode(int x)`: convert an integer into a Base-Ä string. Throws `IllegalArgumentException` if `x` is less than 0 or greater than `MAX`.
- `public static int decode(String x)`: convert a Base-Ä string into an integer. Throws `IllegalArgumentException` if `x` is not `valid`.

Test script:
	
	> cd java
	> javac *.java
	> java -ea Test

C
---
Routines are declared in a single header file `basea.h`. The following definitions are exported:

- `BASE_A_MAX`: the maximum integer encodable in Base-Ä. (4095)
- `BASE_A_LENGTH`: an appropriate buffer size, including null-terminator, for a formatted Base-Ä name. (64)
- `int base_a_valid(const char* x)`: returns 1 if `x` can be decoded in Base-Ä.
- `int base_a_encode(int x, char* result)`: write the name corresponding to `x` into `result` with a null-terminator. Returns 1 if `x` is less than 0 or greater than `BASE_A_MAX`.
- `int base_a_decode(const char* x, int* result)`: write the integer corresponding to `x` into `result`. Returns 1 if `x` is not `valid`.

Test script:

	> cd c
	> chmod +x test.c
	> ./test.c

K7
---
Routines are installed in the `.baseA` directory of the K-tree. The following names are meant for external use:

- `m`: the maximum int encodable in Base-Ä. (4095)
- `valid[x]`: returns 1 if `x` can be decoded in Base-Ä.
- `encode[x]`: convert an int `x` into a Base-Ä string. Invalid indices result in a string null value.
- `decode[x]`: convert a string `x` into an int. Invalid strings result in `0N`.

`valid`, `encode` and `decode` may be applied to vectors as well as single arguments.

Test script:

	> cd k7
	> k7 test.k
	
Python
---
The `basea` package has a `basea` object instance which has the computed encoding values.  This object exposes an API composed of:

- `basea.max`: the maximum int encodable in Base-Ä. (4095)
- `basea.valid(name)`: returns `True` if `name` can be decoded in Base-Ä.
- `basea.encode(number)`: convert an int/float/Decimal `number` into a Base-Ä string. Invalid values result in a `ValueError`.
- `basea.decode(name)`: convert a string `name` into an int. Invalid strings result in a `ValueError`.

A small example:

    from basea import basea
    
    basea.encode(4)  # Challenger Redeemer
    basea.decode('Challenger Redeemer')  # 4

Test script:

    > cd python
    > pip install nose nose-ignore-docstring coverage
    > nose

License (MIT)
=============
Copyright 2018 John Earnest, with apologies to Guillermo del Toro.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
