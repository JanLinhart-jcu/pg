from cviceni8 import obsah_ctverce, obvod_ctverce, pocet_pismen, index_pismene, fibonachi


def test_obsah_ctverce():
    assert obsah_ctverce(4) == 16
    assert obsah_ctverce(5) == 25


def test_obvod_ctverce():
    assert obvod_ctverce(4) == 16
    assert obvod_ctverce(5) == 20


def test_pocet_pismen():
    assert pocet_pismen("ahoj, jak se mas?", "a") == 3
    assert pocet_pismen("ahoj, jak se mas?", "j") == 2


def test_index_pismene():
    assert index_pismene("ahoj, jak se mas?", "a") == [0, 7, 14]
    assert index_pismene("ahoj, jak se mas?", "x") == []


def test_fibonachi():
    assert fibonachi(5) == [1, 1 ,2 ,3, 5]
    assert fibonachi(10) == [1, 1 ,2 ,3, 5, 8]