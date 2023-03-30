import streamlit as st

st.title('Konversi Satuan Panjang')
st.write('by: rijallatipudin')
length = st.number_input("Masukkan nilai yang akan dikonversi", min_value=0.0)
unit1 = st.selectbox("Pilih satuan awal", ["mm", "cm", "dm", "m", "dam", "hm", "km", "inchi"])
unit2 = st.selectbox("Pilih satuan tujuan", ["mm", "cm", "dm", "m", "dam", "hm", "km", "inchi"])

def convert(length, unit1, unit2):
        if unit1 == "mm":
            if unit2 == "cm":
                return length / 10
            elif unit2 == "dm":
                return length / 100
            elif unit2 == "m":
                return length / 1000
            elif unit2 == "dam":
                return length / 10000
            elif unit2 == "hm":
                return length / 100000
            elif unit2 == "km":
                return length / 1000000
            elif unit2 == "mm":
                return length / 1
        if unit1 == "cm":
            if unit2 == "dm":
                return length / 10
            elif unit2 == "m":
                return length / 100
            elif unit2 == "dam":
                return length / 1000
            elif unit2 == "hm":
                return length / 10000
            elif unit2 == "km":
                return length / 100000
            elif unit2 == "cm":
                return length / 1
        if unit1 == "dm":
            if unit2 == "m":
                return length / 10
            elif unit2 == "dam":
                return length / 100
            elif unit2 == "hm":
                return length / 1000
            elif unit2 == "km":
                return length / 10000
            elif unit2 == "dm":
                return length / 1
        if unit1 == "m":
            if unit2 == "dam":
                return length / 10
            elif unit2 == "hm":
                return length / 100
            elif unit2 == "km":
                return length / 1000
            elif unit2 == "m":
                return length / 1
        if unit1 == "dam":
            if unit2 == "hm":
                return length / 10
            elif unit2 == "km":
                return length / 100
            elif unit2 == "dam":
                return length / 1
        if unit1 == "hm":
            if unit2 == "km":
                return length / 10
            elif unit2 == "hm":
                return length / 1
        if unit1 == "km":
            if unit2 == "hm":
                return length * 10
            elif unit2 == "dam":
                return length * 100
            elif unit2 == "m":
                return length * 1000
            elif unit2 == "dm":
                return length * 10000
            elif unit2 == "cm":
                return length * 100000
            elif unit2 == "mm":
                return length * 1000000
            elif unit2 == "km":
                return length * 1
        if unit1 == "hm":
            if unit2 == "dam":
                return length * 10
            elif unit2 == "m":
                return length * 100
            elif unit2 == "dm":
                return length * 1000
            elif unit2 == "cm":
                return length * 10000
            elif unit2 == "mm":
                return length * 100000
            elif unit2 == "km":
                return length * 1
        if unit1 == "dam":
            if unit2 == "dam":
                return length * 1
            elif unit2 == "m":
                return length * 10
            elif unit2 == "dm":
                return length * 100
            elif unit2 == "cm":
                return length * 1000
            elif unit2 == "mm":
                return length * 10000
        if unit1 == "m":
            if unit2 == "m":
                return length * 1
            elif unit2 == "dm":
                return length * 10
            elif unit2 == "cm":
                return length * 100
            elif unit2 == "mm":
                return length * 1000
        if unit1 == "dm":
            if unit2 == "dm":
                return length * 1
            elif unit2 == "cm":
                return length * 10
            elif unit2 == "mm":
                return length * 100
        if unit1 == "cm":
            if unit2 == "cm":
                return length * 1
            elif unit2 == "mm":
                return length * 10
        if unit1 == "mm":
            if unit2 == "mm":
                return length * 1
            
        if unit1 == "km":
            if unit2 == "inchi":
                return length / 0.0000254
        if unit1 == "hm":
            if unit2 == "inchi":
                return length / 0.000254
        if unit1 == "dam":
            if unit2 == "inchi":
                return length / 0.00254
        if unit1 == "m":
            if unit2 == "inchi":
                return length / 0.0254
        if unit1 == "dm":
            if unit2 == "inchi":
                return length / 0.254
        if unit1 == "cm":
            if unit2 == "inchi":
                return length / 2.54
        if unit1 == "mm":
            if unit2 == "inchi":
                return length / 25.4
            
        if unit1 == "inchi":
            if unit2 == "km":
                return length * (2.54 / 100000)
        if unit1 == "inchi":
            if unit2 == "hm":
                return length * (2.54 / 10000)
        if unit1 == "inchi":
            if unit2 == "dam":
                return length * (2.54 / 1000)
        if unit1 == "inchi":
            if unit2 == "m":
                return length * (2.54 / 100)
        if unit1 == "inchi":
            if unit2 == "dm":
                return length * (2.54 / 10)
        if unit1 == "inchi":
            if unit2 == "cm":
                return length * (2.54 / 1)
        if unit1 == "inchi":
            if unit2 == "mm":
                return length * (2.54 * 10)

if st.button("Konversi"):
        result = convert(length, unit1, unit2)
        st.success(f"{length} {unit1} = {result} {unit2}")
        st.text('satuan metrik (SI) : mm, cm, dm, m, dam, hm, km.')
        st.text('satuan imperial : inchi, kaki, mil, yard.')
