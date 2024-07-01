# jmeter_compare

(c) 2024 - [@YoKulGuy](https://twitter.com/YoKulGuy)

`jmeter_compare` is a command-line tool for comparing JMeter CSV results. It generates an HTML report with statistical comparisons and percentile graphs, making it easy to analyze performance differences between test runs.

## Features

- Compare two JMeter CSV result files (current vs. baseline)
- Generate overall performance statistics
- Provide label-wise comparisons
- Create percentile graphs for each label
- Output an easy-to-read HTML report

## Installation

You can install `jmeter_compare` using pip:

```
pip install jmeter_compare
```

## Requirements

- Python 3.6+
- matplotlib

## Usage

After installation, you can use the `jmeter_compare` command from your terminal:

```
jmeter_compare <current_csv> <baseline_csv> <output_html>
```

Where:
- `<current_csv>` is the path to your current JMeter results CSV file
- `<baseline_csv>` is the path to your baseline JMeter results CSV file
- `<output_html>` is the path where you want to save the output HTML report

Example:

```
jmeter_compare current_results.csv baseline_results.csv comparison_report.html
```

## Output

The tool generates an HTML report that includes:

1. Overall statistics comparing current and baseline results
2. Label-wise statistics for each unique label in the JMeter results
3. Percentile graphs for each label, comparing current and baseline performance

The report highlights improvements in green and regressions in red for easy identification of performance changes.

## CSV File Format

The tool expects JMeter CSV result files with at least the following columns:

- `timeStamp`
- `elapsed`
- `label`
- `responseCode`
- `responseMessage`
- `threadName`
- `success`
- `bytes`
- `grpThreads`
- `allThreads`
- `Latency`
- `Hostname`
- `Connect`

## Contributing

Contributions to `jmeter_compare` are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Support

If you encounter any problems or have any questions, please open an issue on the GitHub repository.
