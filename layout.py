import streamlit as st
st.sidebar.title("General Setting")
st.sidebar.checkbox("DarkMode",key="dark_mode")


col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("This is the first Column.")
    st.text_input("Input for Column 1", key="col1_input")


    with col2:
        st.header("Column 2")
        st.write("This is the second Column.")
        st.text_input("Input for Column 2", key="col2_input")

        tab1, tab2, tab3 = st.tabs(["Home", "About","Contact"])
        with tab1:
            st.header("Home Tab")
            st.write("Welcome to the Home tab!")
        with tab2:
            st.header("About Tab")
            st.write("This is the About tab.")
        with tab3:
            st.header("Contact Tab")
            st.write("Get in touch with us through the Contact tab.")
            

        with st.form("my_form"):
            st.write("Inside the from write your query")
            name = st.text_input("Name")
            email = st.text_input("Email")
            query = st.text_area("Query")
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.success("Form submitted successfully!")
        

        




