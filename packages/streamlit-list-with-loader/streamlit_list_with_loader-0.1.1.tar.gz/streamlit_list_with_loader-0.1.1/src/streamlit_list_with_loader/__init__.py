from pathlib import Path
from typing import Optional
from streamlit.runtime.state import WidgetCallback

import streamlit as st
import streamlit.components.v1 as components
import time

# Tell streamlit that there is a component called streamlit_list_with_loader,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"streamlit_list_with_loader", path=str(frontend_dir)
)

# Create the python function that will be called
def streamlit_list_with_loader(
    key: Optional[str] = None,
    data: list[dict[str, bool]] = []
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        key=key,
        data=data
    )

    return component_value


def main():
    st.write("## Example")

    data = [
        { "name": "file_1.txt", "status": "loading" },
        { "name": "file_2.txt", "status": "loading" },
        { "name": "file_3.txt", "status": "loading" },
        { "name": "file_4.txt", "status": "loading" }
    ]

    st.markdown("""
        <style>
            .element-container {
                height: 50px
            }

            .element-container:nth-child(2) {
                display: none
            }
        </style>
        """, unsafe_allow_html=True)

    for idx, item in enumerate(data):
        streamlit_list_with_loader(key=idx, data=item)

if __name__ == "__main__":
    main()
