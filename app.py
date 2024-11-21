import streamlit as st
import random

class Quiz:
    # TODO: Define Constructor
    def __init__(self):
        self.__users__ = st.session_state.get("users", {})
        self.__current_user__ = st.session_state.get("current_user", None)
        self.__quiz_list__ = {}
    # TODO: Complete function to check if user exists
    def check_user(self, user_name) -> bool:
        if user_name in self.__users__:
            return True
        return False

    # TODO: To create start quiz function
    def start_quiz(self):
        st.success('Quiz Started')

        col1, col2 = st.columns(2)
        with col1:
            subj = st.radio(
                "Select Subject",
                ["DSA", "DBMS", "PYTHON"],
                captions=["Data Structures and Algorithms", "Database Management Systems", "Python Programming Language"]
            )

            if 'ques' not in st.session_state:
                ques = random.sample(list(self.__quiz_list__[subj]), 5)
                st.session_state['ques'] = ques

            if st.button("Randomize Questions", use_container_width=True):
                ques = random.sample(list(self.__quiz_list__[subj]), 5)
                st.session_state['ques'] = ques
                # ques = list(self.__quiz_list__[subj])
            st.button("Logout", on_click=self.user_logout, use_container_width=True)

        with col2:
            self.listQues(subj, st.session_state['ques'])

    # TODO: listQues function to show the questions
    def listQues(self, subj, questions):
        score = 0

        for ques in questions:
            q1 = st.radio(
                self.__quiz_list__[subj][ques]['ques'],
                self.__quiz_list__[subj][ques]['opt'],
            )

            if q1 == self.__quiz_list__[subj][ques]['ans']:
                score += 1

        if st.button("Submit", use_container_width=True):
            st.write(f"Your Total Score is: {score}")

    # TODO: To create user Registration
    def user_registration(self, name, user_name, user_class, user_password):
        if self.check_user(user_name):
            st.error('User already exists')
            return
        else:
            if 'users' not in st.session_state:
                st.session_state['users'] = {}

            st.session_state.users[user_name] = {
                'name': name,
                'class': user_class,
                'pwd': user_password
            }
            st.success('User Successfully Registered')

    # TODO: TO create user login function
    def user_login(self, user_name, user_password):
        if self.check_user(user_name) and self.__users__[user_name]['pwd'] == user_password:
            st.session_state["Logged"] = True
            st.session_state["current_user"] = user_name
            st.success(f'Login Successful. Logged in as {user_name}')
        else:
            st.error('Invalid Credentials')

    # TODO: To create User Log Out Function
    def user_logout(self):
        st.session_state.Logged = False
        st.session_state.current_user = None


    # TODO: a function to check the functionality
    def status(self):
        st.text(self.__current_user__)
        st.write(self.__users__)
        st.write(st.session_state)


if __name__ == "__main__":
    st.markdown("""
    # 🌌 **Welcome to Galactic Quiz!** 🚀

    ✨ **Unleash Your Knowledge Across the Universe!** ✨
    Are you ready to challenge your mind and explore diverse galaxies of trivia?
    Whether it's science, history, pop culture, or more, **Galactic Quiz** takes you on an interstellar journey through knowledge.

    `> 🌠 **Galactic Quiz - Your Ultimate Journey Through Knowledge!**`
    """)

    q = Quiz()
    # q.status()

    # TODO: creating user login and registration option
    if "Logged" in st.session_state and st.session_state["Logged"] == True:
        q.start_quiz()
    else:
        st.header("Login or Registration")
        col1, col2 = st.columns(2)
        with col1:
            user_opt = st.radio(
                "Choose one",
                ["Login", "Registration"],
                captions=["Already have an account", "Don't have an account?"]
            )

        with col2:
            if user_opt == "Login":
                # st.header("User Login")
                username = st.text_input(label='username')
                password = st.text_input(label='password', type='password')

                st.button("Login", on_click=q.user_login, args=(username, password))

            if user_opt == "Registration":
                # st.header("User Registration")
                username = st.text_input(label='username')
                uname = st.text_input(label='name')
                uclass = st.text_input(label='class')
                password = st.text_input(label='password', type='password')

                st.button("Register", on_click=q.user_registration, args=(uname, username, uclass, password))