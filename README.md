🌍 How The World Changes
A Global Data Visualization Platform

🔗 Live App: https://worldvisual.streamlit.app

📖 Introduction

Human civilization has changed dramatically over the past decades — economies grew, populations expanded, energy sources shifted, the digital era emerged, and environmental impacts increased. Understanding this evolution requires not just data, but meaningful visualization.

How The World Changes is an interactive Streamlit application designed to visualize historical global datasets and help users explore how countries evolved across various indicators. Through animated maps and scatter visualizations, the platform brings static data to life.

🎯 Purpose of the Project

Transform raw datasets into meaningful visual stories

Compare development progress between countries and regions

Identify historical patterns, global turning points, and growth trajectories

Support research, education, and presentations with interactive visuals

Encourage data-driven thinking about how humanity has shaped the world

📚 Indicators Included

The platform integrates multiple global indicators, including:

Category	Datasets
Population & Society	Population, Life Expectancy, Fertility Rate
Economy	GDP per Capita, Inflation
Environment & Climate	CO₂ consumption
Energy	Oil, Coal, Natural Gas, Hydro Power, Nuclear Power, Electricity Generation
Technology	Internet Users

All datasets are structured in standardized .xlsx format for consistency and reusability.

📊 Available Visualization Types
Visualization Type	Animation         Support	                               Description
🌐 Animated Choropleth Map	         ✔ Yes	          Compare global distribution of a metric over time on an interactive world map
🔵 Animated Scatter Plot	         ✔ Yes	          Observe relationships between variables such as income, population, emissions, etc., with time-based motion
📈 Line Graph	                    Static            Only Show historical progress or decline of selected indicators across time

✨ Users can filter by year, country, or indicator depending on the visualization mode.

🧩 App Capabilities

Explore global datasets spanning multiple decades

View time-based animated transformations

Compare multiple countries on the same scale

Identify global shifts such as:

Rise of internet adoption

Decline in fertility rates

Transition in energy sources

Population explosions

Economic growth patterns

📁 Project Layout
📦 How-The-World-Changes
 ┣ 📂 datasets
 ┣ 📂 pages
 ┣ 📂 static
 ┣ Home.py
 ┣ requirements.txt
 ┗ README.md

🛠 Technologies Used
Component	Technology
Language	Python
Framework	Streamlit
Visualization	Plotly Express
Deployment	Streamlit Community Cloud
Data Format	.xlsx
🚀 Running Locally
git clone <repo-url>
cd How-The-World-Changes
pip install -r requirements.txt
streamlit run Home.py

🔮 Planned Features
Feature	Status
Data comparison between two countries	⏳ Planned
Prediction using machine learning	⏳ Planned
PDF report export	⏳ Planned
Dataset correlations dashboard	⏳ Planned
👤 Author

📌 Gaurav Agrawal,📌 Achintya Mishra,📌 Arnav Kohli,📌 Dhanvin Ambavkar,📌 Eeshaan Suryanwanshi,📌 Ayaan Lone

🏷 License

This project is open for educational and research use. Enhancements, forks, and collaboration are welcome with attribution.

⭐ Support the Project

If you found this project helpful, consider giving it a ⭐ on GitHub (when available) and sharing the live app:

👉 https://worldvisual.streamlit.app