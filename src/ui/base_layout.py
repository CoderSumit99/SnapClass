import streamlit as st

def style_background_home():
    st.markdown("""
                <style>
                .stApp {
                    background-color: #5865F2 !important;
                }
                .stApp div[data-testid="stColumn"] {
                       background-color: #E0E3FF !important;
                       padding: 2rem !important;
                       border-radius:5rem !important;
                }
                /* Hide only the Streamlit-generated page header on home */
                h1[data-testid="stHeader"], h2[data-testid="stHeader"] {
                    display: none !important;
                }
                /* Hide the extra custom header markup in header_home while keeping the styled title */
                div[style*="display: flex"][style*="flex-direction: column"] h1 {
                    display: none !important;
                }
                /* Make column headers (I'm a Student, I'm a Teacher) black for visibility */
                .stColumn h2 {
                    color: grey !important;
                }
                /* Make SnapClass title white on home page */
                .snapclass-title span {
                    color: white !important;
                }
                </style>
                """, unsafe_allow_html=True)



def style_background_dashboard():
    st.markdown("""
                <style>
                .stApp {
                    background-color: #E0E3FF !important;
                }
                /* Make SnapClass title blue on teacher portal */
                .snapclass-title-dashboard span {
                    color: #5865F2 !important;
                }
                /* Make teacher screen heading dull black */
                h2 {
                    color: #666666 !important;
                }
                </style>
                """, unsafe_allow_html=True)




def style_base_layout():
    st.markdown("""
                <style>
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Plus+Jakarta+Sans&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&family=Plus+Jakarta+Sans&display=swap');

                .snapclass-title {
                    font-family: 'Climate Crisis', 'Outfit', 'Plus Jakarta Sans', sans-serif !important;
                    font-size: 2.4rem !important;
                    line-height: 1.0 !important;
                    margin-bottom: 0.5rem !important;
                    text-align: center;
                }

                .snapclass-title span {
                    display: block;
                    line-height: 1 !important;
                }

                .snapclass-title-dashboard {
                    font-family: 'Climate Crisis', 'Outfit', 'Plus Jakarta Sans', sans-serif !important;
                    font-size: 2.4rem !important;
                    line-height: 1.0 !important;
                    margin-bottom: 0.5rem !important;
                    text-align: center;
                }

                .snapclass-title-dashboard span {
                    display: inline;
                    line-height: 1 !important;
                }

                .snapclass-title + h1, .snapclass-title + h2,
                .snapclass-title + * h1, .snapclass-title ~ * h1,
                .snapclass-title ~ h1 {
                    display: none !important;
                }

                
               /*Hide top bar of streamlit*/
                
                #MainMenu ,footer,header {
                  visibility: hidden;
                
                }
                .block-container {
                    padding: 1.5rem !important;
                }
                 h1{
                    font-family: 'Climate Crisis', sans-serif !important;
                    font-size: 3.5rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem !important;
                   
                }  
                 h2{
                    font-family: 'Climate Crisis', sans-serif !important;
                    font-size: 2rem !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0rem !important;
                }
                
                h3,h,p {
                    font-family: 'Outfit', sans-serif !important;
                }

                /* Make text input labels black */
                label {
                    color: black !important;
                }


                button{
                     border-radius: 1.5rem !important;
                     background-color: #5865F2 !important;
                     color: white !important;
                     padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                
                button[kind="secondary"] {
                     border-radius: 1.5rem !important;
                     background-color: #EB459E !important;
                     color: white !important;
                     padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                 
                button[kind="tertiary"] {
                     border-radius: 1.5rem !important;
                     background-color: black !important;
                     color: white !important;
                     padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
              
                button:hover {
                    transform: scale(1.05) !important;
                }
                

                </style>
                """, unsafe_allow_html=True)
    
    