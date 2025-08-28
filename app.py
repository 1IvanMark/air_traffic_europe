import streamlit as st
import time
import pandas as pd
from datetime import datetime
from data_source import DataSource
from chart import ChartCreator

st.set_page_config(
    page_title="✈️ Europe Air Traffic",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("✈️ Real-time Airplanes in Europe")
    st.markdown("Live dashboard showing how many planes are currently in European airspace.")
    st.markdown("---")

    auto_refresh = st.sidebar.checkbox("Enable Auto Refresh", value=True)
    refresh_interval = st.sidebar.slider("Update interval (sec)", 5, 60, 5)

    data_source = DataSource()
    chart_creator = ChartCreator()

    status_container = st.empty()
    metrics_container = st.empty()
    chart_container = st.empty()
    table_container = st.empty()

    history = pd.DataFrame(columns=["time", "count"])
    update_count = 0

    while auto_refresh:
        update_count += 1

        with status_container.container():
            st.info(f"🔄 Getting fresh data... (Update #{update_count})")

        new_data = data_source.get_planes_in_europe()
        if not new_data.empty:
            history = pd.concat([history, new_data], ignore_index=True)

            latest_record = new_data.iloc[0]

            with status_container.container():
                st.success(f"✅ Data updated at {latest_record['time'].strftime('%H:%M:%S')}")

            with metrics_container.container():
                chart_creator.create_summary_metrics(latest_record, update_count)

            with chart_container.container():
                fig = chart_creator.create_line_chart(history)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)

            with table_container.container():
                with st.expander("📊 View Raw Data"):
                    st.dataframe(history.tail(10))

        else:
            st.error("⚠️ Could not fetch data from OpenSky API")

        time.sleep(refresh_interval)

if __name__ == "__main__":
    main()
