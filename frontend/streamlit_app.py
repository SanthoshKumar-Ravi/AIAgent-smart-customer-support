import streamlit as st
import requests

st.title("💬 Smart Customer Support")

# Initialize session state variables
if "query_id" not in st.session_state:
    st.session_state.query_id = None
if "answer" not in st.session_state:
    st.session_state.answer = ""

query = st.text_input("Ask a question")

# Submit button for the question
if st.button("Submit"):
    if query.strip():
        response = requests.post("http://localhost:8000/query/", json={"question": query})
        data = response.json()
        st.session_state.query_id = data["query_id"]
        st.session_state.answer = data["answer"]
    else:
        st.warning("Please enter a question.")

# Show answer if available
if st.session_state.query_id:
    st.write("**Answer:**", st.session_state.answer)

    st.subheader("Provide Feedback")
    rating = st.slider("Rate the response", 1, 5, key="rating_slider")
    comment = st.text_area("Leave a comment", key="comment_box")

    # Separate button to submit feedback
    if st.button("Submit Feedback"):
        feedback_data = {
            "query_id": st.session_state.query_id,
            "rating": rating,
            "comment": comment
        }
        feedback_response = requests.post("http://localhost:8000/feedback/", json=feedback_data)
        if feedback_response.status_code == 200:
            st.success("✅ Feedback submitted!")
        else:
            st.error("❌ Failed to submit feedback.")
