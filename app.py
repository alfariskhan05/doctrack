import streamlit as st

# Document data
doc_links = {
    "Aadhaar Card": {
        "steps": [
            "Visit the UIDAI website.",
            "Click on 'Book an Appointment' at Aadhaar Seva Kendra.",
            "Fill in your details and book a slot.",
            "Visit the center with valid documents.",
            "Complete biometric verification and get an acknowledgment receipt."
        ],
        "link": "https://uidai.gov.in/en/"
    },
    "PAN Card": {
        "steps": [
            "Go to the NSDL e-Gov or UTIITSL website.",
            "Select 'Apply for PAN' option.",
            "Fill in the online form with your details.",
            "Upload the necessary documents and pay the fee.",
            "Submit the application and track the status online."
        ],
        "link": "https://www.onlineservices.nsdl.com/paam/endUserRegisterContact.html"
    },
    "Driving License": {
        "steps": [
            "Visit the Parivahan website.",
            "Select 'Apply for Driving License'.",
            "Fill in the application form and upload documents.",
            "Book a slot for the driving test.",
            "Appear for the test and receive your DL upon passing."
        ],
        "link": "https://parivahan.gov.in/parivahan/"
    },
    "Passport": {
        "steps": [
            "Go to the Passport Seva website.",
            "Register and log in.",
            "Fill in the application form and schedule an appointment.",
            "Visit the Passport Seva Kendra with documents.",
            "Complete the verification process and track application status."
        ],
        "link": "https://portal2.passportindia.gov.in/"
    },
    "Birth Certificate": {
        "steps": [
            "Visit your state's official e-District website.",
            "Select 'Apply for Birth Certificate'.",
            "Fill in the application form and upload documents.",
            "Submit the form and pay applicable fees.",
            "Download the certificate after approval."
        ],
        "link": "https://crsorgi.gov.in/"
    },
    "Voter ID": {
        "steps": [
            "Go to the NVSP website.",
            "Click on 'Apply for New Voter ID'.",
            "Fill in Form 6 and upload required documents.",
            "Submit the application and track status online.",
            "Receive your Voter ID after verification."
        ],
        "link": "https://www.nvsp.in/"
    }
}

# Streamlit app
st.set_page_config(page_title="DOCGUIDE", layout="centered")

st.title("📄 DOCGUIDE")
st.subheader("✅ Document Checklist")

# Collect checkbox inputs
selected = {}
for doc in doc_links:
    selected[doc] = st.checkbox(doc)

# Submit button
if st.button("Check Status"):
    missing = [doc for doc, have in selected.items() if not have]

    if not missing:
        st.success("✅ You have all essential documents! No action needed.")
    else:
        st.error("❌ Missing Documents:")
        for doc in missing:
            st.markdown(f"### 📌 {doc}")
            for i, step in enumerate(doc_links[doc]["steps"]):
                st.markdown(f"{i+1}. {step}")
            st.markdown(f"[Apply Here]({doc_links[doc]['link']})\n")



