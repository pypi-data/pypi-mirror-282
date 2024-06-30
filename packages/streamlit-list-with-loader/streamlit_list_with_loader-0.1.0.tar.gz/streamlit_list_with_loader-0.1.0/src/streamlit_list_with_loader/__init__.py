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
    data: list[dict[str, bool]] = [],
    on_click: WidgetCallback | None = None,
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        key=key,
        data=data,
        on_click=on_click
    )

    return component_value


def main():
    st.write("## Example")

    data = [
        { "name": "file_1.txt", "status": "loading" },
        { "name": "file_2.txt", "status": "loading" },
        { "name": "file_3.txt", "status": "loading" },
    ]

    streamlit_list_with_loader(data=data)

if __name__ == "__main__":
    main()
