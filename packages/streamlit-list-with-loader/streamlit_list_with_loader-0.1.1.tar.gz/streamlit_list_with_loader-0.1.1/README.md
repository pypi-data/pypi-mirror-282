# streamlit-list-with-loader

A streamlist component that allows you to have a liist with loading status

## Installation instructions 

```sh
pip install streamlit-list-with-loader
```

## Usage instructions

```python
import streamlit as st

from streamlit_list_with_loader import streamlit_list_with_loader

data = [
    { "name": "file_1.txt", "status": "failed" },
    { "name": "file_2.txt", "status": "loading" },
    { "name": "file_3.txt", "status": "loading" },
]

for item in data:
    streamlit_list_with_loader(data=data)
```