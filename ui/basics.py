import string
from random import random
from typing import Dict, Callable

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path


def show_text_widgets() -> None:
    st.header("Display text")
    st.write("This section shows the diverse way how text can be displayed in [streamlit](https://www.streamlit.io/)")

    st.subheader("Regular text")
    with st.echo():
        st.text("Hello World")

    # Markdown

    st.write("------")
    st.subheader("Better formatting with Markdown")
    with st.echo():
        st.markdown("Hello **World** :wave:")

    with st.echo():
        st.markdown("""
        Markdown allows:
        * making ordered lists
            * nested
            * (un-) ordered
        * show $\LaTeX$ when wrapping it in `$ $`
        * URLs: [fhLUG](https://fhlug.at/)
        """)

    st.write("`markdown` can be used to display (unsafe) HTML code by setting the `unsafe_allow_html`-flag")
    with st.echo():
        html_wrapper = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""
        displacy_res = """
        <div class="entities" style="line-height: 2.5; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; font-size: 18px">
            When
            <mark class="entity" style="background: #aa9cfc; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em">
                Bob
                <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">PERSON</span>
            </mark>
            started working on self-driving cars at
            <mark class="entity" style="background: #7aecec; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em">
                Google
                <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">ORG</span>
            </mark>
            in
            <mark class="entity" style="background: #bfe1d9; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em">
                2007
                <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">DATE</span>
            </mark>
            , few people outside of the company took him seriously.
        </div>
        """
        st.markdown(html_wrapper.format(displacy_res), unsafe_allow_html=True)

    # Latex
    st.write("------")
    st.subheader("Show $\LaTeX$")
    with st.echo():
        st.latex(r"f(x) = \frac{1} {\sigma \sqrt{2\pi}} e^{-\frac{1}{2} (\frac{x-\mu}{\sigma})^2}")

    st.write("------")
    st.subheader("Show Code")

    st.markdown("""Code can be displayed using the `st.code()` command.
    When using this command to display code, syntax highlighting is enabled.
    """)
    st.code("""st.code('print("Hello World")')""")
    st.markdown("Which outputs the following:")
    st.code('print("Hello World")')

    st.markdown("""A nice utility function to document code is the `echo`-command.  
    `echo()` is a _context manager_ that outputs everything in its scope as code
    """)

    st.code("""with st.echo():\n\tst.code('print("Hello World")')""")

    # write
    st.markdown("-----")
    st.write("""
    ### universal `write` command
    > This is the swiss-army knife of Streamlit commands. It does different things depending on what you throw at it.
    """)

    with st.echo():
        st.write("""
        the `write` function can:
        * display `markdown`
        * display `dataframe`
        * display exceptions
        * display information about a function
        * display dictionaries in interactive widgets
        * display charts
        *
        """, "take multiple arguments")

    st.write("#### display dict")
    with st.echo():
        st.write({"a": 1, "b": 2})

    st.write("#### function information ")
    with st.echo():
        def inspect_me(data: pd.DataFrame) -> bool:
            """
            A dummy function which has a very insightful doc-string
            :param data: pandas Dataframe containing useful data
            :return: returns always True
            """
            return True

        st.write(inspect_me)

    st.write("""
    -----
    _For completeness: there are also [magic commands](https://docs.streamlit.io/api.html#magic-commands)_  
    > Magic commands are a feature in Streamlit that allows you to 
    write markdown and data to your app with very few keypresses.  
    > How it works is simple: any time Streamlit sees either a variable or literal value on its own line,
     it automatically writes that to your app using `st.write`.
    """)


def show_tabular_data() -> None:
    n = 20
    df = pd.DataFrame({"Column A": np.random.randint(0, 100, n),
                       "Column B": np.random.randn(n),
                       "Column C": np.random.randint(0, 10, n)})

    st.subheader("Show dataframe")

    if st.checkbox("Highlight maximum value"):
        with st.echo():
            df = df.style.highlight_max(axis=0)

    with st.echo():
        st.dataframe(df, 1000)
    st.markdown("_Note: bug with width most likely fixed in next version_")

    st.subheader("Show table")
    with st.echo():
        st.table(df)


def show_media_widgets() -> None:
    DATA = Path('data/external')
    st.write("""
    ### Display images """)

    st.write("#### Reference images")
    with st.echo():
        st.image("https://www.dogalize.com/wp-content/uploads/2018/03/ceiling-cat.jpg",
                 caption="Ceiling cat", use_column_width=True)

    st.write("#### Embed image")
    with st.echo():
        st.image("""data:image/jpeg;base64,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""",
                 caption="embedded image", width=500)

    # audio
    st.write("------")
    st.subheader("Embed audio")
    with st.echo():
        audio_file = open(DATA/'applause7.mp3', 'rb')
        st.audio(audio_file, format='audio/mp3')
    st.write("_Note: seems to have trouble in Firefox_")

    # video
    st.write("------")
    st.subheader("Embed video")
    with st.echo():
        st.video("https://www.youtube.com/watch?v=B2iAodr0fOo", start_time=2)


def get_sections() -> Dict[str, Callable]:
    return {
        "Show text widgets": show_text_widgets,
        "Show tabular data": show_tabular_data,
        "Show media widgets": show_media_widgets
    }
