from app import index

""" Add a new env path: 
    -export PYTHONPATH=src
    -echo $PYTHONPATH """


def test_index():
    assert index() == "Hello World!"
