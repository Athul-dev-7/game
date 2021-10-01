import conway

def test_helper():
    try:
        assert conway.helper(0,0) == 0
        assert conway.helper(0,0) == 1
        assert conway.helper(0,0) == 2
        assert conway.helper(0,0) == 3
        assert conway.helper(0,1) == 5
    except NameError:
        assert True

def test_rules_live():
    try:
        assert conway.rules(0,1,2) == 1
        assert conway.rules(0,1,3) == 1
        assert conway.rules(0,1,3) == 1
    except NameError:
        assert True
        
    
def test_rules_dead():
    try:
        assert conway.rules(0,0,1) == 0
        assert conway.rules(0,0,2) == 0
        assert conway.rules(0,0,4) == 0
    except NameError:
        assert True