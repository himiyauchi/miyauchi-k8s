from arith.add import Add

def test_0_add_0_eq_0():  # 0+0=0
    assert Add.add(0, 0) == 0

def test_1_add_2_eq_3():  # 1+2=3
    assert Add.add(1, 2) == 3

def test_m1_add_2_eq_1():  # -1+2=1
    assert Add.add(-1, 2) == 1
