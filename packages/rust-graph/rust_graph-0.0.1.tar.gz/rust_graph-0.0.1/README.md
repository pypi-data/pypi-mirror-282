# rust-graph

[![image](https://img.shields.io/pypi/v/rust-graph.svg)](https://pypi.python.org/pypi/rust-graph)
[![image](https://img.shields.io/pypi/l/rust-graph.svg)](https://pypi.python.org/pypi/rust-graph)
[![image](https://img.shields.io/pypi/pyversions/rust-graph.svg)](https://pypi.python.org/pypi/rust-graph)
[![Actions status](https://github.com/deargen/rust-graph/workflows/Deploy%20a%20new%20version/badge.svg)](https://github.com/deargen/rust-graph/actions)

|  |  |
|--|--|
| [![pytest](https://img.shields.io/badge/pytest-black)](https://github.com/pytest-dev/pytest) [![cargo test](https://img.shields.io/badge/cargo%20test-black)](https://doc.rust-lang.org/cargo/commands/cargo-test.html) | [![Actions status](https://github.com/deargen/rust-graph/workflows/Tests/badge.svg)](https://github.com/deargen/rust-graph/actions) |
| [![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv) | [![Actions status](https://github.com/deargen/rust-graph/workflows/Check%20pip%20compile%20sync/badge.svg)](https://github.com/deargen/rust-graph/actions) |

Graph algorithms implemented in Rust, available as a Python package.

So far, there is only one function implemented: `all_pairs_dijkstra_path_length`. It's a re-write of the `networkx` function with the same name and should return the same results.

## Installation

```bash
pip install rust-graph
```

## Usage

```python
from rust_graph import all_pairs_dijkstra_path_length

weighted_edges = [
    (0, 1, 1.0),
    (1, 2, 2.0),
    (2, 3, 3.0),
    (3, 0, 4.0),
    (0, 3, 5.0),
]

shortest_paths = all_pairs_dijkstra_path_length(weighted_edges, cutoff=3.0)
```

```python
>>> shortest_paths
{3: {3: 0.0, 2: 3.0}, 2: {2: 0.0, 1: 2.0, 0: 3.0, 3: 3.0}, 1: {0: 1.0, 2: 2.0, 1: 0.0}, 0: {1: 1.0, 0: 0.0, 2: 3.0}}
```

## Benchmark

