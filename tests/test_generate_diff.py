from gendiff.generate_diff import generate_diff

def test_generate_diff():
    result = generate_diff('file1.json', 'file2.yml')
    assert isinstance(result, list)
    assert any(i[0] in ['added', 'removed', 'changed'] for i in result)
