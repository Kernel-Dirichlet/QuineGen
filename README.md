# QuineGen

This repository is geared towards collecting examples of quines which remain quines upon copying the source code N times. 
Additionally, there will be a toolkit to generate N-line quines from templates in a variety of languages. Over time, this
repository will showcase how different quine strategies can be used to create programs which not only output themselves,
but continue to do so no matter how many times the original source is copied. 

While not the primary goal, polyglot quines (programs which are valid in more than one language and themselves are quines simultaneously), and
palipolygot quines (polyglot quines which are also palindromes) would be interesting examples to consider.  

## Background on Quines:

A quine is a self-replicating program - a computer program that takes no input and produces a copy of its own source code as its only output. The term"quine" was coined by Douglas Hofstadter, inspired by the philosopher Willard Van Orman Quine, who made significant contributions to logic and philosophy. 


## Popular Quine Related GitHub Repositories:

1. **The 128 quine relay**: This is the largest quine relay project where 128 languages are used to generate a quine from the original source language, but with the logic encoded and passed through each of the 128 languages. The quines do not have the restriction that they must remain valid if copied N-times   - GitHub Link: [128 quine relay](https://github.com/mame/quine-relay)

2. **Snake over Quine**: This repository showcases a unique C++ quine which serves as a background for the popular game "Snake"
    - GitHub Link: [Snake over C++ quine](https://github.com/taylorconor/quinesnake)  

## Significance of Generating Quines of Arbitrary Length:

Generating quines of arbitrary length highlights significant properties of a given language. Here's why it's significant:

- **Algorithmic Complexity**: Writing a quine that can self-replicate is already a non-trivial task. However, as the length of the quine increases, the complexity of the algorithm required to generate *should* increases significantly. Even though this is true, the examples in the repository often feature "standard" quine techniques which are sufficient to generate programs of arbitrary length. 

- **Demonstration of Language Features**: Writing quines of varying lengths can demonstrate the capabilities and limitations of different programming languages. Some languages may offer features or constraints that make quine generation easier or more challenging, which can serve as a proxy for gauging its metaprogramming capabilities and limitations.

- **LLM "testing"**: As of the current date (3/11/2024), many LLMs, even GPT4, struggle generating quines in even simpler scripting languages, let alone with the additional constraints of polyquines and arbitrary length quines.  

- **Because we can**: Much like many code golf related tasks, we simply can push the boundaries of what is possible. 

## Contributing to this Repository 

- This repository will have automated tests that will check all quines submitted to the quines template are indeed quines and remain so when copied N-times. For now, interesting examples (quines that feature techniques not pulled from StackExchange or elsewhere) take priority. 
