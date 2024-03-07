from random import randint

def main():
    # Define the circuit as a set of gates
    # Input of the circuit are a[x1], a[x10] and b[x1], b[x10]

    # a[x1] is the least significant bit of the input provided by Alice
    # a[x10] is the most significant bit of the input provided by Alice
    # b[x1] is the least significant bit of the input provided by Bob
    # b[x10] is the most significant bit of the input provided by Bob

    # Output of the circuit are o[x1], o[x10] and o[x100]
    # o[x1] is the least significant bit of the output (sum of the inputs)
    # o[x10] is the second least significant bit of the output (sum of the inputs)
    # o[x100] is the most significant bit of the output (sum of the inputs)

    # gate #1 XOR that takes two inputs a[x1] and b[x1] and returns one output o[x1]
    # gate #2 AND that takes two inputs a[x1] and b[x1] and returns one internal output o2
    # gate #3 XOR that takes two inputs a[x10] and b[x10] and returns one internal output o3
    # gate #4 OR that takes two inputs a[x10] and b[x10] and returns one internal output o4
    # gate #5 AND that takes two inputs a[x10] and b[x10] and returns one internal output o5
    # gate #6 XOR that takes two internal inputs o2 and o3 and returns one output o[x10]
    # gate #7 AND that takes two internal inputs o2 and o4 and returns one internal output o7
    # gate #8 OR that takes two internal inputs o7 and o5 and returns one output o[x100]

    # PHASE 1
    # Setup phase -> Alice assigns labels for inputs and intermediate outputs for each wire

    # Gate #1 XOR
    # a[x1] | b[x1] | o[x1]
    # 0     | 0     | 0
    # 0     | 1     | 1
    # 1     | 0     | 1
    # 1     | 1     | 0

    kax1_0, kax1_1 = sample_lable_tuple()
    kbx1_0, kbx1_1 = sample_lable_tuple()

    # Labelled table for gate #1
    # a[x1] | b[x1] | o[x1]
    # kax1_0| kbx1_0| -
    # kax1_0| kbx1_1| -
    # kax1_1| kbx1_0| -
    # kax1_1| kbx1_1| -

    # Gate #2 AND
    # a[x1] | b[x1] | o2
    # 0     | 0     | 0
    # 0     | 1     | 0
    # 1     | 0     | 0
    # 1     | 1     | 1

    ko2_0, ko2_1 = sample_lable_tuple()

    # Labelled table for gate #2
    # a[x1] | b[x1] | o2
    # kax1_0| kbx1_0| ko2_0
    # kax1_0| kbx1_1| ko2_0
    # kax1_1| kbx1_0| ko2_0
    # kax1_1| kbx1_1| ko2_1

    # Gate #3 XOR
    # a[x10]| b[x10]| o3
    # 0     | 0     | 0
    # 0     | 1     | 1
    # 1     | 0     | 1
    # 1     | 1     | 0

    kax10_0, kax10_1 = sample_lable_tuple()
    kbx10_0, kbx10_1 = sample_lable_tuple()
    k03_0, k03_1 = sample_lable_tuple()

    # Labelled table for gate #3
    # a[x10]| b[x10]| o3
    # kax10_0| kbx10_0| k03_0
    # kax10_0| kbx10_1| k03_1
    # kax10_1| kbx10_0| k03_1
    # kax10_1| kbx10_1| k03_0

    # Gate #4 OR
    # a[x10]| b[x10]| o4
    # 0     | 0     | 0
    # 0     | 1     | 1
    # 1     | 0     | 1
    # 1     | 1     | 1

    k04_0, k04_1 = sample_lable_tuple()

    # Labelled table for gate #4
    # a[x10]| b[x10]| o4
    # kax10_0| kbx10_0| k04_0
    # kax10_0| kbx10_1| k04_1
    # kax10_1| kbx10_0| k04_1
    # kax10_1| kbx10_1| k04_1

    # Gate #5 AND
    # a[x10]| b[x10]| o5
    # 0     | 0     | 0
    # 0     | 1     | 0
    # 1     | 0     | 0
    # 1     | 1     | 1

    k05_0, k05_1 = sample_lable_tuple()

    # Labelled table for gate #5
    # a[x10]| b[x10]| o5
    # kax10_0| kbx10_0| k05_0
    # kax10_0| kbx10_1| k05_0
    # kax10_1| kbx10_0| k05_0
    # kax10_1| kbx10_1| k05_1

    # Gate #6 XOR
    # o2    | o3    | o[x10]
    # 0     | 0     | 0
    # 0     | 1     | 1
    # 1     | 0     | 1
    # 1     | 1     | 0

    # Labelled table for gate #6
    # o2    | o3   | o[x10]
    # ko2_0 | k03_0| -
    # ko2_0 | k03_1| -
    # ko2_1 | k03_0| -
    # ko2_1 | k03_1| -

    # Gate #7 AND
    # o2    | o4    | o7
    # 0     | 0     | 0
    # 0     | 1     | 0
    # 1     | 0     | 0
    # 1     | 1     | 1

    ko7_0, ko7_1 = sample_lable_tuple()

    # Labelled table for gate #7
    # o2    | o4   | o7
    # ko2_0 | k04_0| ko7_0
    # ko2_0 | k04_1| ko7_0
    # ko2_1 | k04_0| ko7_0
    # ko2_1 | k04_1| ko7_1

    # Gate #8 OR
    # o7    | o5    | o[x100]
    # 0     | 0     | 0
    # 0     | 1     | 1
    # 1     | 0     | 1
    # 1     | 1     | 1

    # Labelled table for gate #8
    # o7    | o5   | o[x100]
    # ko7_0 | k05_0| -
    # ko7_0 | k05_1| -
    # ko7_1 | k05_0| -
    # ko7_1 | k05_1| -

    # PHASE 2
    # Alice performs the garbling of the circuit and share it with Bob
    # In particular Alice garbles the labelled output for the intermediate wires and the output wires

    # Gate #1 XOR
    garbled_1 = garble_gate([kax1_0, kax1_0, kax1_1, kax1_1], [kbx1_0, kbx1_1, kbx1_0, kbx1_1], [0, 1, 1, 0], 1)

    # Gate #2 AND
    garbled_2 = garble_gate([kax1_0, kax1_0, kax1_0, kax1_1], [kbx1_0, kbx1_1, kbx1_0, kbx1_1], [ko2_0, ko2_0, ko2_0, ko2_1], 2)

    # Gate #3 XOR
    garbled_3 = garble_gate([kax10_0, kax10_0, kax10_1, kax10_1], [kbx10_0, kbx10_1, kbx10_0, kbx10_1], [k03_0, k03_1, k03_1, k03_0], 3)

    # Gate #4 OR
    garbled_4 = garble_gate([kax10_0, kax10_0, kax10_1, kax10_1], [kbx10_0, kbx10_1, kbx10_0, kbx10_1], [k04_0, k04_1, k04_1, k04_1], 4)

    # Gate #5 AND
    garbled_5 = garble_gate([kax10_0, kax10_0, kax10_0, kax10_1], [kbx10_0, kbx10_1, kbx10_0, kbx10_1], [k05_0, k05_0, k05_0, k05_1], 5)

    # Gate #6 XOR
    garbled_6 = garble_gate([ko2_0, ko2_0, ko2_1, ko2_1], [k03_0, k03_1, k03_0, k03_1], [0, 1, 1, 0], 6)

    # Gate #7 AND
    garbled_7 = garble_gate([ko2_0, ko2_0, ko2_0, ko2_1], [k04_0, k04_1, k04_0, k04_1], [ko7_0, ko7_0, ko7_0, ko7_1], 7)

    # Gate #8 OR
    garbled_8 = garble_gate([ko7_0, ko7_0, ko7_1, ko7_1], [k05_0, k05_1, k05_0, k05_1], [0, 1, 1, 1], 8)

    # Alice choses her input (1, 1) and share the corresponding labels with Bob
    alice_labels = (kax1_1, kax10_1)

    # Bob choses his input (1, 1) and asks Alice for the corresponding labels via 1-of-2 OT
    bob_labels = (kbx1_1, kbx10_1)

    # PHASE 3 
    # Bob evaluates the circuit using the garbled circuit and the labels received from Alice

    # Gate #1 XOR
    o_x1 = decrypt_gate_output(garbled_1, alice_labels[0], bob_labels[0], 1)

    # Gate #2 AND
    o2 = decrypt_gate_output(garbled_2, alice_labels[0], bob_labels[0], 2)

    # Gate #3 XOR
    o3 = decrypt_gate_output(garbled_3, alice_labels[1], bob_labels[1], 3)

    # Gate #4 OR
    o4 = decrypt_gate_output(garbled_4, alice_labels[1], bob_labels[1], 4)

    # Gate #5 AND
    o5 = decrypt_gate_output(garbled_5, alice_labels[1], bob_labels[1], 5)

    # Gate #6 XOR
    o_x10 = decrypt_gate_output(garbled_6, o2, o3, 6)

    # Gate #7 AND
    o7 = decrypt_gate_output(garbled_7, o2, o4, 7)

    # Gate #8 OR
    o_x100 = decrypt_gate_output(garbled_8, o7, o5, 8)

    print(f"Output: {o_x1}, {o_x10}, {o_x100}")

def sample_lable_tuple():
    label_1 = randint(0, 100000)
    # if label 1 is odd, label 2 must be even. And viceversa
    if label_1 % 2 == 1:
        label_2 = randint(0, 100000)
        while label_2 % 2 == 1:
            label_2 = randint(0, 100000)
    else:
        label_2 = randint(0, 100000)
        while label_2 % 2 == 0:
            label_2 = randint(0, 100000)
    return label_1, label_2

def garble_gate(labels_bit_left, labels_bit_right, outputs, gate_index):
    garbled_gate = [0, 0, 0, 0]
    for i in range(4):
        garbled_row, index = garble_row(labels_bit_left[i], labels_bit_right[i], outputs[i], gate_index)
        garbled_gate[index] = garbled_row
    return garbled_gate

def garble_row(label_bit_left, label_bit_right, output, gate_index):
    label_bit_left_parity = label_bit_left % 2
    label_bit_right_parity = label_bit_right % 2
    if label_bit_left_parity == 0 and label_bit_right_parity == 0:
        index = 0
    elif label_bit_left_parity == 0 and label_bit_right_parity == 1:
        index = 1
    elif label_bit_left_parity == 1 and label_bit_right_parity == 0:
        index = 2
    else:
        index = 3
    
    return output + hash((gate_index, label_bit_left, label_bit_right)), index

def decrypt_gate_output(garbled_gate, label_bit_left, lable_bit_right, gate_index):
    label_bit_left_parity = label_bit_left % 2
    label_bit_right_parity = lable_bit_right % 2
    if label_bit_left_parity == 0 and label_bit_right_parity == 0:
        index = 0
    elif label_bit_left_parity == 0 and label_bit_right_parity == 1:
        index = 1
    elif label_bit_left_parity == 1 and label_bit_right_parity == 0:
        index = 2
    else:
        index = 3
    return garbled_gate[index] - hash((gate_index, label_bit_left, lable_bit_right))

main()
