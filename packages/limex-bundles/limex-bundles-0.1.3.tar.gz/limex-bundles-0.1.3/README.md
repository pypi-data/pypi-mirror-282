# limex-bundles

`limex-bundles` is a Python library designed to make it easy to add Limex data bundles to Zipline. This package simplifies the process of copying necessary bundle files to the correct locations within your Zipline installation.

## Features

- Automatically checks if Zipline is installed
- Copies necessary bundle files to the correct locations
- Updates the LimEx configuration with your API key

## Installation

You can install `limex-bundles` from PyPi using pip:

```sh
pip install limex-bundles
```

## Usage

The primary function provided by this package is install_bundle, which requires your Limex API key as a parameter.

```sh
from limex_bundle.installer import install_bundle

# Replace 'YOUR_API_KEY' with your actual Limex Data Hub API key
api_key = 'YOUR_API_KEY'
install_bundle(api_key)
```

