# humansizes

## Overview
Parse human-readable filesizes into bytes 

### Install

```bash
pip install humansizes
```

### Example

```python

from humansizes.convert import Humansizes


humansizes = Humansizes()

example_strings = ["1024b", "10.43 KB", "11 GB", "343.1 MB", "10.43KB", "11GB", "343.1MB", "10.43 kb", "11 gb", "343.1 mb", "10.43kb", "11gb", "343.1mb"]

for example_string in example_strings:
        print(example_string, humansizes.parse_size(example_string))
```

```bash
('1024b', 1024)
('10.43 KB', 10680)
('11 GB', 11811160064)
('343.1 MB', 359766425)
('10.43KB', 10680)
('11GB', 11811160064)
('343.1MB', 359766425)
('10.43 kb', 10680)
('11 gb', 11811160064)
('343.1 mb', 359766425)
('10.43kb', 10680)
('11gb', 11811160064)
('343.1mb', 359766425)
```


