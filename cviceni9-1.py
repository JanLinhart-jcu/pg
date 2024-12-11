def nejvetsi(seznam_cisel):
    
    return max(seznam_cisel)



def test_nejvetsi():
    assert nejvetsi([1,2,3,4,5]) == 5
    assert nejvetsi([100,90,80,70]) == 100