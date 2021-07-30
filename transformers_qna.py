import streamlit as st
from transformers import pipeline


@st.cache(allow_output_mutation=True)
def load_model():
    question_answerer = pipeline("question-answering", model='bert-large-uncased-whole-word-masking-finetuned-squad')
    return question_answerer


def get_data(question, context):
    question_answerer = load_model()
    a = question_answerer(
        question=question,
        context=context
    )
    return a['answer']


# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    st.title('Transformers Q and A Demo')
    import socket   
    hostname = socket.gethostname()   
    IPAddr = socket.gethostbyname(hostname)   
    print("Your Computer Name is:" + hostname)   
    print("Your Computer IP Address is:" + IPAddr)   
    st.success(IPAddr)

    # following lines create boxes in which user can enter data required to make prediction
    c = st.text_area("Context", "My name is Robert")
    q = st.text_input('Question', 'What is my name?')
    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = get_data(q, c)
        st.success(result)
        print(result)


if __name__ == '__main__':
    main()
