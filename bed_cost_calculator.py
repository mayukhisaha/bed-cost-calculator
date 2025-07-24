import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------
# Data Setup
# --------------------------
data = {
    "Care Type": ["General Ward", "Emergency Ward"],
    "NHS Cost Per Night": [18.94, 40.00],
    "Darwin Cost Per Night": [80.00, 80.00]
}
df = pd.DataFrame(data)

# --------------------------
# Streamlit App
# --------------------------
st.set_page_config(page_title="NHS vs Darwin Bed Cost Calculator", layout="centered")

st.title("NHS vs Darwin Bed Cost Calculator")
st.markdown("Estimate and compare the cost per bed per night between traditional NHS facilities and Darwin Group modular solutions.")

# --------------------------
# User Inputs
# --------------------------
care_type = st.selectbox("Select Ward Type", df["Care Type"].unique())
num_beds = st.number_input("Number of Beds", min_value=1, max_value=100, value=10)
num_nights = st.number_input("Number of Nights", min_value=1, max_value=365, value=30)

# --------------------------
# Get Costs
# --------------------------
selected_row = df[df["Care Type"] == care_type].iloc[0]
nhs_cost_per_night = selected_row["NHS Cost Per Night"]
darwin_cost_per_night = selected_row["Darwin Cost Per Night"]

# --------------------------
# Calculations
# --------------------------
total_nhs = nhs_cost_per_night * num_beds * num_nights
total_darwin = darwin_cost_per_night * num_beds * num_nights
savings = total_nhs - total_darwin

# --------------------------
# Display Metrics
# --------------------------
col1, col2, col3 = st.columns(3)
col1.metric("NHS Total Cost", f"£{total_nhs:,.2f}")
col2.metric("Darwin Total Cost", f"£{total_darwin:,.2f}")
col3.metric("Estimated Savings", f"£{abs(savings):,.2f}", delta=f"{'-' if savings > 0 else '+'}{abs(savings):,.2f}")

# --------------------------
# Visual Comparison
# --------------------------
st.subheader("Cost Comparison Chart")
fig, ax = plt.subplots()
bars = ax.bar(["NHS", "Darwin"], [total_nhs, total_darwin], color=["#1f77b4", "#2ca02c"])
ax.set_ylabel("Total Cost (£)")
ax.set_title(f"Total Cost Comparison for {care_type}")
st.pyplot(fig)

# --------------------------
# Footer
# --------------------------
st.markdown("---")
st.markdown(
    "**Data Sources:** NHS Estates (ERIC reports), King’s Fund, and Darwin Group documentation. "
    "Costs include capital + maintenance for NHS, and modular hire cost for Darwin (5-year lease)."
)
