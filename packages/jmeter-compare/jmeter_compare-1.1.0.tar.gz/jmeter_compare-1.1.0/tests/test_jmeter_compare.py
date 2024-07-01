import pytest
from jmeter_compare import read_csv, calculate_stats, calculate_label_stats, create_percentile_graph, generate_html
import os
import tempfile

@pytest.fixture
def sample_data():
    return [
        {'elapsed': '100', 'label': 'Homepage'},
        {'elapsed': '150', 'label': 'Homepage'},
        {'elapsed': '200', 'label': 'Login'},
        {'elapsed': '250', 'label': 'Login'},
        {'elapsed': '300', 'label': 'Search'},
    ]

def test_read_csv():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        tmp.write("elapsed,label\n100,Homepage\n150,Homepage\n200,Login\n")
        tmp.flush()

        data = read_csv(tmp.name)
        assert len(data) == 3
        assert data[0]['elapsed'] == '100'
        assert data[0]['label'] == 'Homepage'

    os.unlink(tmp.name)

def test_calculate_stats(sample_data):
    stats = calculate_stats(sample_data)
    assert stats['min'] == 100
    assert stats['max'] == 300
    assert stats['avg'] == 200
    assert stats['median'] == 200

def test_create_percentile_graph():
    current_data = [100, 200, 300, 400, 500]
    baseline_data = [90, 180, 270, 360, 450]
    graph = create_percentile_graph(current_data, baseline_data, 'Test Label')
    assert isinstance(graph, str)
    assert graph.startswith('iVBORw0KGgo')  # Base64 encoded PNG always starts with this

def test_generate_html():
    current_stats = {'min': 100, 'max': 500, 'avg': 300}
    baseline_stats = {'min': 90, 'max': 450, 'avg': 270}
    current_label_stats = {'Test': {'min': 100, 'max': 500, 'avg': 300, 'raw_data': [100, 300, 500]}}
    baseline_label_stats = {'Test': {'min': 90, 'max': 450, 'avg': 270, 'raw_data': [90, 270, 450]}}

    html = generate_html(current_stats, baseline_stats, current_label_stats, baseline_label_stats)
    assert isinstance(html, str)
    assert '<html>' in html
    assert '<table>' in html
    assert 'Test' in html
    assert 'data:image/png;base64,' in html

def test_main(monkeypatch, tmpdir):
    current_csv = tmpdir.join("current.csv")
    current_csv.write("elapsed,label\n100,Test\n200,Test\n300,Test\n")

    baseline_csv = tmpdir.join("baseline.csv")
    baseline_csv.write("elapsed,label\n90,Test\n180,Test\n270,Test\n")

    output_html = tmpdir.join("output.html")

    monkeypatch.setattr('sys.argv', ['jmeter_compare', str(current_csv), str(baseline_csv), str(output_html)])

    import jmeter_compare
    jmeter_compare.main()

    assert output_html.exists()
    content = output_html.read()
    assert '<html>' in content
    assert 'Test' in content
    assert 'data:image/png;base64,' in content

if __name__ == '__main__':
    pytest.main()
