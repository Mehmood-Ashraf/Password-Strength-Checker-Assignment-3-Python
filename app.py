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
    


st.title("🔐 Password Strength Meter")

user_password = st.text_input("Enter your password", type="password")


if user_password:
    strength = check_password_strength(user_password)
    st.subheader(f"Password Strength: {strength}")
