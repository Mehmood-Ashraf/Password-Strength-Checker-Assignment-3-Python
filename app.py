import streamlit as st
# Regular Expression
import re
import random


# Function for Check Password Strength
# This function will return a Password dtrength value
def check_password_strength(password):
    # All variables will return boolean value True or False
    length = len(password) >= 8 
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    number = bool(re.search(r'[0-9]', password)) # we can use also "\d" for check numbers [0-9]
    special_character = bool(re.search(r"[!@#$%^&*]", password))

    # Sum method for sum the value of list password_strength will return sum of list True = 1 and False = 0; 
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

if user_password not in st.session_state.password_history:
    st.session_state.password_history.append(user_password)



show_history = st.checkbox("Password History")

if show_history:
    st.subheader("Password History")
    for password in st.session_state.password_history[::-1]: # [:: -1] for reverse the list (Last wali value pehle aayegi)
        st.write(password)


def generate_password(length, numbers, special_characters, uppercase, lowercase):
    num_characters = "0123456789"
    special_character_set = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"
    lower_alphabets = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    characters = ""
    if numbers:
        characters += num_characters
    if special_characters:
        characters += special_character_set
    if uppercase:
        characters += upper_alphabets
    if lowercase:
        characters += lower_alphabets
    
    if not characters:
        return "Please select atleast one character set."
    
    return "".join(random.choice(characters) for _ in range(length))

password_generator = st.checkbox("Password Generator")

if password_generator:
    st.title("Password Generator")
    length = st.slider("Total Password Length:", min_value=8, max_value=20, value=8)
    numbers = st.checkbox("Include Numbers")
    special_characters = st.checkbox("Include Special Characters")
    uppercase = st.checkbox("Include Uppercase Characters")
    lowercase = st.checkbox("Include Lowercase Characters")

if st.button("Generate Password"):
    password = generate_password(length, numbers, special_characters, uppercase, lowercase)
    st.text_input("Generated Password: ", password, type = "default")