import streamlit as st
st.title("แอปพลิเคชั่นเปลี่ยนแปลงปี ค.ศ. ที่ต้องการเปลี่ยนแปลง")

bh_year=st.number_input("กรอกปี พ.ศ. ที่ต้องการเปลี่ยนแปลง",value=2569)
ce_year=bh_year-543
st'header(f"ปี ค.ศ. คือ : {ce_year}")                       
