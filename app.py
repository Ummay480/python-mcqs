import streamlit as st

st.title("Python MCQs Quiz 📝")

# Store correct answers
correct_answers = {
    "q1": "A) def",
    "q2": "A) <class 'list'>",
    "q3": "B) False",
    "q4": "B) set()",
    "q5": "A) open('file.txt', 'r')",
    "q6": "A) 3",
    "q7": "D) Tuple",
    "q8": "C) 8",
    "q9": "A) list('hello')",
    "q10": "A) 3"
}

# User answers
user_answers = {}

# Function to check answers and display feedback
def check_answer(q_key, question, options):
    user_answers[q_key] = st.radio(question, options)
    if st.button(f"Check {q_key}"):
        if user_answers[q_key] == correct_answers[q_key]:
            st.success("✅ Correct!")
        else:
            st.error("❌ Wrong! The correct answer is: " + correct_answers[q_key])

# Questions
check_answer("q1", "1. Which keyword is used to define a function in Python?", 
             ("A) def", "B) func", "C) define", "D) function"))
check_answer("q2", "2. What will `print(type([]))` output?", 
             ("A) <class 'list'>", "B) <class 'tuple'>", "C) <class 'dict'>", "D) <class 'set'>"))
check_answer("q3", "3. What is the output of `bool([])`?", 
             ("A) True", "B) False", "C) None", "D) Error"))
check_answer("q4", "4. Which of the following is used to create an empty set?", 
             ("A) {}", "B) set()", "C) []", "D) empty()"))
check_answer("q5", "5. What is the correct way to open a file in Python?", 
             ("A) open('file.txt', 'r')", "B) file.open('file.txt')", "C) open('file.txt', 'read')", "D) read('file.txt')"))
check_answer("q6", "6. What does `len({'a': 1, 'b': 2, 'c': 3})` return?", 
             ("A) 3", "B) 2", "C) 1", "D) 0"))
check_answer("q7", "7. Which of the following data types is immutable?", 
             ("A) List", "B) Dictionary", "C) Set", "D) Tuple"))
check_answer("q8", "8. What will `print(2 ** 3)` output?", 
             ("A) 5", "B) 6", "C) 8", "D) 9"))
check_answer("q9", "9. How do you convert a string into a list?", 
             ("A) list('hello')", "B) str('hello')", "C) tuple('hello')", "D) dict('hello')"))
check_answer("q10", "10. What is the output of `print(10 // 3)`?", 
             ("A) 3", "B) 3.33", "C) 3.0", "D) 4"))

# Display all answers after submission
if st.button("Submit Quiz"):
    st.subheader("📋 Quiz Results:")
    for key, answer in correct_answers.items():
        st.write(f"**{key.upper()}**: ✅ Correct Answer: {answer}")
