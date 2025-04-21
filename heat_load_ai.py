
import streamlit as st

st.set_page_config(page_title="AI Heat Load Estimator", layout="centered")

st.title("🌡️ AI Heat Load Estimator")
st.markdown("Estimate cooling load based on simple room descriptions, including humidity (latent heat).")

description = st.text_area("Describe the space", placeholder="e.g. 6x4m room, brick walls, tin roof, 3 windows, 2 people, 2 computers, Broome WA")

if st.button("Estimate Heat Load"):
    if not description.strip():
        st.warning("Please enter a room description.")
    else:
        # Basic assumptions
        base_load = 1.2  # base load in kW for shell (walls/roof)
        per_person = 0.2  # sensible heat in kW per person
        per_device = 0.15  # equipment heat in kW per computer/device
        latent_per_person = 0.06  # latent (humidity) load per person in kW

        # Rough parsing (not NLP-based, just keyword count)
        num_people = description.lower().count("person") + description.lower().count("people")
        num_computers = description.lower().count("computer") + description.lower().count("laptop")

        # Estimate values
        sensible = base_load + (num_people * per_person) + (num_computers * per_device)
        latent = num_people * latent_per_person
        total = sensible + latent

        st.success(f"Estimated Total Cooling Load: **{total:.2f} kW**")
        st.markdown("**Breakdown:**")
        st.markdown(f"- Sensible Load (walls, people, equipment): **{sensible:.2f} kW**")
        st.markdown(f"- Latent Load (humidity): **{latent:.2f} kW**")
        st.caption("Estimates are approximate and assume warm, humid climate (e.g. coastal WA).")
