import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from password_strength import calculate_password_strength

st.set_page_config(page_title="Password Strength Analyzer", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Analyzer")
st.markdown("### Check how strong your password is!")

# --- User Input ---
password = st.text_input("Enter your password:", type="password")

if password:
    strength, feedback, entropy = calculate_password_strength(password)
    st.write(f"**Score:** {round(strength * 100)}%")
    st.write(f"**Entropy:** {entropy} bits")

    # Show strength color bar
    st.progress(strength)

    if strength < 0.4:
        st.error("Weak Password 🔴")
    elif strength < 0.8:
        st.warning("Moderate Password 🟡")
    else:
        st.success("Strong Password 🟢")

    if feedback:
        st.subheader("Suggestions to improve:")
        for tip in feedback:
            st.write(f"- {tip}")

# --- Batch Password Analysis ---
st.markdown("---")
st.subheader("📂 Analyze multiple passwords (Upload CSV file)")

uploaded_file = st.file_uploader("Upload a CSV file with a column named 'password'", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    results = []
    for pwd in df["password"]:
        strength, _, _ = calculate_password_strength(str(pwd))
        results.append(strength)
    df["strength_score"] = results

    st.write("### Password Strength Results")
    st.dataframe(df)

    # Plot distribution
    fig, ax = plt.subplots()
    ax.hist(df["strength_score"], bins=5, color="skyblue", edgecolor="black")
    ax.set_xlabel("Strength Score")
    ax.set_ylabel("Count")
    ax.set_title("Password Strength Distribution")
    st.pyplot(fig)

st.markdown("---")
st.caption("Made by Hitesh 💻 | Final Year Cyber Security Project")
