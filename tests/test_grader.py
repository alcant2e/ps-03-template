from src import grader


def test_grader():
    assert grader.grade_letter(-3) == None
    assert grader.grade_letter(87) == "B"
    assert grader.grade_letter(55) == "F"
    assert grader.grade_letter(69) == "D"
