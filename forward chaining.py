global facts
global is_changed

is_changed =True
facts=[["vertbrates","duck"],["flying","duck"],["mammal",'cat']]

def assert_f(fact):
    global facts,is_changed

    if not fact in facts:
        facts +=[fact]
        is_changed=True
    
while is_changed:
    is_changed=False

    for a1 in facts:
        if a1[0]=="mammal":
            assert_f(["vertbrates",a1[1]])
        if a1[0]=="vertbrates":
            assert_f(["animals",a1[1]])
        
        if a1[0]=="vertbrates" and ["flying",a1[1]] in facts:
            assert_f(['baris',a1[1]])

print(facts)
