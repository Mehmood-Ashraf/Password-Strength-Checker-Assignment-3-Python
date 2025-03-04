import streamlit as st
import re


def check_password_strength(password):
    length = len(password) >= 8
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    number = bool(re.search(r'[0-9]', password))
    special_character = bool(re.search(r"[!@#$%^&*]", password))

    password_strength = sum([length, uppercase, lowercase, number, special_character])

    if password_strength == 5:
        return "Very Strong"
    elif password_strength == 4:
        return "Strong"
    elif password_strength == 3:
        return "Medium"
    elif password_strength == 2:
        return "Weak"
    else:
        return "Very Weak"
    

if "password_history" not in st.session_state:
    st.session_state.password_history = []
    

st.title("🔐 Password Strength Meter")

user_password = st.text_input("Enter your password", type="password")


if user_password:
    strength = check_password_strength(user_password)
    st.subheader(f"Password Strength: {strength}")

if "user_password" not in st.session_state.password_history:
    st.session_state.password_history.append(user_password)

st.session_state.password_input = ""

show_history = st.checkbox("Password History")

if show_history:
    st.subheader("Password History")
    for password in st.session_state.password_history[::-1]: # [:: -1] for reverse the list (Last wali value pehle aayegi)
        st.write(password)