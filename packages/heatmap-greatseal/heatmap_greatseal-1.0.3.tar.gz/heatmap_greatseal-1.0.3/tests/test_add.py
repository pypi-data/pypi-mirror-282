import heatmap_greatseal as hm

def test_correct_output():
    assert hm.add([[1,1],[1,1]], [[1,1],[1,1]]) == [2,2]