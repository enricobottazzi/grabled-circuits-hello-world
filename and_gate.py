from random import randint, shuffle

def main():
    # Perform circuit garbling

    # Define the truth table for the AND gate
    # u | v | w
    # 0 | 0 | 0
    # 0 | 1 | 0
    # 1 | 0 | 0
    # 1 | 1 | 1

    # represent u0 and u1 with 256 bits random values 
    ku0 = randint(0, 100000)
    ku1 = randint(0, 100000)

    # represent v0 and v1 with 256 bits random values
    kv0 = randint(0, 100000)
    kv1 = randint(0, 100000)

    # represent w0 and w1 with 256 bits random values
    kw0 = randint(0, 100000)
    kw1 = randint(0, 100000)

    # build the garbed truth table 
    # u   | v  | w
    # ku0 | kv0| kw0
    # ku0 | kv1| kw0
    # ku1 | kv0| kw0
    # ku1 | kv1| kw1

    row_0 = [ku0, kv0, kw0]
    row_1 = [ku0, kv1, kw0]
    row_2 = [ku1, kv0, kw0]
    row_3 = [ku1, kv1, kw1]
    garbled_table = [row_0, row_1, row_2, row_3]

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
    # Pass the garbled inputs (ku0, kv1) to the evaluator
    garbled_inputs = (ku0, kv1)

    def dummy_decrypt(value, key):
        return value - key
    
    # Given the double encrypted w column and the garbled inputs.
    # The evaluator is able to compute the output key of the circuit without learning anything about the inputs or the output
    decrypted_w_col = []
    for i in range(4):
        decrypted_w_col.append(dummy_decrypt(dummy_decrypt(double_encrypted_w_col[i], garbled_inputs[1]), garbled_inputs[0]))
    
    # The user receives the decrypted w column and can decrypt the output
    for i in range(4):
        if decrypted_w_col[i] == kw1:
            print("The output of the circuit is 1")
            break
        if decrypted_w_col[i] == kw0:
            print("The output of the circuit is 0")
            break
    


main()

    

