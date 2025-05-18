import streamlit as st

st.set_page_config(page_title="Quiz App", page_icon="🧠")

st.title("🧠 Multiple Choice Quiz")
st.subheader("Answer the questions below:")

# Define quiz questions and options
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used to build Streamlit apps?",
        "options": ["Java", "Python", "C++", "JavaScript"],
        "answer": "Python"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    }
]

score = 0

user_answers = []

# Go through questions one by one
for i, q in enumerate(quiz):
    st.markdown(f"**Q{i+1}: {q['question']}**")
    selected = st.radio(
        "Choose one:",
        q['options'],
        key=f"q{i}"
    )
    user_answers.append(selected)

# Submit button
if st.button("Submit Quiz"):
    for i, q in enumerate(quiz):
        if user_answers[i] == q["answer"]:
            score += 1

    st.success(f"✅ You scored {score} out of {len(quiz)}")

    if score == len(quiz):
        st.balloons()
