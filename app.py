import streamlit as st
hide_menu = """
<style>
#MainMenu{visibility:hidden;}
footer{visibility:visible;}
footer:after{
    content:' by Kamal Kishor Chaurasiya';
    color:tomato;
}
</style>
"""

def main():
    st.set_page_config(
    page_title="My App",
    page_icon=":tada:",
    # layout="wide"
    )
    st.markdown(hide_menu, unsafe_allow_html=True)
    st.title("Enter your numbers to find the largest number.")
    st.write("---")

    num1 = st.number_input('Enter the first number and press Enter...', key=1, value=0)
    num2 = st.number_input('Enter the second number and press Enter...', key=2, value=0)
    num3 = st.number_input('Enter the third number and press Enter...', key=3, value=0)
    st.write("---")
    st.write("###### The numbers entered by you are :red[**{}**], :red[**{}**] and :red[**{}**]".format(num1, num2,num3))

    choice = st.radio(
        "Kindly confirm :green[**Yes**] to see the result.",
        ('Yes', 'No'), index=1
        )
    if choice == 'Yes':
        st.write("---")
        st.header("Result")
        max_num = max([num1, num2,num3])
        st.write("##### The largest among the three numbers is :blue[**{}**].".format(max_num))
    else:
        st.write("---")
        st.write("Please refresh, re-enter the numbers and click :green['Yes'] to confirm'.")

if __name__ == "__main__":
    main()