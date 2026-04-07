# # # import streamlit as st
# # # import joblib
# # # import numpy as np

# # # # load model
# # # model = joblib.load("regression_model_joblib")

# # # st.title("🎓 CGPA to Package Predictor")
# # # st.write("Enter your CGPA to predict the expected package")

# # # cgpa = st.number_input(
# # #     "Enter CGPA",
# # #     min_value=0.0,
# # #     max_value=10.0,
# # #     step=0.1
# # # )

# # # if st.button("Predict Package"):
# # #     input_data = np.array([[cgpa]])
# # #     prediction = model.predict(input_data)

# # #     # ✅ FIX HERE
# # #     predicted_package = prediction[0][0]

# # #     st.success(f"💼Predicted Package: ₹ {predicted_package:.2f} LPA")

# # import streamlit as st
# # import joblib
# # import numpy as np
# # import matplotlib.pyplot as plt

# # # Load model
# # model = joblib.load("regression_model_joblib")

# # # Page config
# # st.set_page_config(page_title="CGPA Predictor", page_icon="🎓", layout="centered")

# # # Custom CSS (for professional UI)
# # st.markdown("""
# #     <style>
# #         .main {
# #             background-color: #f5f7fa;
# #         }
# #         .title {
# #             text-align: center;
# #             font-size: 40px;
# #             font-weight: bold;
# #             color: #2E86C1;
# #         }
# #         .subtitle {
# #             text-align: center;
# #             font-size: 18px;
# #             color: gray;
# #             margin-bottom: 30px;
# #         }
# #         .stButton>button {
# #             background-color: #2E86C1;
# #             color: white;
# #             border-radius: 8px;
# #             height: 3em;
# #             width: 100%;
# #             font-size: 16px;
# #         }
# #     </style>
# # """, unsafe_allow_html=True)

# # # Header
# # st.markdown("<div class='title'>🎓 CGPA to Package Predictor</div>", unsafe_allow_html=True)
# # st.markdown("<div class='subtitle'>Predict your expected placement package based on CGPA</div>", unsafe_allow_html=True)

# # # Layout (2 columns)
# # col1, col2 = st.columns([1, 1])

# # with col1:
# #     st.subheader("📥 Input")
# #     cgpa = st.slider("Select CGPA", 0.0, 10.0, 7.0, 0.1)

# #     predict_btn = st.button("🚀 Predict Package")

# # with col2:
# #     st.subheader("📊 Result")

# #     if predict_btn:
# #         input_data = np.array([[cgpa]])
# #         prediction = model.predict(input_data)
# #         predicted_package = prediction[0][0]

# #         # Metric style output
# #         st.metric(label="💼 Expected Package", value=f"₹ {predicted_package:.2f} LPA")

# # # Graph section
# # if predict_btn:
# #     st.markdown("---")
# #     st.subheader("📈 Prediction Analysis")

# #     # Generate smooth line
# #     x = np.linspace(0, 10, 100).reshape(-1, 1)
# #     y = model.predict(x)

# #     fig, ax = plt.subplots()

# #     # Clean professional style
# #     ax.plot(x, y, linewidth=3, label="Model Trend")
# #     ax.scatter(cgpa, predicted_package, s=100, label="Your Prediction")

# #     ax.set_xlabel("CGPA", fontsize=12)
# #     ax.set_ylabel("Package (LPA)", fontsize=12)
# #     ax.set_title("CGPA vs Placement Package", fontsize=14)

# #     ax.grid(True, linestyle='--', alpha=0.6)
# #     ax.legend()

# #     st.pyplot(fig)

# import streamlit as st
# import joblib
# import numpy as np
# import matplotlib.pyplot as plt

# # Page config
# st.set_page_config(
#     page_title="CGPA Package Predictor",
#     page_icon="🎓",
#     layout="centered"
# )

# # Load model
# model = joblib.load("regression_model_joblib")

# # Custom CSS for styling
# st.markdown("""
#     <style>
#     .main {
#         background-color: #f5f7fa;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#         border-radius: 10px;
#         height: 3em;
#         width: 100%;
#         font-size: 16px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Title
# st.title("🎓 CGPA to Package Predictor")
# st.markdown("### Predict your expected placement package 💼")

# # Sidebar
# st.sidebar.header("📊 Input Details")
# cgpa = st.sidebar.slider("Select your CGPA", 0.0, 10.0, 7.0, 0.1)

# # Main container
# st.markdown("### 📌 Enter Details Below")

# col1, col2 = st.columns(2)

# with col1:
#     st.metric("📚 CGPA Entered", f"{cgpa}")

# with col2:
#     st.metric("📈 Placement Trend", "Increasing")

# # Prediction
# if st.button("🚀 Predict Package"):
#     input_data = np.array([[cgpa]])
#     prediction = model.predict(input_data)

#     predicted_package = prediction[0][0]

#     # Display result
#     st.success(f"💼 Predicted Package: ₹ {predicted_package:.2f} LPA")

#     # Generate graph data
#     cgpa_range = np.linspace(0, 10, 50)
#     predictions = model.predict(cgpa_range.reshape(-1, 1))

#     # Plot graph
#     fig, ax = plt.subplots()
#     ax.plot(cgpa_range, predictions, label="Prediction Curve")
#     ax.scatter(cgpa, predicted_package, marker='o', label="Your Prediction")

#     ax.set_xlabel("CGPA")
#     ax.set_ylabel("Package (LPA)")
#     ax.set_title("📊 CGPA vs Package Prediction")
#     ax.legend()

#     st.pyplot(fig)

# # Footer
# st.markdown("---")
# st.caption("Built with ❤️ using Streamlit")

import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(
    page_title="CGPA Package Predictor",
    page_icon="🎓",
    layout="wide"
)

# Load model
model = joblib.load("regression_model_joblib")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}

.title {
    font-size: 40px;
    font-weight: bold;
    background: linear-gradient(90deg, #00C9FF, #92FE9D);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #1c1f26;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    text-align: center;
}

.result {
    font-size: 28px;
    color: #00ffcc;
    font-weight: bold;
}

.small-text {
    color: #aaa;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<p class="title">🎓 CGPA → Package Predictor</p>', unsafe_allow_html=True)
st.markdown("#### Smart Placement Prediction Dashboard 💼")

# ---------- INPUT ----------
st.sidebar.header("📊 Input Panel")
cgpa = st.sidebar.slider("Select CGPA", 0.0, 10.0, 7.0, 0.1)

st.sidebar.markdown("### 💡 Tips")
st.sidebar.info("Higher CGPA generally leads to better packages, but skills matter too!")

# ---------- MAIN LAYOUT ----------
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.metric("📚 CGPA", f"{cgpa}")
    st.progress(int(cgpa * 10))
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("### 📈 Placement Insights")
    st.write("""
    - CGPA < 6 → Low chances  
    - CGPA 6–8 → Moderate packages  
    - CGPA > 8 → High package opportunities 🚀  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- PREDICTION ----------
if st.button("🚀 Predict Package"):
    input_data = np.array([[cgpa]])
    prediction = model.predict(input_data)
    predicted_package = prediction[0][0]

    # RESULT CARD
    st.markdown(f"""
    <div class="card">
        <div class="small-text">Predicted Package</div>
        <div class="result">₹ {predicted_package:.2f} LPA</div>
    </div>
    """, unsafe_allow_html=True)

    # GRAPH
    cgpa_range = np.linspace(0, 10, 100)
    predictions = model.predict(cgpa_range.reshape(-1, 1))

    fig, ax = plt.subplots()
    ax.plot(cgpa_range, predictions)
    ax.scatter(cgpa, predicted_package)

    ax.set_xlabel("CGPA")
    ax.set_ylabel("Package (LPA)")
    ax.set_title("CGPA vs Package Trend")

    st.pyplot(fig)

    # ---------- INTERPRETATION ----------
    if predicted_package > 12:
        st.success("🔥 Excellent! You're in top-tier package range.")
    elif predicted_package > 6:
        st.info("👍 Good! You have decent placement chances.")
    else:
        st.warning("⚠️ Improve skills & projects to boost package.")

# ---------- FOOTER ----------
st.markdown("---")
st.caption("🚀 Built for Placement Prediction | By You")