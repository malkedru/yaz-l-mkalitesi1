"""Streamlit user interface for the Gemini code review assistant."""

import os

import streamlit as st

from services.gemini_service import MAX_CODE_LENGTH, review_code

st.set_page_config(
    page_title="Yapay Zekâ Destekli Kod İnceleme Asistanı",
    page_icon="💻",
    layout="wide",
)

st.title("💻 Yapay Zekâ Destekli Kod İnceleme Asistanı")
st.markdown(
    "Kodunuzu kalite, güvenlik ve bakım kolaylığı açısından inceleyin; "
    "uygulanabilir iyileştirme önerileri alın."
)

with st.sidebar:
    st.header("Proje hakkında")
    st.info(
        "Bu eğitim projesi; kodu doğruluk, hata yönetimi, güvenlik, "
        "performans, bakım kolaylığı ve test edilebilirlik ölçütlerine göre inceler."
    )
    st.divider()
    key_is_configured = bool(os.getenv("GEMINI_API_KEY", "").strip())
    status = "Yapılandırıldı ✅" if key_is_configured else "Yapılandırılmadı ❌"
    st.write(f"**Gemini API anahtarı:** {status}")

code_input = st.text_area(
    "İncelenecek kod",
    height=300,
    max_chars=MAX_CODE_LENGTH,
    placeholder="Örnek: def topla(a, b):\n    return a + b",
    help=f"En fazla {MAX_CODE_LENGTH:,} karakter girilebilir.",
)

if st.button("🚀 Kodu incele", type="primary"):
    if not code_input.strip():
        st.warning("Lütfen incelemek için bir kod parçası girin.")
    else:
        with st.spinner("Kod Gemini ile inceleniyor…"):
            review_result = review_code(code_input)
        st.divider()
        st.subheader("📊 İnceleme raporu ve öneriler")
        st.markdown(review_result)
