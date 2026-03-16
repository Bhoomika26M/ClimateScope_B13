import streamlit as st
import pandas as pd
import plotly.express as px

# Setting up the page layout
st.set_page_config(page_title="Global Weather Analytics", layout="wide")

@st.cache_data
def load_data():
    try:
        # UPDATED PATH: Pointing to the data folder
        df = pd.read_csv('data/GlobalWeatherRepository.csv')
        
        # Convert the date column to datetime objects
        df['last_updated'] = pd.to_datetime(df['last_updated'])
        
        # Map months to seasons for better analysis
        df['Season'] = df['last_updated'].dt.month.map({
            3:'Summer', 4:'Summer', 5:'Summer',
            6:'Monsoon', 7:'Monsoon', 8:'Monsoon', 9:'Monsoon',
            10:'Autumn', 11:'Autumn',
            12:'Winter', 1:'Winter', 2:'Winter'
        }).fillna('Unknown')
        
        return df
    except Exception as e:
        return None

# Initializing data
df = load_data()

if df is not None:
    st.title("🌍 ClimateScope: Full Analytics Report")
    st.markdown("---")
    
    # Sidebar filters for user interaction
    st.sidebar.header("🧭 Navigation & Filters")
    
    # Metric selection
    metric = st.sidebar.selectbox("Select Metric", ["temperature_celsius", "humidity", "wind_mph", "precip_mm"])
    
    # Country selection filter
    countries = st.sidebar.multiselect("Select Countries", 
                                       options=df['country'].unique(), 
                                       default=df['country'].unique()[:10])
    
    # Filtering the dataframe based on selection
    f_df = df[df['country'].isin(countries)]

    # Section 1: Visual Performance Trends
    st.header("📊 Performance & Trends")
    c1, c2 = st.columns(2)
    
    with c1:
        st.plotly_chart(px.bar(f_df, x='country', y=metric, color='Season', barmode='group', 
                               title="Regional Bar Comparison"), use_container_width=True)
        st.plotly_chart(px.line(f_df, x='last_updated', y=metric, color='country', 
                                title="Time-Series Trend"), use_container_width=True)
    
    with c2:
        st.plotly_chart(px.pie(f_df, names='country', values=metric, hole=0.4, 
                               title="Regional Distribution"), use_container_width=True)
        st.plotly_chart(px.area(f_df, x='last_updated', y=metric, color='country', 
                                title="Cumulative Growth Plot"), use_container_width=True)

    # Section 2: Global Maps
    st.header("🌎 Global Geospatial Analysis")
    st.plotly_chart(px.choropleth(f_df, locations="country", locationmode='country names', 
                                  color=metric, color_continuous_scale="Viridis", 
                                  title="Global Choropleth Map"), use_container_width=True)
    
    c3, c4 = st.columns(2)
    with c3:
        st.plotly_chart(px.scatter_geo(f_df, locations="country", locationmode='country names', 
                                       size=metric, color="country", title="Regional Bubble Map"), 
                                       use_container_width=True)
    with c4:
        st.plotly_chart(px.sunburst(f_df, path=['country', 'Season'], values=metric, 
                                    title="Hierarchical Breakdown"), use_container_width=True)

    # Data Preview Section
    st.markdown("---")
    st.subheader("📋 Dataset Preview")
    st.dataframe(f_df.head(15))

else:
    # UPDATED ERROR MESSAGE: More specific to your new folder
    st.error("CSV File not found in 'data/' folder. Please check your folder structure.")