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

value = streamlit_list_with_loader()

st.write(value)
```

## Dev

```sh
streamlit run streamlit-list-with-loader/src/streamlit_list_with_loader/__init__.py
```