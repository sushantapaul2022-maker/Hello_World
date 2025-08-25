# file: facefusion/uis/layouts/share.py
import gradio
from facefusion.uis.layouts import default

def pre_check() -> bool:
    return default.pre_check()

def pre_render() -> bool:
    return default.pre_render()

def render() -> gradio.Blocks:
    return default.render()

def listen() -> None:
    default.listen()

def run(ui: gradio.Blocks) -> None:
    ui.launch(show_api=False, share=True)
