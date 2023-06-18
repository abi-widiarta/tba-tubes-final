# Cara Menjalankan Program :
# Program dapat digunakan dengan mengakses alamat tautan 


import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align: center;'>Lexical Analyzer/Parser</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Tugas Besar TBA IF-45-09</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Kelompok 9</h4>", unsafe_allow_html=True)
st.divider()

statusValid = '<p style="color:Green; font-size: 20px; text-align: center;">Kode yang anda input benar!</p>'
statusInvalid = '<p style="color:Red; font-size: 20px; text-align: center;">Kode yang anda input salah!</p>'

st.markdown("<h5 style='text-align: center;'>Program lexical analyzer/parser untuk sintaks perulangan \"while-do\" dalam bahasa c++</h5>", unsafe_allow_html=True)

st.write('Copy this code: ')
code = '''while (x<y) {
    x++;
}
    '''
st.code(code, language='cpp')

text=st.text_area("Input Code : ", placeholder="Input code")

def notFound(cekList, cek):
    for i in range(len(cekList)):
        if cekList[i].head == cek:
            return False
    return True

def analyze(text):
    currState = 'q0'
    i = 0
    while i < len(text):
        if currState == 'q0':
            if text[i] == 'w':
                currState = 'q1'
                i+=1
            elif text[i] == '(' or text[i] == ')' or text[i] == '{' or text[i] == '}' or text[i] == '+' or text[i] == '-' or text[i] == ';' or text[i] == 'x' or text[i] == 'y' or text[i] == '>' or text[i] == '<':
                if notFound(listToken, text[i]):
                    temp = token(text[i], True)
                    listToken.append(temp)
                head.append(text[i])
                state.append(currState)
                if text[i] == 'x' or text[i] == 'y':
                    statement.append("<var>")
                elif text[i] == '>' or text[i] == '<':
                    statement.append("<operator>")
                else:
                    statement.append(text[i])
                i+=1
            elif text[i] == ' ' or text[i] == '\n':
                i+=1
            else:
                if notFound(listToken, text[i]):
                    temp = token(text[i], False)
                    listToken.append(temp)
                i+=1
        elif currState == 'q1':
            if text[i] == 'h':
                currState = 'q2'
                i+=1
            elif text[i] == ' ' or text[i] == '\n':
                i+=1
            else:
                if notFound(listToken, text[i]):
                    temp = token(text[i], False)
                    listToken.append(temp)
                currState = 'q0'
                i+=1
        elif currState == 'q2':
            if text[i] == 'i':
                currState = 'q3'
                i+=1
            elif text[i] == ' ' or text[i] == '\n':
                i+=1
            else:
                if notFound(listToken, text[i]):
                    temp = token(text[i], False)
                    listToken.append(temp)
                currState = 'q0'
                i+=1
        elif currState == 'q3':
            if text[i] == 'l':
                currState = 'q4'
                i+=1
            elif text[i] == ' ' or text[i] == '\n':
                i+=1
            else:
                if notFound(listToken, text[i]):
                    temp = token(text[i], False)
                    listToken.append(temp)
                currState = 'q0'
                i+=1
        elif currState == 'q4':
            if text[i] == 'e':
                if notFound(listToken, "while"):
                    temp = token("while", True)
                    listToken.append(temp)
                head.append("while")
                state.append(currState)
                statement.append("while")
                currState = 'q0'
                i+=1
            elif text[i] == ' ' or text[i] == '\n':
                i+=1
            else:
                if notFound(listToken, text[i]):
                    temp = token(text[i], False)
                    listToken.append(temp)
                currState = 'q0'
                i+=1

statement = []
statement1 = ['while', '(', '<var>', '<operator>', '<var>', ')', '{', '<var>', '+', '+', ';', '}']
statement2 = ['while', '(', '<var>', '<operator>', '<var>', ')', '{', '<var>', '-', '-', ';', '}']
head = []
state = []

class token:
    def __init__(self, head, valid):
        self.head = head
        self.valid = valid

listToken = []

text = list(text)
valid = True
currState = 'q0'

namaToken = []
statusToken = []
if st.button('RUN'):
    analyze(text)
    for i in range(len(listToken)):
        if listToken[i].valid:
            statusToken.append("True")
            namaToken.append(listToken[i].head)
        else:
            statusToken.append("False")
            namaToken.append(listToken[i].head)
            valid = False
    st.write(pd.DataFrame({
                'Token': namaToken,
                'Valid' : statusToken
            }))
    if valid:
        if statement == statement1 or statement == statement2:
            grammar = "Grammar: "
            for i in range(len(statement)):
                grammar+= statement[i] + " "
            st.write(grammar)
            st.write("\nSusunan token sudah sesuai grammar")

            st.write("\nParser")
            parser = []
            for i in range(len(head)):
                parser.append(head[i])
            st.write(pd.DataFrame({
                'Parser': parser,
            }))
        else:
            susunanToken = "Susunan token: "
            for i in range(len(statement)):
                susunanToken += statement[i] + " "
            st.write(susunanToken)
            i = 0
            stop = False
            while i <= len(statement)-1 and stop == False:
                if len(statement) < 1:
                    st.write("\nError, Expected while at the start of statement")
                elif statement[0] != "while":
                    st.write("\nError, Expected while at the start of statement")
                    stop = True
                elif (len(statement) == 1 and statement[0] == "while"):
                    st.write("\nError, Expected ( after while")
                    stop = True
                elif (len(statement) > 1 and statement[0] == "while") and (statement[1] != '('):
                    st.write("\nError, Expected ( after while")
                    stop = True
                elif (i == 8) and len(statement) > 8:
                    if (statement[i] != statement1[i]) and (i == 8 and statement[i] != statement2[i]):
                        st.write("\nError, Expected + or - after <var>")
                        stop = True
                elif i == 9 and len(statement) > 9:
                    if (statement[i] != statement1[i]) and statement[i-1] == '+':
                        st.write("\nError, Expected + after +")
                        stop = True
                elif i == 9 and len(statement) > 9:
                    if (statement[i] != statement2[i]) and statement[i-1] == '-':
                        st.write("\nError, Expected - after -")
                        stop = True
                elif (i != 8 and i != 9) and ((len(statement) > 9) or (len(statement) < 8)):
                    if (statement[i] != statement1[i]):
                        st.write("\nError, Expected", statement1[i], "after", statement[i-1])
                        stop = True
                i += 1
            if len(statement) == 0:
                st.write("\nError, Expected while at the start of statement")
            elif stop != True and len(statement) != 0:
                st.write("\nError, Expected", statement1[i], "after", statement[i-1])
    else:
        st.write("Token tidak valid")