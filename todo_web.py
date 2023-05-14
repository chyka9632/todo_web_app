import streamlit as st
import todo_fnx as fn
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt", "w") as file:
        pass

todos = fn.get_todos()


def add_todo():
    todo = st.session_state["new_todo"].capitalize() + "\n"
    todos.append(todo)
    fn.write_todos(todos)


st.title("TaskMate")
st.subheader("Welcome to TaskMate. What task do you wish to accomplish today?")
st.write("TaskMate helps you max out your productivity without hassles")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label=" ", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")
