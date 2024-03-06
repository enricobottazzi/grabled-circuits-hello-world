from random import randint, shuffle

def main():
    # Define the circuit by mixing a set of gates
    # Define a gate #1 AND that takes two external inputs and returns one internal output
    # Define a gate #2 AND that takes one external input and one internal input from the #1 gate and returns one output
    # Define a gate #3 OR that takes one external input and one internal input from the #1 gate and returns one output
    # Setup: randomize the truth table for each gate

    # Gate #1 AND
    # b | c | e
    # 0 | 0 | 0
    # 0 | 1 | 0
    # 1 | 0 | 0
    # 1 | 1 | 1

    kb0 = randint(0, 100000)
    kb1 = randint(0, 100000)
    kc0 = randint(0, 100000)
    kc1 = randint(0, 100000)
    ke0 = randint(0, 100000)
    ke1 = randint(0, 100000)

    # Garbled table for gate #1
    # b   | c  | e
    # kb0 | kc0| ke0
    # kb0 | kc1| ke0
    # kb1 | kc0| ke0
    # kb1 | kc1| ke1

    garbled_table_1 = [[kb0, kc0, ke0], [kb0, kc1, ke0], [kb1, kc0, ke0], [kb1, kc1, ke1]]

    # Gate #2 AND
    # a | e | f
    # 0 | 0 | 0
    # 0 | 1 | 0
    # 1 | 0 | 0
    # 1 | 1 | 1

    ka0 = randint(0, 100000)
    ka1 = randint(0, 100000)
    kf0 = randint(0, 100000)
    kf1 = randint(0, 100000)

    # Garbled table for gate #2
    # a   | e  | f
    # ka0 | ke0| kf0
    # ka0 | ke1| kf0
    # ka1 | ke0| kf0
    # ka1 | ke1| kf1

    garbled_table_2 = [[ka0, ke0, kf0], [ka0, ke1, kf0], [ka1, ke0, kf0], [ka1, ke1, kf1]]

    # Gate #3 OR
    # e | d | g
    # 0 | 0 | 0
    # 0 | 1 | 1
    # 1 | 0 | 1
    # 1 | 1 | 1

    kd0 = randint(0, 100000)
    kd1 = randint(0, 100000)
    kg0 = randint(0, 100000)
    kg1 = randint(0, 100000)

    # Garbled table for gate #3
    # e   | d  | g
    # ke0 | kd0| kg0
    # ke1 | kd0| kg1
    # ke0 | kd1| kg1
    # ke1 | kd1| kg1

    garbled_table_3 = [[ke0, kd0, kg0], [ke1, kd0, kg1], [ke0, kd1, kg1], [ke1, kd1, kg1]]

    # Permute and double encrypt the output wire of each gate
    shuffle(garbled_table_1)
    shuffle(garbled_table_2)
    shuffle(garbled_table_3)

    def dummy_encrypt(value, key):
        return value + key
    
    # Double_encrypted_e_col
    # E_kb0(E_kc0(ke0)) 
    # E_kb0(E_kc1(ke0)) 
    # E_kb1(E_kc0(ke0)) 
    # E_kb1(E_kc1(ke1)
    double_encrypted_e_col = []
    for i in range(4):
        double_encrypted_e = dummy_encrypt(dummy_encrypt(garbled_table_1[i][2], garbled_table_1[i][1]), garbled_table_1[i][0])
        double_encrypted_e_col.append(double_encrypted_e)

    # Double_encrypted_f_col
    # E_ka0(E_ke0(kf0))
    # E_ka0(E_ke1(kf0))
    # E_ka1(E_ke0(kf0))
    # E_ka1(E_ke1(kf1))
    double_encrypted_f_col = []
    for i in range(4):
        double_encrypted_f = dummy_encrypt(dummy_encrypt(garbled_table_2[i][2], garbled_table_2[i][1]), garbled_table_2[i][0])
        double_encrypted_f_col.append(double_encrypted_f)

    # Double_encrypted_g_col
    # E_ke0(E_kd0(kg0))
    # E_ke1(E_kd0(kg1))
    # E_ke0(E_kd1(kg1))
    # E_ke1(E_kd1(kg1))
    double_encrypted_g_col = []
    for i in range(4):
        double_encrypted_g = dummy_encrypt(dummy_encrypt(garbled_table_3[i][2], garbled_table_3[i][1]), garbled_table_3[i][0])
        double_encrypted_g_col.append(double_encrypted_g)
    
    # Produce output translation table. 
    # If the output of the circuit is equal to kf0, then the output of the circuit is 0
    # If the output of the circuit is equal to kf1, then the output of the circuit is 1
    # If the output of the circuit is equal to kg0, then the output of the circuit is 0
    # If the output of the circuit is equal to kg1, then the output of the circuit is 1
        
    # Define the input of the garbled circuit
    input = [0, 1, 0, 1]

    # I want an evaluator to be able to compute the output of the circuit without learning anything about the inputs. Just the output
    # The evaluator receives the double encrypted output wire of each gate, the output translation table and the garbled inputs
    garbled_inputs = (ka0, kb1, kc0, kd1)

    # Evaluator go through each gate of the circuit and compute the output wire
    def dummy_decrypt(value, key):
        return value - key
    
    decrypted_e_col = []
    for i in range(4):
        decrypted_e_col.append(dummy_decrypt(dummy_decrypt(double_encrypted_e_col[i], garbled_inputs[2]), garbled_inputs[1]))

    decrypted_f_col = []
    for i in range(4):
        decrypted_f_col_row = []
        for j in range(4):
            decrypted_f_col_row.append(dummy_decrypt(dummy_decrypt(double_encrypted_f_col[i], decrypted_e_col[j]), garbled_inputs[0]))
        decrypted_f_col.append(decrypted_f_col_row)

    decrypted_g_col = []
    for i in range(4):
        decrypted_g_row = []
        for j in range(4):
            decrypted_g_row.append(dummy_decrypt(dummy_decrypt(double_encrypted_g_col[i], garbled_inputs[3]), decrypted_e_col[j]))
        decrypted_g_col.append(decrypted_g_row)
    
    # The evaluator uses the output translation table to decrypt the output of the circuit
    for i in range(4):
        for j in range(4):
            if decrypted_f_col[i][j] == kf0:
                print("The f output of the circuit is 0")
            if decrypted_f_col[i][j] == kf1:
                print("The f output of the circuit is 1")
            if decrypted_g_col[i][j] == kg0:
                print("The g output of the circuit is 0")
            if decrypted_g_col[i][j] == kg1:
                print("The g output of the circuit is 1")

main()