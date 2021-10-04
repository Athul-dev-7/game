import conway

def test_get_live_neighbours():
    assert conway.get_live_neighbours_count(0, 0, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 1
    assert conway.get_live_neighbours_count(0, 1, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 1
    assert conway.get_live_neighbours_count(0, 2, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 2
    assert conway.get_live_neighbours_count(1, 0, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 3
    assert conway.get_live_neighbours_count(1, 1, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 5
    assert conway.get_live_neighbours_count(1, 2, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 3
    assert conway.get_live_neighbours_count(2, 0, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 1
    assert conway.get_live_neighbours_count(2, 1, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 3
    assert conway.get_live_neighbours_count(2, 2, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 2
    assert conway.get_live_neighbours_count(3, 0, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 2
    assert conway.get_live_neighbours_count(3, 1, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 3
    assert conway.get_live_neighbours_count(3, 2, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 2
    
    
def test_apply_4_rules():
    assert conway.apply_4_rules(0, 0, 1, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 0
    assert conway.apply_4_rules(0, 1, 1, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 0
    assert conway.apply_4_rules(0, 2, 2, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 0
    assert conway.apply_4_rules(1, 0, 3, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 1
    assert conway.apply_4_rules(1, 1, 5, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 0
    assert conway.apply_4_rules(1, 2, 3, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 1
    assert conway.apply_4_rules(2, 0, 1, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 0
    assert conway.apply_4_rules(2, 1, 3, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 1
    assert conway.apply_4_rules(2, 2, 2, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 1
    assert conway.apply_4_rules(3, 0, 2, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 0
    assert conway.apply_4_rules(3, 1, 3, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 1
    assert conway.apply_4_rules(3, 2, 2, [[0, 1, 0],[0, 0, 1],[1, 1, 1],[0, 0, 0]]) == 0
    
    

 