class VektorboyutuHatasi(Exception):
    pass


def ic_carpim(L1, L2):
    if len(L1)!=len(L2):
        raise VektorboyutuHatasi("Parametreler ayni sayida elemandan olusmali")
    return sum([a*b for (a,b) in zip(L1,L2) ])





try:
    ic_carpim([1,2,3,4], [-1,0,1])
except VektorboyutuHatasi as e:
    print(e)





