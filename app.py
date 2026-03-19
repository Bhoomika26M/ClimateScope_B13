import streamlit as st
import pandas as pd
import plotly.express as px

# 1. PAGE SETUP
st.set_page_config(page_title="ClimateScope Pro | Milestone 3", layout="wide")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- 🔐 LOGIN PAGE (Modern Cyan & Navy Style) ---
def show_login_page():
    st.markdown("""
        <style>
        .stApp {
            background-color: #0F172A;
        }
        .login-box {
            max-width: 400px;
            margin: auto;
            padding: 40px;
            border-radius: 20px;
            background: #1E293B; 
            box-shadow: 0px 15px 35px rgba(0,0,0,0.4);
            text-align: center;
            border: 1px solid #38BDF8;
        }
        .logo-img {
            width: 80px;
            margin-bottom: 10px;
            display: block;
            margin-left: auto;
            margin-right: auto;
            filter: drop-shadow(0px 0px 5px #38BDF8);
        }
        h2 {
            color: #38BDF8 !important;
            font-family: 'Inter', sans-serif;
            font-weight: 700;
        }
        div.stButton > button {
            width: 100% !important;
            background: linear-gradient(135deg, #0EA5E9 0%, #2563EB 100%) !important;
            color: white !important;
            border: none !important;
            padding: 12px !important;
            border-radius: 8px !important;
            font-weight: bold !important;
            text-transform: uppercase;
            box-shadow: 0px 4px 15px rgba(37, 99, 235, 0.4) !important;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0px 6px 20px rgba(56, 189, 248, 0.6) !important;
            color: white !important;
        }
        label {
            color: #94A3B8 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)
    _, col2, _ = st.columns([1, 1.2, 1])

    with col2:
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)
        # ✅ FIXED LOGO
        st.markdown(
            '<img src="https://cdn-icons-png.flaticon.com/512/4052/4052984.png" class="logo-img">',
            unsafe_allow_html=True
        )
        st.markdown("<h2>ClimateScope</h2>", unsafe_allow_html=True)

        user_input = st.text_input("Username", placeholder="e.g. Swapna")
        pwd_input = st.text_input("Password", type="password", placeholder="••••••••")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("SIGN IN"):
            if user_input == "Swapna" and pwd_input == "123":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Invalid! (Hint: Swapna / 123)")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 📊 DASHBOARD (MILESTONE 3 UPDATED) ---
def show_dashboard():
    st.sidebar.markdown("<h2 style='color:#38BDF8;'>ClimateScope Pro</h2>", unsafe_allow_html=True)
    st.sidebar.write(f"👤 **Admin:** Swapna")

    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()

    try:
        # Load Data from Global Weather Repository
        df = pd.read_csv("data/GlobalWeatherRepository.csv")

        # --- 📍 ADVANCED FILTERS (Milestone 3 New Feature) ---
        st.sidebar.divider()
        st.sidebar.header("📍 Region & Climate Filters")
        
        # 1. Country Multiselect
        countries = sorted(df['country'].unique())
        selected_countries = st.sidebar.multiselect("Select Countries", countries, default=countries[:10])
        
        # 2. Temperature Slider (Milestone 3 Interactivity)
        min_temp = float(df['temperature_celsius'].min())
        max_temp = float(df['temperature_celsius'].max())
        temp_range = st.sidebar.slider("Temperature Range (°C)", min_temp, max_temp, (min_temp, max_temp))

        # Filter Logic
        filtered_df = df[
            (df['country'].isin(selected_countries)) & 
            (df['temperature_celsius'] >= temp_range[0]) & 
            (df['temperature_celsius'] <= temp_range[1])
        ]

        # --- 💡 LIVE INSIGHTS BOX (Milestone 3 Highlight) ---
        st.title("🌍 ClimateScope Intelligence")
        
        if not filtered_df.empty:
            hottest_row = filtered_df.loc[filtered_df['temperature_celsius'].idxmax()]
            st.info(f"✨ **Notable Finding:** Based on your filters, the hottest location is **{hottest_row['location_name']}, {hottest_row['country']}** at **{hottest_row['temperature_celsius']}°C**.")

        # --- 4 METRICS ---
        st.divider()
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("🌡️ Avg Temp", f"{filtered_df['temperature_celsius'].mean():.1f} °C")
        m2.metric("💧 Humidity", f"{filtered_df['humidity'].mean():.1f} %")
        m3.metric("🌬️ Max Wind", f"{filtered_df['wind_kph'].max():.1f} KPH")
        m4.metric("⏲️ Pressure", f"{filtered_df['pressure_mb'].mean():.0f} mb")
        st.divider()

        # --- 7 VISUALIZATIONS ---
        c1, c2 = st.columns([1.2, 0.8])
        with c1:
            st.plotly_chart(px.choropleth(filtered_df, locations="country", locationmode='country names', color="temperature_celsius", title="1. Global Heatmap", color_continuous_scale="Blues"), use_container_width=True)
        with c2:
            st.plotly_chart(px.pie(filtered_df, names='condition_text', hole=0.4, title="2. Weather Mix", color_discrete_sequence=px.colors.sequential.Blues_r), use_container_width=True)

        c3, c4 = st.columns(2)
        with c3:
            st.plotly_chart(px.bar(filtered_df.nlargest(10, 'temperature_celsius'), x='temperature_celsius', y='location_name', orientation='h', title="3. Hottest Spots", color_discrete_sequence=["#38BDF8"]), use_container_width=True)
        with c4:
            st.plotly_chart(px.scatter(filtered_df, x="temperature_celsius", y="humidity", color="condition_text", title="4. Correlation (Temp vs Humid)"), use_container_width=True)

        c5, c6, c7 = st.columns(3)
        with c5:
            st.plotly_chart(px.box(filtered_df, y="temperature_celsius", title="5. Temperature Outliers"), use_container_width=True)
        with c6:
            st.plotly_chart(px.histogram(filtered_df, x="wind_kph", title="6. Wind Distribution"), use_container_width=True)
        with c7:
            st.plotly_chart(px.sunburst(filtered_df.head(30), path=['country', 'location_name'], values='temperature_celsius', title="7. Regional Hierarchy"), use_container_width=True)

        # --- 📋 TABLE ACTIONS ---
        st.divider()
        st.subheader("📋 Data Preview & Action Center")
        st.dataframe(filtered_df.head(10), use_container_width=True)

        st.markdown("### 🛠️ Table Actions & Advanced Insights")
        col_act1, col_act2 = st.columns(2)

        with col_act1:
            st.warning(f"Total entries analyzed: **{len(filtered_df)}**")
            csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download This Report (CSV)",
                data=csv,
                file_name='climatescope_data.csv',
                mime='text/csv',
                use_container_width=True
            )

        with col_act2:
            st.success("Analysis Engine: Operational ✅")
            if st.button("🔄 Refresh Data View", use_container_width=True):
                st.rerun()

    except Exception as e:
        st.error(f"Error loading data: {e}. Please ensure 'data/GlobalWeatherRepository.csv' exists.")

# ROUTING
if st.session_state['logged_in']:
    show_dashboard()
else:
    show_login_page()