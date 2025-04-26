# Level Tracker Plotter

This script reads decibel level data from a CSV file and generates a plot saved as a PNG image.

## Requirements

- Python 3.x
- pandas
- matplotlib

Install the required libraries:

```bash
pip install pandas matplotlib
```

## Usage

Run the script from your terminal, optionally providing the path to your CSV file as a command-line argument. If no path is provided, it defaults to `test.csv`.

```bash
python plot_decibel.py [path/to/your/data.csv]
```

For example:

```bash
python plot_decibel.py my_measurement.csv
```

Or using the default file:

```bash
python plot_decibel.py
```

## Output

The generated plot image (e.g., `test.png` or `my_measurement.png`) will be saved in the `output` directory.

## Script Details (`plot_decibel.py`)

- Reads a CSV file (default encoding: Shift_JIS / `cp932`).
- Skips the first 4 rows by default.
- Removes leading/trailing whitespace from column names.
- Drops the 'ｱﾄﾞﾚｽ' column if it exists.
- Plots all numerical columns against time (calculated assuming 10 samples per second).
- Saves the plot to the `output` directory.
