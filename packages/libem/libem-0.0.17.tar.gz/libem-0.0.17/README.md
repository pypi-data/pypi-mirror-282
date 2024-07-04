# Libem

An open-source toolchain for fast entity matching with human-level accuracy, powered by LLMs and tools.

## Installation

```bash
make install
```







To run the sample example.

```bash
make run
```

You can also install libem library with pip:

```bash
pip install libem
```

## Usage

```python
import libem

libem.match("apple", "orange")
```

In shell:

```bash
libem apple orange
```

## Conventions

Libem enforces a strict naming convention for a toolchain and the tool access methods.
Toolchain's main methods are defined in the interface.py and exposed at the toolchain level.
For example, the following code will import the tune tool in libem toolchain.

```python
from libem import tune
```

To import the libem.tune toolchain, we must explicitly invoke:

```python 
import libem

tune = libem.toolchain("libem.tune") 
```

Note that this does not prevent us from importing the tools in the toolchain directly:

```python
from libem.tune import learn
```

In a nutshell, one can directly import a toolchain's tools but not the tool's module. 
This is to _encourage_ (but not enforce) that tools are always accessed via well-defined methods consistent with the LM access.