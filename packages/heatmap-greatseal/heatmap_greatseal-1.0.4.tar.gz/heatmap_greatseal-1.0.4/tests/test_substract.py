import heatmap_greatseal.heatmap_greatseal as hm

def test_correct_output():
    assert hm.substract([[1,1],[1,1]], [[1,1],[1,1]]) == [[0,0],[0,0]]

def test_empty_matrix():
    assert hm.substract([[]], [[1,1],[1,1]]) == False

def test_not_same_shape():
    assert hm.substract([[1,1,1],[1,1,1],[1,1,1]],[[1,1],[1,1]]) == False