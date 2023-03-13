import qrbsgen.qrbs as q


def test_qrbs():
    rule_system = q.QuantumRuleBasedSystem()
    # Define and add rules
    rule = "IF ((A) AND ((B) OR (C))) THEN (R)"
    rule_terms, qubits = rule_system.add_rules([rule])
    # Perform quantum circuit
    rule_system.evaluate_rules(rule_terms, qubits)
    print("Test passed!")


if __name__ == "__main__":
    test_qrbs()
    print("Tests successful")
