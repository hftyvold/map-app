import streamlit.components.v1 as components
import os

# Declare the Streamlit component for the map
_component_func = components.declare_component(
    "my_map_component", 
    path=os.path.join(os.path.dirname(__file__), "frontend/build")
)

def show_map():
    return _component_func()
