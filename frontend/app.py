import requests
import streamlit as st

st.title("Генератор Оправданий")

situation = st.text_input("Ситуация:", "Опоздание на работу")
absurdity = st.slider("Уровень абсурдности:", 1, 10, 5)
moon_phase = st.checkbox("Учитывать фазу луны")

if st.button("Сгенерировать"):
    with st.spinner("Генерация..."):
        try:
            response = requests.post(
                "http://localhost:8000/generate",
                json={
                    "situation": situation,
                    "absurdity_level": absurdity,
                    "include_moon_phase": moon_phase
                }
            )
            if response.status_code == 200:
                data = response.json()
                st.success(data["data"]["excuse"])
                st.write("Факторы:", data["data"]["factors_used"])
            else:
                st.error(f"Ошибка: {response.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("Не удалось подключиться к API. Убедитесь, что backend запущен.")