import streamlit as st

st.title("Python MCQs Quiz 📝")

# Question 1
question1 = st.radio("1. Which keyword is used to define a function in Python?", 
                     ("A) def", "B) func", "C) define", "D) function"))

if st.button("Next 1"):
    st.write("Proceed to the next question.")

# Question 2
question2 = st.radio("2. What will `print(type([]))` output?", 
                     ("A) <class 'list'>", "B) <class 'tuple'>", "C) <class 'dict'>", "D) <class 'set'>"))

if st.button("Next 2"):
    st.write("Proceed to the next question.")

# Question 3
question3 = st.radio("3. What is the output of `bool([])`?", 
                     ("A) True", "B) False", "C) None", "D) Error"))

if st.button("Next 3"):
    st.write("Proceed to the next question.")

# Question 4
question4 = st.radio("4. Which of the following is used to create an empty set?", 
                     ("A) {}", "B) set()", "C) []", "D) empty()"))

if st.button("Next 4"):
    st.write("Proceed to the next question.")

# Question 5
question5 = st.radio("5. What is the correct way to open a file in Python?", 
                     ("A) open('file.txt', 'r')", "B) file.open('file.txt')", "C) open('file.txt', 'read')", "D) read('file.txt')"))

if st.button("Next 5"):
    st.write("Proceed to the next question.")

# Question 6
question6 = st.radio("6. What does `len({'a': 1, 'b': 2, 'c': 3})` return?", 
                     ("A) 3", "B) 2", "C) 1", "D) 0"))

if st.button("Next 6"):
    st.write("Proceed to the next question.")

# Question 7
question7 = st.radio("7. Which of the following data types is immutable?", 
                     ("A) List", "B) Dictionary", "C) Set", "D) Tuple"))

if st.button("Next 7"):
    st.write("Proceed to the next question.")

# Question 8
question8 = st.radio("8. What will `print(2 ** 3)` output?", 
                     ("A) 5", "B) 6", "C) 8", "D) 9"))

if st.button("Next 8"):
    st.write("Proceed to the next question.")

# Question 9
question9 = st.radio("9. How do you convert a string into a list?", 
                     ("A) list('hello')", "B) str('hello')", "C) tuple('hello')", "D) dict('hello')"))

if st.button("Next 9"):
    st.write("Proceed to the next question.")

# Question 10
question10 = st.radio("10. What is the output of `print(10 // 3)`?", 
                      ("A) 3", "B) 3.33", "C) 3.0", "D) 4"))

if st.button("Submit"):
    st.write("Quiz submitted! 🎉")
