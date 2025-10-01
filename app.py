import streamlit as st
import math
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from io import BytesIO

st.set_page_config(page_title="Kružnice", layout="centered")

st.title("Vykreslení bodů na kružnici")

# 📥 Vstupní parametry
center_x = st.number_input("Střed X", value=0.0)
center_y = st.number_input("Střed Y", value=0.0)
radius = st.number_input("Poloměr (m)", value=5.0)
points = st.number_input("Počet bodů", min_value=1, value=8)
color = st.color_picker("Barva bodů", "#ff0000")

# 🖼️ Vykreslení kružnice
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(center_x - radius - 1, center_x + radius + 1)
ax.set_ylim(center_y - radius - 1, center_y + radius + 1)
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
circle = plt.Circle((center_x, center_y), radius, fill=False, color='gray')
ax.add_artist(circle)

for i in range(points):
    angle = 2 * math.pi * i / points
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    ax.plot(x, y, 'o', color=color)

st.pyplot(fig)

# 🧾 Informace o aplikaci
with st.expander("O aplikaci"):
    st.markdown("""
    **Autor:** Aneta Kubáčová  
    **Kontakt:** aneta.kubacova@seznam.cz 
    **Technologie:** Python, Streamlit, Matplotlib, ReportLab
    """)

# 📤 Export do PDF
if st.button("Exportovat do PDF"):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 800, "Vykreslení bodů na kružnici")
    pdf.drawString(50, 780, f"Střed: ({center_x}, {center_y})")
    pdf.drawString(50, 760, f"Poloměr: {radius} m")
    pdf.drawString(50, 740, f"Počet bodů: {points}")
    pdf.drawString(50, 720, f"Barva bodů: {color}")
    pdf.drawString(50, 700, "Autor: Aneta Kubáčová ")
    pdf.drawString(50, 680, "Kontakt: aneta.kubacova@seznam.cz ")
    pdf.save()
    buffer.seek(0)
    st.download_button("Stáhnout PDF", buffer, file_name="kruznice.pdf")