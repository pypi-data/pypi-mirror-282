import heatmap_greatseal.heatmap_greatseal as hm

test = [[1,2,3],
        [1,2,3],
        [1,2,3]]
rect = [[1,2,3],
        [1,2,3]]
rect2 = [[1,2],
         [1,2],
         [1,2]]

def test_empty_matrix():
    assert hm.neighbours([[]], 0,0) == []

def test_negative_indexes():
    assert hm.neighbours(test, -1,-1) == [1]
    assert hm.neighbours(test, -2,-2) == []

def test_not_square_matrix():
    assert hm.neighbours(rect, 0,0) == [2,1,2]

def test_corner():
    assert hm.neighbours(test, 0,0) == [2,1,2]
    assert hm.neighbours(test, 0,2) == [2,2,3]
    assert hm.neighbours(test, 2,0) == [1,2,2]
    assert hm.neighbours(test, 2,2) == [2,3,2]

def test_side():
    assert hm.neighbours(test, 1,0) == [1,2,2,1,2]
    assert hm.neighbours(rect2, 1,0) == [1,2,2,1,2]

def test_out_of_range_index():
    assert hm.neighbours(test, 10, 10) == []