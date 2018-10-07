import scrmbl


def test_version():
    assert scrmbl.__version__ == '0.1.1'


def test_echo_single(capsys):
    scrmbl.echo('this is a test')
    captured = capsys.readouterr().out
    assert captured.split('\r')[-1] == 'this is a test\n'


def test_echo_multi(capsys):
    scrmbl.echo('this is a test\nthis is also a test')
    captured = capsys.readouterr().out
    assert captured.split('\n')[0].split('\r')[-1] == 'this is a test'
    assert captured.split('\r')[-1] == 'this is also a test\n'
