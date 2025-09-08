import streamlit as st

import pandas as pd
import numpy as np

data = np.random.randn(1000)

st.title('Histogram')
hist_value,hist_bins = np.histogram(data,bins=20)
st.bar_chart(hist_value)