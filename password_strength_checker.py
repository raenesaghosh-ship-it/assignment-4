import streamlit as st
import re

# Page Configuration
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

# Application Title
st.title("🔐 Password Strength Checker")
st.write("Check your password strength and get suggestions to improve it.")

st.info("Use sample passwords for testing. Do not enter your personal passwords.")

# Password Input
password = st.text_input(
    "Enter a sample password:",
    type="password",
    placeholder="Enter password here"
)

# Check Password Strength
if password:
    # Password Criteria
    length_check = len(password) >= 8
    uppercase_check = bool(re.search(r"[A-Z]", password))
    lowercase_check = bool(re.search(r"[a-z]", password))
    number_check = bool(re.search(r"[0-9]", password))
    special_check = bool(re.search(r"[^A-Za-z0-9]", password))

    # Calculate Score
    score = sum([
        length_check,
        uppercase_check,
        lowercase_check,
        number_check,
        special_check
    ])

    # Determine Strength
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    # Display Results
    st.subheader("📊 Password Strength Analysis")

    st.markdown(
        f"### Password Strength: :{color}[{strength}]"
    )

    st.write(f"**Password Strength Score: {score}/5**")

    # Progress Bar
    st.progress(score / 5)

    # Criteria Checklist
    st.subheader("✅ Password Criteria Checklist")

    criteria = {
        "At least 8 characters": length_check,
        "Contains an uppercase letter (A-Z)": uppercase_check,
        "Contains a lowercase letter (a-z)": lowercase_check,
        "Contains a number (0-9)": number_check,
        "Contains a special character (!@#$%^&*)": special_check
    }

    for criterion, passed in criteria.items():
        if passed:
            st.success(f"✓ {criterion}")
        else:
            st.error(f"✗ {criterion}")

    # Suggestions for Improvement
    st.subheader("💡 Suggestions for Improvement")

    suggestions = []

    if not length_check:
        suggestions.append("Use at least 8 characters.")

    if not uppercase_check:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    if not lowercase_check:
        suggestions.append("Add at least one lowercase letter (a-z).")

    if not number_check:
        suggestions.append("Include at least one number (0-9).")

    if not special_check:
        suggestions.append(
            "Include at least one special character, such as !, @, #, or $."
        )

    if suggestions:
        for suggestion in suggestions:
            st.write(f"- {suggestion}")
    else:
        st.success("Excellent! Your password meets all five criteria.")

    # Final Message
    st.subheader("📝 Final Result")

    if strength == "Weak":
        st.warning(
            "Your password is weak. Follow the suggestions above to improve it."
        )
    elif strength == "Moderate":
        st.info(
            "Your password is moderately strong. Improve the missing criteria "
            "to make it stronger."
        )
    else:
        st.success(
            "Your password is strong according to all five specified criteria!"
        )

else:
    st.caption("Enter a sample password above to see the strength analysis.")