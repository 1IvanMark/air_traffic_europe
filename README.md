# air_traffic_europe
This interactive Streamlit application provides a real-time overview of air traffic across European airspace, giving users valuable insights into the number of airplanes currently flying over the region. Leveraging live data from the OpenSky Network API, the app tracks aircraft positions within a predefined bounding box that broadly covers Europe (latitudes 35°–70°, longitudes -10°–40°).

The dashboard is designed with both usability and functionality in mind. Upon launching, it displays the current number of planes in European skies, updates automatically at user-defined intervals, and keeps a history of flight counts that can be visualized through interactive line charts powered by Plotly. These charts show how the number of planes changes over time, making it easy to observe fluctuations in traffic patterns, peak hours, and potential anomalies.

Key features include:

Live tracking of airplane counts in Europe, updated every few seconds (configurable).

Custom auto-refresh settings in the sidebar, allowing users to define update intervals.

Interactive line chart that visualizes real-time changes in air traffic, providing both clarity and depth.

Summary metrics displaying the latest airplane count, timestamp of the last update, and total number of refresh cycles performed since startup.

Expandable raw data table, enabling users to inspect the most recent historical records of air traffic updates.

This app demonstrates the power of combining Streamlit for rapid dashboard development, requests for API integration, pandas for data handling, and Plotly for rich visualizations. It can be used for aviation enthusiasts, researchers, or data scientists who want to monitor, analyze, or showcase real-time flight activity in Europe.

With its clean layout, dark theme visualization, and responsive update cycle, the dashboard provides a compelling live monitoring experience that bridges raw aviation data with intuitive visual analytics. Whether for personal curiosity, academic study, or professional demonstration, this tool offers a simple yet powerful way to explore European airspace in real time.
