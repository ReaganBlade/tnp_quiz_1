import streamlit as st
import random

class Quiz:
    def __init__(self):
        # Initializing session states if not already done
        if "users" not in st.session_state:
            st.session_state["users"] = {}
        if "current_user" not in st.session_state:
            st.session_state["current_user"] = None
        if "Logged" not in st.session_state:
            st.session_state["Logged"] = False
        if "ques" not in st.session_state:
            st.session_state["ques"] = []

        self.__quiz_list__ = {
            "DSA": {
                "q1": {
                    "ques": "What does DSA stand for?",
                    "opt": [
                        "Data Structure Algorithm",
                        "Data Systems Application",
                        "Data Structures and Algorithms",
                        "Digital System Analysis",
                    ],
                    "ans": "Data Structures and Algorithms",
                }
            },
            "PYTHON": {
                "q1": {
                    "ques": "What is the correct file extension for Python files?",
                    "opt": [".pyt", ".pt", ".py", ".python"],
                    "ans": ".py",
                }
            },
            "DBMS": {
                "q1": {
                    "ques": "What does DBMS stand for?",
                    "opt": [
                        "Database Management System",
                        "Data Backup Management System",
                        "Data Base Management Service",
                        "Data Banking Management Service",
                    ],
                    "ans": "Database Management System",
                }
            },
        }

    def check_user(self, user_name) -> bool:
        return user_name in st.session_state["users"]

    def user_registration(self, name, user_name, user_class, user_password):
        if self.check_user(user_name):
            st.error("User already exists")
        else:
            st.session_state["users"][user_name] = {
                "name": name,
                "class": user_class,
                "pwd": user_password,
            }
            st.success("User Successfully Registered")

    def user_login(self, user_name, user_password):
        if (
            self.check_user(user_name)
            and st.session_state["users"][user_name]["pwd"] == user_password
        ):
            st.session_state["Logged"] = True
            st.session_state["current_user"] = user_name
            st.success(f"Login Successful. Welcome, {user_name}!")
        else:
            st.error("Invalid Credentials")

    def user_logout(self):
        st.session_state["Logged"] = False
        st.session_state["current_user"] = None
        st.session_state["ques"] = []
        st.success("Logged out successfully")

    def start_quiz(self):
        st.header("🌌 Quiz Time!")
        col1, col2 = st.columns(2)

        with col1:
            subj = st.radio(
                "Select Subject",
                list(self.__quiz_list__.keys()),
                help="Choose the subject you want to attempt",
            )

            if not st.session_state["ques"]:
                st.session_state["ques"] = random.sample(
                    list(self.__quiz_list__[subj].keys()), len(self.__quiz_list__[subj])
                )

            if st.button("Randomize Questions"):
                st.session_state["ques"] = random.sample(
                    list(self.__quiz_list__[subj].keys()), len(self.__quiz_list__[subj])
                )

            st.button("Logout", on_click=self.user_logout)

        with col2:
            self.list_questions(subj, st.session_state["ques"])

    def list_questions(self, subj, questions):
        score = 0
        for ques in questions:
            selected = st.radio(
                self.__quiz_list__[subj][ques]["ques"],
                self.__quiz_list__[subj][ques]["opt"],
            )
            if st.button("Submit", use_container_width=True):
                if selected == self.__quiz_list__[subj][ques]["ans"]:
                    score += 1
                st.write(f"Your Total Score is: {score}")

    def status(self):
        st.write("Current User:", st.session_state["current_user"])
        st.write("All Users:", st.session_state["users"])
        st.write("Session State:", st.session_state)


if __name__ == "__main__":
    st.markdown(
        """
    # 🌌 **Welcome to Galactic Quiz!** 🚀

    ✨ **Unleash Your Knowledge Across the Universe!** ✨
    Are you ready to challenge your mind and explore diverse galaxies of trivia?
    Whether it's science, history, pop culture, or more, **Galactic Quiz** takes you on an interstellar journey through knowledge.
    """
    )

    q = Quiz()

    if st.session_state["Logged"]:
        q.start_quiz()
    else:
        st.header("Login or Registration")
        col1, col2 = st.columns(2)

        with col1:
            user_opt = st.radio("Choose one", ["Login", "Registration"])

        with col2:
            if user_opt == "Login":
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                st.button("Login", on_click=q.user_login, args=(username, password))
            elif user_opt == "Registration":
                username = st.text_input("Username")
                name = st.text_input("Name")
                user_class = st.text_input("Class")
                password = st.text_input("Password", type="password")
                st.button(
                    "Register",
                    on_click=q.user_registration,
                    args=(name, username, user_class, password),
                )
