import heatmap_greatseal.heatmap_greatseal as hm

def test_0_degree_returns_same_matrix():
    assert hm.rotate([[1,1,1],[2,2,2],[3,3,3]], 0) == [[1,1,1],[2,2,2],[3,3,3]]

def test_negative_rotate():
    assert hm.rotate([[1,1,1],[2,2,2],[3,3,3]], -90) == [[1,2,3],[1,2,3],[1,2,3]]

def test_empty_matrix():
    assert hm.rotate([[]], 90) == [[]]

def test_more_than_full_circle():
    assert hm.rotate([[1,1,1],[2,2,2],[3,3,3]], 450) == [[3,2,1],[3,2,1],[3,2,1]]