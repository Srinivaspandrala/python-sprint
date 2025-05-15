# Install Streamlit
# pip install streamlit

import streamlit as st

# Initialize the session state for tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Function to add a task
def add_task():
    task = st.session_state.new_task
    if task:
        st.session_state.tasks.append(task)
        st.session_state.new_task = ""

# Function to delete a task
def delete_task(task):
    st.session_state.tasks.remove(task)

# Streamlit user interface
st.title("Todo List")

# Input field for new task
st.text_input("Add a new task:", key='new_task', on_change=add_task)

# Display the list of tasks
if st.session_state.tasks:
    st.write("### Your Tasks:")
    for task in st.session_state.tasks:
        col1, col2 = st.columns([8, 1])
        with col1:
            st.write(task)
        with col2:
            if st.button("Delete", key=task):
                delete_task(task)
else:
    st.write("No tasks yet! Add a task above.")
