import streamlit as st

# Apply custom CSS for background and styling
def apply_custom_style():
    st.markdown("""
        <style>
        body {
            background-color: #f0f2f6;
            background-image: url("https://images.unsplash.com/photo-1581093588401-22b0d53df543?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
            background-size: cover;
            background-position: center;
        }
        .main {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 12px;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_style()

# Page Configuration
st.set_page_config(page_title="DOCGUIDE", layout="wide")

# Sidebar
st.sidebar.title("📘 DOCGUIDE")
st.sidebar.markdown("""
This tool helps you track your **essential documents** and gives step-by-step instructions to apply for missing ones.

✅ Aadhaar  
✅ PAN  
✅ Driving License  
✅ Passport  
✅ Birth Certificate  
✅ Voter ID  
""")

# Main content inside a styled container
with st.container():
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.title("📄 DOCGUIDE")
    st.subheader("📋 Essential Document Checklist")

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

    selected = {}
    for doc in doc_links:
        selected[doc] = st.checkbox(f"✅ {doc}")

    if st.button("🔍 Check My Status"):
        missing = [doc for doc, have in selected.items() if not have]

        if not missing:
            st.success("🎉 You have all essential documents! No action needed.")
        else:
            st.warning("⚠️ Missing Documents Found:")
            for doc in missing:
                st.markdown(f"### 📌 {doc}")
                for i, step in enumerate(doc_links[doc]["steps"]):
                    st.markdown(f"{i+1}. {step}")
                st.markdown(f"[🌐 Apply Here]({doc_links[doc]['link']})", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


