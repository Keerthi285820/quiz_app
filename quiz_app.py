import streamlit as st

# Page setup
st.set_page_config(page_title="Quiz App", page_icon="🧠")

st.title("🧠 Multiple Choice Quiz App")
st.subheader("Answer all the questions below:")

# ✅ Quiz Questions List – Add as many as you like!
quiz_data = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Computer Personal Unit", "Central Processing Unit", "Control Process Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which is the smallest prime number?",
        "options": ["1", "2", "3", "0"],
        "answer": "2"
    },
    {
        "question": "HTML is used to?",
        "options": ["Design websites", "Make coffee", "Send emails", "Play videos"],
        "answer": "Design websites"
    },
    {
        "question": "Which language is primarily used for Android app development?",
        "options": ["Python", "Java", "C#", "Swift"],
        "answer": "Java"
    },
    {
        "question": "How many continents are there?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["Amazon", "Nile", "Ganga", "Yangtze"],
        "answer": "Nile"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Gold", "Oxygen", "Osmium", "Oxide"],
        "answer": "Oxygen"
    },
    {
        "question": "Which sport uses the term 'Love'?",
        "options": ["Cricket", "Tennis", "Football", "Basketball"],
        "answer": "Tennis"
    }
]

# Score tracking
score = 0
user_answers = []

# Display each question and collect answers
for idx, q in enumerate(quiz_data):
    st.markdown(f"**Q{idx + 1}: {q['question']}**")
    selected = st.radio("Choose one:", q["options"], key=idx)
    user_answers.append(selected)

# Submit button
if st.button("Submit Quiz"):
    for i, q in enumerate(quiz_data):
        if user_answers[i] == q["answer"]:
            score += 1

    st.success(f"✅ You scored **{score} out of {len(quiz_data)}**")
    
    # Optional: show right/wrong answer feedback
    st.markdown("---")
    st.markdown("### 📊 Review Answers:")
    for i, q in enumerate(quiz_data):
        if user_answers[i] == q["answer"]:
            st.markdown(f"✅ **Q{i+1}: Correct** – {q['question']}")
        else:
            st.markdown(f"❌ **Q{i+1}: Incorrect** – {q['question']}<br>"
                        f"Your answer: *{user_answers[i]}*<br>"
                        f"Correct answer: **{q['answer']}**", unsafe_allow_html=True)

    if score == len(quiz_data):
        st.balloons()
