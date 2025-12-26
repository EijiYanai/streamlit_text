import numpy as np
import pandas as pd
import streamlit as st

st.write(
    "実践での見習い魔法使い",
    ["一般攻撃魔法", "服が透けて見える魔法", "服の汚れを落とす魔法"],
    pd.DataFrame(np.random.rand(2, 3)),
)
