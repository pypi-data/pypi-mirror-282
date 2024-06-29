from cdh-test-pkg import hello_world

def test_hello_world():
    assert hello_world() == 'Hello from cdh-test-pkg!'
