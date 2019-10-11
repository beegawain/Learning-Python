def test01():
    print("test01")
    test01()         #test01没执行完，test01(1)就执行了,text01没执行完，就执行test01(2)

def test02():
    print("test02")

test01()