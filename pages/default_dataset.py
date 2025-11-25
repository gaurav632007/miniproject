import streamlit as st
import pandas as pd
import plotly.express as px
import os 

st.set_page_config(
    page_title="Home",
    layout="centered"
)


DATASET_DIR = "datasets"

def melt_years(df, country_col, value_name="Value"):
    df = df.copy()
    year_cols = [c for c in df.columns if isinstance(c, str) and c.isdigit()]
    long_df = df.melt(
        id_vars=[country_col],
        value_vars=year_cols,
        var_name="Year",
        value_name=value_name
    )
    long_df.rename(columns={country_col: "Country"}, inplace=True)
    long_df["Year"] = pd.to_numeric(long_df["Year"], errors="coerce")
    long_df[value_name] = pd.to_numeric(long_df[value_name], errors="coerce")
    long_df = long_df.dropna(subset=["Year", value_name, "Country"])
    return long_df


def load_temperature():
    df = pd.read_csv(os.path.join(DATASET_DIR, "all countries global temperature.csv"))
    long_df = melt_years(df, "Country Name", "TempChange")
    long_df.rename(columns={"TempChange": "Value"}, inplace=True)
    return long_df, "Temperature change (°C)"

def load_internet_usage_wide():
    df = pd.read_csv(os.path.join(DATASET_DIR, "internet_usage.csv"))
    long_df = melt_years(df, "Country Name", "InternetPercent")
    long_df.rename(columns={"InternetPercent": "Value"}, inplace=True)
    return long_df, "Internet users (%)"

def load_gdp():
    df = pd.read_csv(os.path.join(DATASET_DIR, "Countries GDP 1960-2020.csv"))
    long_df = melt_years(df, "Country Name", "GDP")
    long_df.rename(columns={"GDP": "Value"}, inplace=True)
    return long_df, "GDP (US$)"


def load_co2():
    df = pd.read_csv(os.path.join(DATASET_DIR, "co2_production.csv"))

    # Rename co2_prod_YYYY → YYYY so melt_years can detect year columns
    year_cols_map = {
        c: c.replace("co2_prod_", "")
        for c in df.columns
        if isinstance(c, str) and c.startswith("co2_prod_")
    }
    df = df.rename(columns=year_cols_map)

    # Convert wide → long
    long_df = melt_years(df, "Country", "CO2")
    long_df.rename(columns={"CO2": "Value"}, inplace=True)

    return long_df, "CO₂ emissions (Mt)"

# Refugee dataset: correct columns + convert Value to numeric
def load_refugees():
    df = pd.read_csv(
        os.path.join(DATASET_DIR, "Global-Refugee-Dataset-1951-2015.csv"),
        low_memory=False
    )

    df = df.rename(columns={
        "Country / territory of asylum/residence": "Country",
        "Refugees (incl. refugee-like situations)": "Value"
    })

    # Convert strings with commas to numeric
    df["Value"] = df["Value"].replace({',': ''}, regex=True)
    df["Value"] = pd.to_numeric(df["Value"], errors="coerce")

    return df[["Country", "Year", "Value"]].dropna(), "Refugee population"

# Deaths – compute total from all cause columns
def load_causes_of_death():
    df = pd.read_csv(os.path.join(DATASET_DIR, "cause_of_deaths.csv"))

    df = df.rename(columns={"Country/Territory": "Country"})

    ignore_cols = ["Country", "Code", "Year"]
    cause_cols = [c for c in df.columns if c not in ignore_cols]

    # Sum deaths from all listed causes
    df["Value"] = df[cause_cols].sum(axis=1)

    return df[["Country", "Year", "Value"]].dropna(), "Deaths (All causes)"

# Population – simple rename
def load_population_total():
    df = pd.read_csv(os.path.join(DATASET_DIR, "PopulationByAgeSex.csv"))
    df = df.rename(columns={
        "Location": "Country",
        "Time": "Year",
        "PopTotal": "Value"
    })
    return df[["Country", "Year", "Value"]].dropna(), "Population (millions)"

def load_population_migration():
    df = pd.read_csv(os.path.join(DATASET_DIR, "world_pop_mig_186_countries.csv"))
    df = df.rename(columns={"country": "Country", "year": "Year", "netMigration": "Value"})
    return df[["Country", "Year", "Value"]].dropna(), "Net migration"

def load_digital_connectivity():
    df = pd.read_csv(os.path.join(DATASET_DIR, "Final.csv"))
    df = df.rename(columns={"Entity": "Country", "Internet Users(%)": "Value"})
    return df[["Country", "Year", "Value"]].dropna(), "Internet users (%) (alt)"

DATASET_DIR = "datasets"


# List of datasets in UI
DATASETS = {
    "🌡️ Temperature Change": load_temperature,
    "📶 Internet Usage Wide": load_internet_usage_wide,
    "💰 GDP": load_gdp,
    "🌫️ CO₂ Emission": load_co2,
    "⚰️ Deaths": load_causes_of_death,
    "🧳 Refugees": load_refugees,
    "👥 Population": load_population_total,
    "🚶 Migration": load_population_migration,
    "🌐 Internet Users Final": load_digital_connectivity,
}

COLOR_MAPS = ["Viridis", "Plasma", "Cividis", "Turbo", "Inferno"]


#sidebar 
st.sidebar.header("⚙️ Controls")

dataset_label = st.sidebar.selectbox("Choose Dataset", list(DATASETS.keys()))
df, unit = DATASETS[dataset_label]()

years = sorted(df["Year"].unique())
selected_year = st.sidebar.selectbox("Year", years)

# New: visualisation type (map / bar / scatter / line)
viz_type = st.sidebar.radio(
    "Visualisation Type",
    ["🗺️ Map", "📊 Bar Chart", "⭕ Scatter Plot", "📈 Line Chart"]
)

display_mode = st.sidebar.radio("Display Mode", ["🧊 Static", "🎞️ Animated"])
colormap = st.sidebar.selectbox("Colour Style", COLOR_MAPS)

st.sidebar.markdown("**Unit:** " + unit)

# Filter data for selected year
year_df = df[df["Year"] == selected_year].dropna()

# ==============================================
# MAIN CONTENT
# ==============================================
left, right = st.columns([3, 1])

with left:
    # 🗺️ MAP
    if viz_type == "🗺️ Map":
        if display_mode == "🧊 Static":
            fig = px.choropleth(
                year_df,
                locations="Country",
                locationmode="country names",
                color="Value",
                color_continuous_scale=colormap,
                hover_name="Country",
                title=f"{dataset_label} – {selected_year}"
            )
        else:
            fig = px.choropleth(
                df.sort_values("Year"),
                locations="Country",
                locationmode="country names",
                animation_frame="Year",
                color="Value",
                color_continuous_scale=colormap,
                title=f"Animated – {dataset_label}"
            )
        st.plotly_chart(fig, use_container_width=True)

    # 📊 BAR CHART
    elif viz_type == "📊 Bar Chart":
        if display_mode == "🧊 Static":
            bar_data = year_df.sort_values("Value", ascending=False).head(30)
            fig = px.bar(
                bar_data,
                x="Country",
                y="Value",
                title=f"{dataset_label} – Top countries ({selected_year})"
            )
        else:
            bar_data = df.sort_values(["Year", "Value"], ascending=[True, False])
            fig = px.bar(
                bar_data,
                x="Country",
                y="Value",
                animation_frame="Year",
                title=f"Animated Bar Chart – {dataset_label}"
            )
        st.plotly_chart(fig, use_container_width=True)

    # ⭕ SCATTER PLOT
    elif viz_type == "⭕ Scatter Plot":
        if display_mode == "🧊 Static":
            # Scatter for selected year: Country vs Value
            fig = px.scatter(
                year_df,
                x="Country",
                y="Value",
                title=f"Scatter – {dataset_label} ({selected_year})",
                hover_name="Country"
            )
        else:
            # Animated scatter: Country vs Value over years
            fig = px.scatter(
                df,
                x="Country",
                y="Value",
                animation_frame="Year",
                title=f"Animated Scatter – {dataset_label}",
                hover_name="Country"
            )
        st.plotly_chart(fig, use_container_width=True)

    # 📈 LINE CHART
    elif viz_type == "📈 Line Chart":
        # To avoid too many lines, pick top 10 countries by value in selected year
        if not year_df.empty:
            top_countries = (
                year_df.sort_values("Value", ascending=False)
                .head(10)["Country"]
                .unique()
            )
            line_data = df[df["Country"].isin(top_countries)].sort_values("Year")
        else:
            line_data = df.sort_values("Year")

        fig = px.line(
            line_data,
            x="Year",
            y="Value",
            color="Country",
            title=f"Line Chart – {dataset_label} (Top countries)"
        )
        st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("### 🏆 Summary")
    if not year_df.empty:
        max_row = year_df.loc[year_df["Value"].idxmax()]
        min_row = year_df.loc[year_df["Value"].idxmin()]
        st.write(f"Highest: **{max_row['Country']}** ({max_row['Value']:.2f})")
        st.write(f"Lowest: **{min_row['Country']}** ({min_row['Value']:.2f})")
    else:
        st.write("No data available")

# Show raw data
with st.expander("📄 Raw Data"):
    st.dataframe(df.head(200))
