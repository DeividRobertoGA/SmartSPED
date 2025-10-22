def correcao17COD_CTA(array):
    for sub_array in array:
        if len(sub_array) >= 2 and sub_array[0] == "C175" and sub_array[1] in ["5405", "5102"] and sub_array[-2] == "":
            sub_array[-2] = "64"