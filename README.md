# Pi Calculator

A Python project to calculate the value of Pi (π) to any number of decimal places using arbitrary precision arithmetic with the built-in decimal module.

## Features

- Calculate Pi to any number of decimal places (limited only by available memory and time)
- Uses the Machin formula with Taylor series expansion for high-precision computation
- Command-line interface with argument parsing
- No external dependencies required

## Installation

1. Ensure you have Python 3.6+ installed
2. No additional packages needed - uses only built-in modules

## Usage

Run the calculator from the command line:

```bash
python pi_calculator.py <n>
```

Where `<n>` is the number of decimal places you want.

### Examples

```bash
# Pi to 10 decimal places
python pi_calculator.py 10
# Output: 3.1415926535

# Pi to 50 decimal places
python pi_calculator.py 50

# Pi to 1000 decimal places
python pi_calculator.py 1000
```

## How it works

The script uses the Machin formula: π/4 = 4×arctan(1/5) - arctan(1/239)

It computes arctan using Taylor series expansion with the decimal module for arbitrary precision.

## Limitations

- Very large values of n (>1000) may take significant time
- The computation time increases roughly with n²
- Limited by Python's decimal module precision limits

## Troubleshooting

- The script requires Python 3.6 or higher
- For very large n, be patient as computation may take time
- If you need even higher precision or faster computation, consider using specialized libraries like mpmath