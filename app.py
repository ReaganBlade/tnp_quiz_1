import streamlit as st
import random

class Quiz:
    # TODO: Define Constructor
    def __init__(self):
        self.__users__ = st.session_state.get("users", {})
        self.__current_user__ = st.session_state.get("current_user", None)
        self.__quiz_list__ = {
        "DSA": {
            "q1": {
                "ques": "What does DSA stand for?",
                "opt": [
                    "Data Structure Algorithm",
                    "Data Systems Application",
                    "Data Structures and Algorithms",
                    "Digital System Analysis"
                ],
                "ans": "Data Structures and Algorithms"
            },
            "q2": {
                "ques": "Which of the following data structures uses LIFO order?",
                "opt": [
                    "Queue",
                    "Stack",
                    "Array",
                    "Linked List"
                ],
                "ans": "Stack"
            },
            "q3": {
                "ques": "Which data structure is used for Breadth First Search in a graph?",
                "opt": [
                    "Stack",
                    "Queue",
                    "Linked List",
                    "Binary Tree"
                ],
                "ans": "Queue"
            },
            "q4": {
                "ques": "In a binary search tree, the left child node is ____ than the parent node.",
                "opt": [
                    "Greater",
                    "Less",
                    "Equal",
                    "Divisible"
                ],
                "ans": "Less"
            },
            "q5": {
                "ques": "Which algorithm is used to sort an array by repeatedly stepping through the list and swapping adjacent elements if they are in the wrong order?",
                "opt": [
                    "Quick Sort",
                    "Bubble Sort",
                    "Merge Sort",
                    "Insertion Sort"
                ],
                "ans": "Bubble Sort"
            },
            "q6": {
                "ques": "What is the time complexity of binary search?",
                "opt": [
                    "O(n)",
                    "O(n^2)",
                    "O(log n)",
                    "O(n log n)"
                ],
                "ans": "O(log n)"
            },
            "q7": {
                "ques": "Which data structure allows the fastest search?",
                "opt": [
                    "Queue",
                    "Stack",
                    "Binary Search Tree",
                    "Hash Table"
                ],
                "ans": "Hash Table"
            },
            "q8": {
                "ques": "Which traversal method is used to visit each node in a binary tree in ascending order?",
                "opt": [
                    "Pre-order",
                    "In-order",
                    "Post-order",
                    "Level-order"
                ],
                "ans": "In-order"
            },
            "q9": {
                "ques": "In a linked list, what does each node contain?",
                "opt": [
                    "Only data",
                    "Only pointer",
                    "Data and pointer",
                    "Key and value"
                ],
                "ans": "Data and pointer"
            },
            "q10": {
                "ques": "Which data structure is used to implement recursion?",
                "opt": [
                    "Queue",
                    "Array",
                    "Stack",
                    "Tree"
                ],
                "ans": "Stack"
            },
            "q11": {
                "ques": "Which sorting algorithm has the best time complexity in the average case?",
                "opt": [
                    "Selection Sort",
                    "Bubble Sort",
                    "Quick Sort",
                    "Insertion Sort"
                ],
                "ans": "Quick Sort"
            },
            "q12": {
                "ques": "Which of the following is not a linear data structure?",
                "opt": [
                    "Array",
                    "Linked List",
                    "Stack",
                    "Graph"
                ],
                "ans": "Graph"
            },
            "q13": {
                "ques": "What is the maximum number of nodes in a binary tree of height h?",
                "opt": [
                    "2^h",
                    "2^(h+1) - 1",
                    "h^2",
                    "h + 1"
                ],
                "ans": "2^(h+1) - 1"
            },
            "q14": {
                "ques": "Which of these is a divide-and-conquer algorithm?",
                "opt": [
                    "Bubble Sort",
                    "Quick Sort",
                    "Insertion Sort",
                    "Selection Sort"
                ],
                "ans": "Quick Sort"
            },
            "q15": {
                "ques": "Which data structure follows FIFO (First In First Out) principle?",
                "opt": [
                    "Stack",
                    "Queue",
                    "Graph",
                    "Tree"
                ],
                "ans": "Queue"
            },
            "q16": {
                "ques": "What is the time complexity of accessing an element in an array?",
                "opt": [
                    "O(1)",
                    "O(n)",
                    "O(log n)",
                    "O(n^2)"
                ],
                "ans": "O(1)"
            },
            "q17": {
                "ques": "Which of these is not a balanced tree?",
                "opt": [
                    "AVL Tree",
                    "Red-Black Tree",
                    "Binary Search Tree",
                    "B-Tree"
                ],
                "ans": "Binary Search Tree"
            },
            "q18": {
                "ques": "What is a complete binary tree?",
                "opt": [
                    "A tree where all levels are completely filled",
                    "A tree with a single node",
                    "A tree with only left children",
                    "A tree with both left and right children"
                ],
                "ans": "A tree where all levels are completely filled"
            },
            "q19": {
                "ques": "Which algorithm is used to find the shortest path in an unweighted graph?",
                "opt": [
                    "Depth First Search",
                    "Breadth First Search",
                    "Binary Search",
                    "Merge Sort"
                ],
                "ans": "Breadth First Search"
            },
            "q20": {
                "ques": "What is a circular queue?",
                "opt": [
                    "A queue that wraps around at the end",
                    "A queue with fixed size",
                    "A queue with variable size",
                    "A queue implemented with arrays"
                ],
                "ans": "A queue that wraps around at the end"
            }
        },
        "PYTHON": {
            "q1": {
                "ques": "What is the correct file extension for Python files?",
                "opt": [
                    ".pyt",
                    ".pt",
                    ".py",
                    ".python"
                ],
                "ans": ".py"
            },
            "q2": {
                "ques": "How do you create a variable with the numeric value 5 in Python?",
                "opt": [
                    "x = 5",
                    "int x = 5",
                    "num x = 5",
                    "x == 5"
                ],
                "ans": "x = 5"
            },
            "q3": {
                "ques": "Which method can be used to return a string in upper case letters?",
                "opt": [
                    "upper()",
                    "uppercase()",
                    "toUpperCase()",
                    "to_upper()"
                ],
                "ans": "upper()"
            },
            "q4": {
                "ques": "Which of the following is used to define a block of code in Python?",
                "opt": [
                    "Curly braces",
                    "Indentation",
                    "Parentheses",
                    "Square brackets"
                ],
                "ans": "Indentation"
            },
            "q5": {
                "ques": "What is the output of: print(type([]))?",
                "opt": [
                    "<class \"list\">",
                    "<class \"dict\">",
                    "<class \"array\">",
                    "<class \"tuple\">"
                ],
                "ans": "<class \"list\">"
            },
            "q6": {
                "ques": "Which of these is a Python keyword?",
                "opt": [
                    "function",
                    "define",
                    "return",
                    "print"
                ],
                "ans": "return"
            },
            "q7": {
                "ques": "How do you insert COMMENTS in Python code?",
                "opt": [
                    "// This is a comment",
                    "# This is a comment",
                    "/* This is a comment */",
                    "This is a comment"
                ],
                "ans": "# This is a comment"
            },
            "q8": {
                "ques": "Which of the following functions can add elements to a list?",
                "opt": [
                    "add()",
                    "append()",
                    "insert()",
                    "put()"
                ],
                "ans": "append()"
            },
            "q9": {
                "ques": "What is the output of the following code: print(4 // 3)?",
                "opt": [
                    "1.33",
                    "1",
                    "1.0",
                    "Error"
                ],
                "ans": "1"
            },
            "q10": {
                "ques": "Which of the following functions will return the length of a list?",
                "opt": [
                    "size()",
                    "length()",
                    "len()",
                    "count()"
                ],
                "ans": "len()"
            },
            "q11": {
                "ques": "Which operator is used to check if two values are not equal in Python?",
                "opt": [
                    "<>",
                    "!==",
                    "!=",
                    "=="
                ],
                "ans": "!="
            },
            "q12": {
                "ques": "How do you start a for loop in Python?",
                "opt": [
                    "for x in y",
                    "for (x in y):",
                    "foreach x in y:",
                    "loop x in y"
                ],
                "ans": "for x in y"
            },
            "q13": {
                "ques": "What will be the output of the following Python code?\n\nprint(type([]) is list)",
                "opt": [
                    "True",
                    "False",
                    "None",
                    "TypeError"
                ],
                "ans": "True"
            },
            "q14": {
                "ques": "How do you create a function in Python?",
                "opt": [
                    "function myFunction():",
                    "def myFunction():",
                    "create myFunction():",
                    "fun myFunction():"
                ],
                "ans": "def myFunction():"
            },
            "q15": {
                "ques": "What is the correct syntax to output `Hello World` in Python?",
                "opt": [
                    "print(`Hello World`)",
                    "echo(`Hello World`)",
                    "printf(`Hello World`)",
                    "console.log(`Hello World`)"
                ],
                "ans": "print(`Hello World`)"
            },
            "q16": {
                "ques": "Which of these is not a core data type in Python?",
                "opt": [
                    "Lists",
                    "Class",
                    "Tuples",
                    "Dictionary"
                ],
                "ans": "Class"
            },
            "q17": {
                "ques": "What is the output of: print(`Hello`[0])?",
                "opt": [
                    "H",
                    "h",
                    "e",
                    "o"
                ],
                "ans": "H"
            },
            "q18": {
                "ques": "What does the pass statement do in Python?",
                "opt": [
                    "Terminates the loop",
                    "Skips execution",
                    "Does nothing",
                    "Raises an error"
                ],
                "ans": "Does nothing"
            },
            "q19": {
                "ques": "How can you check the type of a variable in Python?",
                "opt": [
                    "typeof(x)",
                    "type(x)",
                    "checktype(x)",
                    "x.type()"
                ],
                "ans": "type(x)"
            },
            "q20": {
                "ques": "Which of the following methods is used to remove whitespace from the beginning and end of a string?",
                "opt": [
                    "strip()",
                    "trim()",
                    "remove()",
                    "clean()"
                ],
                "ans": "strip()"
            }
        },
        "DBMS": {
            "q1": {
                "ques": "What does DBMS stand for?",
                "opt": [
                    "Database Management System",
                    "Data Backup Management System",
                    "Data Base Management Service",
                    "Data Banking Management Service"
                ],
                "ans": "Database Management System"
            },
            "q2": {
                "ques": "Which of the following is not a type of database?",
                "opt": [
                    "Hierarchical",
                    "Network",
                    "Relational",
                    "Flat-table"
                ],
                "ans": "Flat-table"
            },
            "q3": {
                "ques": "Which SQL command is used to delete a table?",
                "opt": [
                    "DELETE TABLE",
                    "DROP TABLE",
                    "REMOVE TABLE",
                    "CLEAR TABLE"
                ],
                "ans": "DROP TABLE"
            },
            "q4": {
                "ques": "In DBMS, what does ACID stand for?",
                "opt": [
                    "Atomicity, Consistency, Isolation, Durability",
                    "Accuracy, Consistency, Isolation, Dependency",
                    "Atomicity, Concurrency, Isolation, Durability",
                    "Atomicity, Consistency, Independence, Dependency"
                ],
                "ans": "Atomicity, Consistency, Isolation, Durability"
            },
            "q5": {
                "ques": "Which of the following is a NoSQL database?",
                "opt": [
                    "MySQL",
                    "MongoDB",
                    "Oracle",
                    "PostgreSQL"
                ],
                "ans": "MongoDB"
            },
            "q6": {
                "ques": "Which command is used to remove all records from a table without removing the table itself?",
                "opt": [
                    "DELETE",
                    "DROP",
                    "CLEAR",
                    "TRUNCATE"
                ],
                "ans": "TRUNCATE"
            },
            "q7": {
                "ques": "Which language is used to query a database?",
                "opt": [
                    "HTML",
                    "SQL",
                    "CSS",
                    "C++"
                ],
                "ans": "SQL"
            },
            "q8": {
                "ques": "Which of these is a key feature of the relational database model?",
                "opt": [
                    "Data stored as objects",
                    "Data stored in tables",
                    "Data stored in hierarchies",
                    "Data stored in XML"
                ],
                "ans": "Data stored in tables"
            },
            "q9": {
                "ques": "A collection of related records in a database is called a ______.",
                "opt": [
                    "Field",
                    "Table",
                    "Column",
                    "Data type"
                ],
                "ans": "Table"
            },
            "q10": {
                "ques": "What is the purpose of the primary key in a database table?",
                "opt": [
                    "To allow duplicate values",
                    "To uniquely identify records",
                    "To act as a foreign key",
                    "To define data type"
                ],
                "ans": "To uniquely identify records"
            },
            "q11": {
                "ques": "Which SQL statement is used to update data in a database?",
                "opt": [
                    "INSERT",
                    "MODIFY",
                    "CHANGE",
                    "UPDATE"
                ],
                "ans": "UPDATE"
            },
            "q12": {
                "ques": "Which command is used to add a new record in a database table?",
                "opt": [
                    "INSERT",
                    "ADD",
                    "UPDATE",
                    "CREATE"
                ],
                "ans": "INSERT"
            },
            "q13": {
                "ques": "Which of these normal forms removes partial dependencies?",
                "opt": [
                    "1NF",
                    "2NF",
                    "3NF",
                    "BCNF"
                ],
                "ans": "2NF"
            },
            "q14": {
                "ques": "What is a foreign key?",
                "opt": [
                    "A key that uniquely identifies a record",
                    "A key that links two tables",
                    "A key with null values",
                    "A primary key for another table"
                ],
                "ans": "A key that links two tables"
            },
            "q15": {
                "ques": "Which of the following is a valid SQL aggregate function?",
                "opt": [
                    "ADD",
                    "MAX",
                    "DELETE",
                    "JOIN"
                ],
                "ans": "MAX"
            },
            "q16": {
                "ques": "Which of the following database types is often used for transaction processing?",
                "opt": [
                    "NoSQL",
                    "Hierarchical",
                    "OLTP",
                    "Relational"
                ],
                "ans": "OLTP"
            },
            "q17": {
                "ques": "In SQL, which clause is used to filter records?",
                "opt": [
                    "SELECT",
                    "FROM",
                    "WHERE",
                    "JOIN"
                ],
                "ans": "WHERE"
            },
            "q18": {
                "ques": "What type of relationship exists between tables with a primary and foreign key?",
                "opt": [
                    "One-to-One",
                    "One-to-Many",
                    "Many-to-Many",
                    "Self-Referencing"
                ],
                "ans": "One-to-Many"
            },
            "q19": {
                "ques": "Which statement is used to create a new database?",
                "opt": [
                    "CREATE DATABASE",
                    "MAKE DATABASE",
                    "NEW DATABASE",
                    "INSERT DATABASE"
                ],
                "ans": "CREATE DATABASE"
            },
            "q20": {
                "ques": "Which SQL clause is used to sort the result set?",
                "opt": [
                    "SORT BY",
                    "ORDER BY",
                    "GROUP BY",
                    "FILTER BY"
                ],
                "ans": "ORDER BY"
            }
        }
    }
        
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