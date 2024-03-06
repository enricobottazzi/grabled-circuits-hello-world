from random import randint, shuffle

def main():
    # Perform circuit garbling

    # Define AND gate truth table
    u = [0, 0, 1, 1]
    v = [0, 1, 0, 1]
    w = [0, 0, 0, 1]

    # represent u0 and u1 with 256 bits random values 
    ku0 = randint(0, 100000)
    ku1 = randint(0, 100000)

    # represent v0 and v1 with 256 bits random values
    kv0 = randint(0, 100000)
    kv1 = randint(0, 100000)

    # represent w0 and w1 with 256 bits random values
    kw0 = randint(0, 100000)
    kw1 = randint(0, 100000)

    # represent the garbled truth table
    u_garbled = [ku0, ku0, ku1, ku1]
    v_garbled = [kv0, kv1, kv0, kv1]
    w_garbled = [kw0, kw0, kw0, kw1]

    # the garbed table has 3 columns and 4 rows
    # u   | v  | w
    # ku0 | kv0| kw0
    # ku0 | kv1| kw0
    # ku1 | kv0| kw0
    # ku1 | kv1| kw1

    garbled_table = []
    for i in range(4):
        garbled_table.append([u_garbled[i], v_garbled[i], w_garbled[i]])

    # Randomly permute the rows of the garbled table
    shuffle(garbled_table)

    def dummy_encrypt(value, key):
        return value + key

    # Double encrypt the table w
    double_encrypted_w_col = []
    for i in range(4):
        double_encrypted_w = dummy_encrypt(dummy_encrypt(garbled_table[i][2], garbled_table[i][1]), garbled_table[i][0])
        double_encrypted_w_col.append(double_encrypted_w)

    # Pass the double encrypted w column to the evaluator

    # Now I want the evaluator to evaluate the circuit on the input tuple (0, 1)
    # Pass the tuple (ku0, kv1) to the evaluator
    evaluator_input = (ku0, kv1)

    def dummy_decrypt(value, key):
        return value - key

    # The evaluator will use the evaluator input to decrypt the double encrypted w column
    decrypted_w = []
    for i in range(4):
        decrypted_w.append(dummy_decrypt(dummy_decrypt(double_encrypted_w_col[i], evaluator_input[1]), evaluator_input[0]))
    
    # output translation table
    output_translation_table = {kw0: 0, kw1: 1}

    # expected output
    excepted_output = 0

    for i in range(4):
        if decrypted_w[i] in output_translation_table:
            print(f"Expected: {excepted_output}")
            print(f"Actual: {output_translation_table[decrypted_w[i]]}")
            assert output_translation_table[decrypted_w[i]] == excepted_output


main()

    

