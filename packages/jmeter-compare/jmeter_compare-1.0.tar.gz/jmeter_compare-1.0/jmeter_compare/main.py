import argparse
import csv
from typing import List, Dict
import statistics
import base64
from io import BytesIO
import matplotlib.pyplot as plt


def read_csv(file_path: str) -> List[Dict]:
    """Read CSV file and return list of dictionaries."""
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def calculate_stats(data: List[Dict]) -> Dict:
    """Calculate statistics for the given data."""
    elapsed_times = [float(row['elapsed']) for row in data]
    return {
        'min': min(elapsed_times),
        'max': max(elapsed_times),
        'avg': statistics.mean(elapsed_times),
        'median': statistics.median(elapsed_times),
        # Percentile calculations:
        # We use different n values for efficiency while maintaining precision.
        # The statistics.quantiles() function internally sorts the data.

        # 90th percentile: divide data into 10 groups (deciles), take the 9th
        # (index 8)
        '90th_percentile': statistics.quantiles(elapsed_times, n=10)[8],

        # 95th percentile: divide data into 20 groups (ventiles),
        # take the 19th (index 18)
        # This is the smallest n that gives us a precise 95th percentile
        '95th_percentile': statistics.quantiles(elapsed_times, n=20)[18],

        # 99th percentile: divide data into 100 groups (percentiles),
        # take the 99th (index 98)
        # We need n=100 to get this level of precision
        '99th_percentile': statistics.quantiles(elapsed_times, n=100)[98],
    }


def calculate_label_stats(data: List[Dict]) -> Dict[str, Dict]:
    """Calculate statistics for each label in the data."""
    label_stats = {}
    for row in data:
        label = row['label']
        elapsed = float(row['elapsed'])
        if label not in label_stats:
            label_stats[label] = []
        label_stats[label].append(elapsed)

    for label, times in label_stats.items():
        label_stats[label] = {
            'min': min(times),
            'max': max(times),
            'avg': statistics.mean(times),
            'median': statistics.median(times),
            '90th_percentile': statistics.quantiles(times, n=10)[8],
            '95th_percentile': statistics.quantiles(times, n=20)[18],
            '99th_percentile': statistics.quantiles(times, n=100)[98],
            # Store sorted raw data for percentile graph
            'raw_data': sorted(times)
        }

    return label_stats


def create_percentile_graph(
        current_data: List[float],
        baseline_data: List[float],
        label: str) -> str:
    """Create a percentile graph comparing current and baseline data."""
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(current_data)), current_data, label='Current')
    plt.plot(range(len(baseline_data)), baseline_data, label='Baseline')
    plt.title(f'Percentile Graph for {label}')
    plt.xlabel('Percentile')
    plt.ylabel('Response Time (ms)')
    plt.legend()
    plt.grid(True)

    # Save the plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image to base64 for embedding in HTML
    graphic = base64.b64encode(image_png).decode('utf-8')
    plt.close()
    return graphic


def generate_html(current_stats: Dict,
                  baseline_stats: Dict,
                  current_label_stats: Dict[str, Dict],
                  baseline_label_stats: Dict[str, Dict]) -> str:
    """Generate HTML report comparing current and baseline statistics."""
    html = """
    <html>
    <head>
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
                margin-bottom: 20px;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: right;
            }
            th {
                background-color: #f2f2f2;
            }
            .better { color: green; }
            .worse { color: red; }
            h2 { margin-top: 30px; }
            img { max-width: 100%; height: auto; }
        </style>
    </head>
    <body>
        <h2>Overall Statistics</h2>
        <table>
            <tr>
                <th>Metric</th>
                <th>Current</th>
                <th>Baseline</th>
                <th>Difference</th>
            </tr>
    """

    for metric in current_stats.keys():
        current_value = current_stats[metric]
        baseline_value = baseline_stats[metric]
        diff = current_value - baseline_value
        diff_class = 'better' if diff <= 0 else 'worse'

        html += f"""
            <tr>
                <td>{metric}</td>
                <td>{current_value:.2f}</td>
                <td>{baseline_value:.2f}</td>
                <td class="{diff_class}">{diff:.2f}</td>
            </tr>
        """

    html += """
        </table>
        <h2>Label-wise Statistics</h2>
    """

    all_labels = set(
        current_label_stats.keys()) | set(
        baseline_label_stats.keys())

    for label in all_labels:
        html += f"""
        <h3>{label}</h3>
        <table>
            <tr>
                <th>Metric</th>
                <th>Current</th>
                <th>Baseline</th>
                <th>Difference</th>
            </tr>
        """

        current_label_data = current_label_stats.get(label, {})
        baseline_label_data = baseline_label_stats.get(label, {})

        for metric in [
            'min',
            'max',
            'avg',
            'median',
            '90th_percentile',
            '95th_percentile',
                '99th_percentile']:
            current_value = current_label_data.get(metric, 0)
            baseline_value = baseline_label_data.get(metric, 0)
            diff = current_value - baseline_value
            diff_class = 'better' if diff <= 0 else 'worse'

            html += f"""
                <tr>
                    <td>{metric}</td>
                    <td>{current_value:.2f}</td>
                    <td>{baseline_value:.2f}</td>
                    <td class="{diff_class}">{diff:.2f}</td>
                </tr>
            """

        html += "</table>"

        # Add percentile graph
        current_raw_data = current_label_data.get('raw_data', [])
        baseline_raw_data = baseline_label_data.get('raw_data', [])
        if current_raw_data and baseline_raw_data:
            graph = create_percentile_graph(
                current_raw_data, baseline_raw_data, label)
            html += f"""
            <img src="data:image/png;base64,{graph}"
            alt="Percentile Graph for {label}">
            """

    html += """
    </body>
    </html>
    """
    return html


def main():
    parser = argparse.ArgumentParser(description='Compare JMeter CSV results')
    parser.add_argument(
        'current_csv',
        help='Path to the current results CSV file')
    parser.add_argument('baseline_csv', help='Path to the baseline CSV file')
    parser.add_argument(
        'output_html',
        help='Path to save the output HTML file')
    args = parser.parse_args()

    current_data = read_csv(args.current_csv)
    baseline_data = read_csv(args.baseline_csv)

    current_stats = calculate_stats(current_data)
    baseline_stats = calculate_stats(baseline_data)

    current_label_stats = calculate_label_stats(current_data)
    baseline_label_stats = calculate_label_stats(baseline_data)

    html_content = generate_html(
        current_stats,
        baseline_stats,
        current_label_stats,
        baseline_label_stats)

    with open(args.output_html, 'w') as f:
        f.write(html_content)

    print(f"Comparison results saved to {args.output_html}")


if __name__ == "__main__":
    main()
