import heatmap_greatseal.heatmap_greatseal as hm

def test_correct_output():
    assert hm.add([[1,1],[1,1]], [[1,1],[1,1]]) == [[2,2],[2,2]]

def test_empty_matrix():
    assert hm.add([[]], [[1,1],[1,1]]) == False

def test_not_same_shape():
    assert hm.add([[1,1,1],[1,1,1]],[[1,1],[1,1]]) == False