import streamlit as st

# Set the page layout

import numpy as np
import base64

if "framework"  not in st.session_state:
    st.session_state.framework = "lstm"
    
#import matplotlib.pyplot as plt
# Path to your logo image
encoded_logo = "logo2.png"
main_bg_ext = 'png'
main_bg = 'page3.png '

if st.session_state.framework == "lstm": 
    bg_color = "#FF5733"  # For example, a warm red/orange
    bg_color_iv = "orange"  # For example, a warm red/orange
    text_h1 = "BI-DIRECTIONAL"
    text_i = "Long short term memory"
    model = "TENSORFLOW"
if st.session_state.framework == "gru": 
    bg_color = "#FF5733"  # For example, a warm red/orange
    bg_color_iv = "orange"  # For example, a warm red/orange
    text_h1 = "GATED RECURRENT UNIT"
    text_i = "Long short term memory"
    model = "TENSORFLOW"
st.markdown(
    f"""
    <style>
       /* Container for logo and text */
        /* Container for logo and text */
        .logo-text-container {{
            position: fixed;
            top: 20px; /* Adjust vertical position */
            left: 30px; /* Align with sidebar */
            display: flex;
            align-items: center;
            gap: 25px;
            width: 70%;
            z-index:1000;
        }}

        /* Logo styling */
        .logo-text-container img {{
            width: 50px; /* Adjust logo size */
            border-radius: 10px; /* Optional: round edges */
            margin-left:-5px;
            margin-top: -15px;

        }}

        /* Bold text styling */
        .logo-text-container h1 {{
            font-family: Nunito;
            color: #0175C2;            
            font-size: 25px;
            font-weight: bold;
            margin-right :100px;
            padding:0px;
            top:0;
            margin-top: -12px;
        }}
         .logo-text-container i{{
             font-family: Nunito;
            color: orange;            
            font-size: 15px;
            margin-right :10px;
            padding:0px;
            margin-left:-18.5%;
            margin-top:1%;
         }}

        /* Sidebar styling */
        section[data-testid="stSidebar"][aria-expanded="true"] {{
            margin-top: 100px !important; /* Space for the logo */
            border-radius: 0 60px 0px 60px !important; /* Top-left and bottom-right corners */
            width: 200px !important; /* Sidebar width */
            background: none; /* No background */
            color: white !important;
        }}

        header[data-testid="stHeader"] {{
            background: transparent !important;
            margin-right: 100px !important;
            margin-top: 1px !important;
            z-index: 1 !important;
            
        color: blue; /* White text */
        font-family:  "Times New Roman " !important; /* Font */
        font-size: 18px !important; /* Font size */
        font-weight: bold !important; /* Bold text */
        padding: 10px 20px; /* Padding for buttons */
        border: none; /* Remove border */
        border-radius: 35px; /* Rounded corners */
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Shadow effect */
        transition: all 0.3s ease-in-out; /* Smooth transition */
         display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px 0;
        width:90%;
        left:5.5%;
        height:60px;
        margin-top:70px;
        backdrop-filter: blur(10px);
        border: 2px solid rgba(255, 255, 255, 0.4); /* Light border */

        }}

        div[data-testid="stDecoration"] {{
            background-image: none;
        }}

        div[data-testid="stApp"] {{
          background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
          background-size: cover;  /* Ensure the image covers the full page */
          background-position: center;
          background-repeat:no-repeat;
            height: 98vh;
            width: 99%;
            border-radius: 20px !important;
            margin-left: 10px;
            margin-right: 20px;
            margin-top: 10px;
            overflow: hidden;
            backdrop-filter: blur(10px); /* Glass effect */
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2); /* Light border */

        }}

        div[data-testid="stSidebarNav"] {{
            display: none;
        }}

        /* Styling for the content container */
         [class*="st-key-content-container-1"] {{
 
             background: rgba(255, 255, 255, 0.5);  /* Semi-transparent white background */
        border: 2px solid rgba(255, 255, 255, 0.4); /* Light border */

            backdrop-filter: blur(10px);  /* Apply blur effect */
            -webkit-backdrop-filter: blur(10px);  /* For Safari compatibility */
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);  /* Subtle shadow for depth */
            width: 98%;  /* Make it span across most of the screen */
            margin-left: 0.5%;
            margin-right: 0.5%;
            height: 92.5vh; /* Adjust to fill most of the screen */
            overflow-y: auto; /* Enable vertical scrolling */
            position: fixed; /* Keep the container fixed on the screen */
            top: 3.5%;  /* Adjust top margin */
            left: 0.5%;  /* Adjust left margin */
            z-index: 0; /* Keep behind sidebar and header */
            margin-bottom:2%;

        }}
          [class*="st-key-content-container-3"] {{
             
            margin-top: 80px;  /* Adjust top margin */
           

            

        }}
        /* Styling for the content container */
         [class*="st-key-content-container-2"] {{
            background-color: transparent; /* Transparent background */
            border-radius: 20px;
            padding: 20px;
            width: 50%;  /* Make it span across most of the screen */

            height: 85vh; /* Adjust to fill most of the screen */
            overflow-y: auto; /* Enable vertical scrolling */
            position: fixed; /* Keep the container fixed on the screen */
            top: 7%;  /* Adjust top margin */
            left: 49.5%;  /* Adjust left margin */
            right:2%;
            border-left: 3px solid rgba(255, 255, 155, 0.9); /* Light border */

        }}

        /* Button row styling */
        .button-row {{
            display: flex;
            justify-content: flex-start;
            gap: 20px;
            margin-bottom: 20px;
        }}

        .custom-button {{
            width: 100px;
            height: 40px;
            border-radius: 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }}

        .custom-button:hover {{
            background-color: #0056b3;
        }}
        div.stButton > button {{                
        background: rgba(255, 255, 255, 0.2);
        color: blue; /* White text */
        font-family:  "Times New Roman " !important; /* Font */
        font-size: 18px !important; /* Font size */
        font-weight: bold !important; /* Bold text */
        padding: 10px 20px; /* Padding for buttons */
        border: none; /* Remove border */
        border-radius: 35px; /* Rounded corners */
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Shadow effect */
        transition: all 0.3s ease-in-out; /* Smooth transition */
         display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px 0;
        width:160px;
        height:50px;
        margin-top:5px;

    }}

    /* Hover effect */
    div.stButton > button:hover {{
        background: rgba(255, 255, 255, 0.2);
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.4); /* Enhanced shadow on hover */
        transform: scale(1.05); /* Slightly enlarge button */
        transform: scale(1.1); /* Slight zoom on hover */
        box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.4); /* Glow effect */
    }}
     /* Outer large circle with transparent background */
        .outer-circle {{
            width: 350px;
            height: 350px;
            border-radius: 40%; /* Circular shape */
            background-color: transparent; /* Transparent background */
            border: 1px solid white; /* Golden border */
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* Shadow for depth */
        }}

        /* Inner smaller circle with light grey background */
        .inner-circle {{
            width: 330px;
            height: 330px;
             backdrop-filter: blur(10px);
            background: rgba(255, 255, 255, 0.2);

            border-radius: 40%; /* Circular shape */
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden; /* Ensure image is contained within the circle */
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4); /* Shadow for depth */
             border: 1px solid white; /* Golden border */

        }}

        /* Style for the image to fit within the inner circle */
        .inner-circle img {{
            width: 100%;
            height: 100%;
            object-fit: cover; /* Ensure the image covers the circular area */
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* Shadow for depth */

        }}
          /* Style for the upload button */
        [class*="st-key-upload-btn"] {{
            position: absolute;
            top: 50%; /* Position from the top of the inner circle */
            left: 5%; /* Position horizontally at the center */
            transform: translateX(-40%); /* Adjust to ensure it's centered */
            padding: 10px 20px;
            color: black;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-size: 23px;
            with:300px;
            height:100px;
            z-index:1000;
        }}

        .upload-btn:hover {{
            background-color: rgba(0, 123, 255, 1);
        }}
          div[data-testid="stFileUploader"] label > div > p {{
            display:none;
            color:white !important;
        }}
        section[data-testid="stFileUploaderDropzone"] {{
          width:190px;
        height: 120px;
        background-color: white;
        border-radius: 40px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top:-10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
        margin:20px;
        background-color: rgba(255, 255, 255, 0.7); /* Transparent blue background */
        color:white;
        }}
        div[data-testid="stFileUploaderDropzoneInstructions"] div > small{{
           color:white !important;
           display:none;
        }}
         div[data-testid="stFileUploaderDropzoneInstructions"] span{{
          margin-left:60px;
        }}
        div[data-testid="stFileUploaderDropzoneInstructions"] div{{
          display:none;
        }}
       section[data-testid="stFileUploaderDropzone"] button{{
        display:none;
       }}
         div[data-testid="stMarkdownContainer"] p {{
            font-family: "Times New Roman" !important; /* Elegant font for title */
            color:white !important;
        }}
   .titles{{
      margin-top:10px !important;
      margin-left:50px;
      font-family: "Times New Roman" !important; 

  }}
    /* Title styling */
    .titles h1{{
   font-family: "Times New Roman" !important; /* Elegant font for title 
    font-size: 3rem;
    font-weight: bold;
    margin-left: 5px;
   /* margin-top:-50px;*/
    margin-bottom:50px;
    padding: 0;
    color: black; /* Neutral color for text */
    }}
 .titles > div{{
   font-family: "Times New Roman" !important; /* Elegant font for title */
    font-size: 1.01rem;
    margin-left: -50px;
    margin-bottom:1px;
    padding: 0;
    color:black; /* Neutral color for text */
    }}

    </style>
  
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
        /* Outer container to define the grid */
        .grid-container {
            display: grid;
            grid-template-columns: repeat(2 1fr);  /* 2 columns */
            grid-template-rows: repeat(2, 1fr);     /* 2 rows */
            gap: 20px;  /* Space between containers */
            width: 90%;
            height: 5vh;
             align-items: center;
        }

        /* Individual grid items (containers) */
        .grid-item {
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            display: flex;
            justify-content: left;
            align-items: center;
            text-align: left;
            background: rgba(0, 0, 0, 0.2);  /* Semi-transparent white background */

            border-radius: 20px;
            padding: 20px;
            width: 80%;  /* Make it span across most of the screen */
            margin-left: 0.5%;
            margin-right: 0.5%;
        }

        /* Optional styling for the subheader and content */
        .grid-item h3 {
            margin: 0;
            color: #333;
            font-size:18px;
            width:100px;
             font-family: "Times New Roman" !important; /* Elegant font for title */
            font-size: 1.rem;
            font-weight: bold;
        }

        .grid-item p {
            color: #555;
        }
        .title-container {
            display: flex;
            align-items: center;  /* Vertically center the title and the image */
        }
        .title-container img {
            width: 40px;  /* Adjust the size of the image */
            height: 40px; /* Adjust the size of the image */
            margin-right: 10px; /* Space between the image and the title */
        }
        .title {
            font-size: 20px;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True
)
st.markdown(f""" <div class="logo-text-container">
    <img src="data:image/png;base64,{base64.b64encode(open("logo2.png","rb").read()).decode()}" alt="Uploaded Image">
<h1>{text_h1}<br>

</h1>
<i>{  text_i}</ai>


</div>

                """,
                    unsafe_allow_html=True,
                )


