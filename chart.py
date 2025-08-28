import plotly.express as px
import streamlit as st

class ChartCreator:
    def create_line_chart(self, history):
        """Time line chart for aeroplanes"""
        if history.empty:
            return None
        
        fig = px.line(
            history,
            x="time",
            y="count",
            markers=True,
            template="plotly_dark",
            title="✈️ Airplanes in Europe (real-time)"
        )
        fig.update_layout(
            xaxis_title="Time",
            yaxis_title="Number of planes",
            height=500
        )
        return fig

    def create_summary_metrics(self, latest_record, total_updates):
        """It will show the most recent values and update them"""
        if latest_record is None:
            return

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                label="Planes in Europe",
                value=latest_record["count"]
            )

        with col2:
            st.metric(
                label="Last Update",
                value=latest_record["time"].strftime("%H:%M:%S")
            )

        with col3:
            st.metric(
                label="Total Updates",
                value=total_updates
            )
