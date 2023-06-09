# Description
A Python library for encoding Quantum Rule Based Systems (QRBS). Calculate the probabilities associated with forward chaining rule bases using quantum gates and circuits. `qrbsgen` supports rule bases involving `AND`, `OR`, and `NOT` operators. 

Made possible with an integration to `Qiskit` SDK. 

## Prerequisites

Familiarity with `Qiskit` is useful - check it out [here](https://qiskit.org/) .

The specification and definition of the QRBS implemented here can be found in the following [publication](https://www.neasqc.eu/wp-content/uploads/2021/05/NEASQC_D6.2_QRBS-Models-Architecture-and-Formal-Specification-V1.5-Final.pdf) by V. Bonillo et al. and the wider NExt ApplicationS of Quantum Computing, or [NEASQC](https://www.neasqc.eu/about-the-project/) project. 

## Installation

`pip install qrbsgen` 

## Usage 

See the usage steps below to get started:

```
import qrbsgen as q

# Instantiate your QuantumRuleBasedSystem
rule_system = q.QuantumRuleBasedSystem()

# Define and add rules using appropriate syntax (see below)
rule = "IF ((A) AND ((B) OR (C))) THEN (R)"
rule_terms, qubits = rule_system.add_rules([rule])

# Perform quantum circuit
rule_system.evaluate_rules(rule_terms, qubits)
```
Given the two-level system representing true or false outcomes, the probability of the above test will be a probabilistic result like so:

```
* Added rule IF ((A) AND ((B) OR (C))) THEN (R)
* Probability of outcome:  0.378 
```

## Syntax 

Currently, QRBS is limited to supporting inputs of two-level systems, as can be easily mapped to a two-level quantum system, or qubit.

This means clauses, or variables, must be defined as `true` or `false`, `one` or `zero`. You can also define variables as `A` and `NOT A` for simplicity.

Please define rules and clauses as follows:

- Start with an `"IF"` statement in capital letters.
- Follow with the rule antecedent and antecedent clauses, where `"IS"` is typed in capital letters where relevant e.g.: `A IS one`, `A IS true`, `(A is true)`, `A` or `(A)`.
- Follow with a `"THEN"` statement in capital letters.
- Finish with the rule consequet, where `"IS"` is typed in capital letters where relevant e.g.: `B IS one`, `B IS true`, `(B is true)`, `B` or `(B)`. 

```
"IF ((A IS true) AND ((B IS true) OR (C IS true))) THEN (R IS true)"
```

## Examples

Examples can be found [here](https://github.com/kvcmarshall/qrbsgen/tree/main/examples).

## Information
Created by Kate Marshall of IBM.  
Although this is copyright of IBM, this is not an official or unofficial IBM product.
Please get in touch for any further information: kate.marshall@ibm.com.

Inspiration for this repo and rule parsing techniques came from the [Simpful](https://github.com/aresio/simpful) fuzzy reasoning API.
