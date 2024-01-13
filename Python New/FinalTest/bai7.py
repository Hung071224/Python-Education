



lst = [5, 1, 8, 92, -1, 30]
def sap_xep(lst):
    ket_qua = []
    while lst:
        min = lst[0]
        for x in lst:
            if x < min:
                min = x
        ket_qua.append(min)
        lst.remove(min)
    return ket_qua
lst_sap_xep = sap_xep(lst)
print("List sau khi sắp xếp là: ")

















































