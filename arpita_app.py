import streamlit as st

st.set_page_config(page_title="For My Bestie Arpita", page_icon="💖")

st.title("🌟 Dedicating to My Best Friend Forever 🌟")
st.write("Hey there! Yeh special web app sirf aur sirf meri bestie ke liye pure pyaar aur dosti ke sath banaya gaya hai.")

st.markdown("---")
user_name = st.text_input("🔐 Enter your sacred name to unlock this secret tribute:")

if user_name:
    cleaned_name = user_name.strip().lower()
    allowed_names = ["arpita", "arpitaa"]
    
    if cleaned_name in allowed_names:
        st.success("🎉 Access Granted! Welcome to your special zone, My Bestie Arpita! 👑")
        
        st.markdown("---")
        st.subheader("💖 Dost Ho Toh Tum Jaisi! 💖")
        
        bestie_age = st.number_input("Apni age yahan daalo:", min_value=1, max_value=100, value=13)
        fav_color = st.selectbox("Apna sabse favourite colour select karo:", ["Red", "Pink", "Blue", "Green", "Purple", "Yellow"])
        
        st.markdown("---")
        
        # Dynamic response based on favorite color
        if fav_color == "Pink":
            st.markdown("🌸 **Pink is your vibe!** Tumhari tarah yeh colour bhi sabse pyaara aur cute hai!")
        elif fav_color == "Blue":
            st.markdown("🌊 **Blue ocean vibes!** Tumhara dil bhi samandar ki tarah gehra aur saaf hai!")
        elif fav_color == "Red":
            st.markdown("❤️ **Bold & Beautiful Red!** Tumhari energy hamesha fire rehti hai!")
        elif fav_color == "Purple":
            st.markdown("💜 **Royal Purple!** Tum meri life ki sabse special aur royal dost ho!")
        elif fav_color == "Green":
            st.markdown("🌿 **Fresh Green vibes!** Tumhari dosti meri life mein hamesha taazgi laati hai!")
        else:
            st.markdown("⭐ **Bright Yellow!** Tumhari hansi sabki life roshan kar deti hai!")

        st.markdown(f"""
        ### 💌 Kuch Dil Ki Baatein (Tumhare Aur Mere Liye):
        * Arpita, tum sirf meri best friend nahi ho, balki meri jaan aur meri partner-in-crime ho!
        * Chahe school ki baatein ho ya life ke pagalpan wale moments, tum hamesha mere sath khadi rahti ho.
        * Tumhari yeh age ({bestie_age} years) aur yeh khubsurat dosti mere liye duniya ki sabse badi daulat hai.
        * Chahe kuch bhi ho jaye, humari dosti kabhi kam nahi hogi. Tum hamesha meri bestie rahogi!
        * **Love you so much, my bestie Arpita! You are the absolute best! ❤️**
        """)
        
        st.markdown("---")
        st.info("✨ **Made with lots of dosti, madness, and coding magic by your best friend, Rabia!** ✨")
        st.balloons()
        
    else:
        st.error("❌ Access Restricted! 🚫 Yeh jagah sirf aur sirf meri bestie **Arpita** ke liye reserved hai! Sirf wahi iska password janti hai.")
