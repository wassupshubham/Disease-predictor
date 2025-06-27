import streamlit as st

# Define the HTML snippet to embed Watson Assistant
chatbot_html = """
<div id="watson-assistant-chat-container" style="display: none; position: fixed; bottom: 20px; right: 20px; z-index: 1000;">
  <script>
    window.watsonAssistantChatOptions = {
      integrationID: "a91ece9e-9f6a-46d9-b251-0cbeb2c34486",
      region: "us-south",
      serviceInstanceID: "60295ae2-9f40-43e6-86fa-a8d209116040",
      onLoad: function(instance) { instance.render(); }
    };
    setTimeout(function(){
      const t=document.createElement('script');
      t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/latest/WatsonAssistantChatEntry.js";
      document.getElementById('watson-assistant-chat-container').appendChild(t);
    });
    
  </script>
</div>
"""

def main():
    # Apply background image and custom styles to the Streamlit app
    st.markdown("""
    <style>
      [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1628348070889-cb656235b4eb?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
      }
      [data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0);  
      }
      [data-testid="stToolbar"] {
        right: 2rem;
      }
      .st-emotion-cache-czk5ss.e16jpq800 {
        visibility: hidden;
      }
      .st-emotion-cache-mnu3yk.ef3psqc5 {
        visibility: hidden;
      }
      .st-emotion-cache-15ecox0.ezrtsby0 {
        visibility: hidden;
      }
      .st-emotion-cache-fm8pe0.e1nzilvr4 {
        color: black;
      }
      .st-emotion-cache-fm8pe0.e1nzilvr4{
        color: white;
      }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: black;'>Welcome To The VitalBot</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.link_button("Diabetic Predictor", "https://diabeticpredictor.streamlit.app/")
    st.link_button("Heart Attack Predictor", "https://heartattackpredictor1.streamlit.app/")
    st.link_button("Liver Predictor", "https://liverpredictor.streamlit.app/")
    st.link_button("Migrane Predictor", "https://migranepredictor.streamlit.app/")
    # Add a button to toggle chatbot visibility
    if st.button("Open Chatbot (Scroll ↓)"):
        st.components.v1.html(chatbot_html, height=800)

if __name__ == "__main__":
    main()
