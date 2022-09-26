import streamlit as st  # web app
import pandas as pd  # data manipulation
import numpy as np  # random gen

st.title("Marketing KPI - Key Metric Dashboard")

st.subheader("Using Python ‍🚀📈")

kpi1, kpi2, kpi3 = st.columns(3)

st.markdown('### Key Metrics')

kpi1.metric(label="$APPL",
            value=200.22,
            delta=1.34, )

kpi2.metric(label="$GOOGL",
            value=143.22,
            delta=-3.34, )

kpi3.metric(label="$CLOUD",
            value=321.22,
            delta=2.4, )

st.markdown('### Important Charts 📈')

chart1, chart2 = st.columns(2)

chart_data = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

chart1.bar_chart(chart_data)
chart2.line_chart(chart_data)

st.dataframe(chart_data)