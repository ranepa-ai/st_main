import streamlit as st

def lk_page():
    st.header("Личный кабинет👨🏻‍💻", divider='rainbow')
    st.subheader("Добро пожаловать в ваш личный кабинет! Здесь вы можете управлять своими данными.")

    # Персональные данные пользователя
    user_info = {
        "Имя": "Иван",
        "Фамилия": "Иванов",
        "Email": "ivanov@example.com",
        "Фотография": "https://avatars.githubusercontent.com/u/74776380?s=400&u=8f590290b1bb1fe733413a3d973b8506396c6aa3&v=4",
        # Другие персональные данные...
    }

    # Отображение карточки пользователя
    st.markdown(f'<img src="{user_info["Фотография"]}" alt="Foo" width="150" height="150"/></a>', unsafe_allow_html=True)
    #st.image(user_info["Фотография"], caption='Ваше фото', use_column_width=True)
    st.write(f"**Имя:** {user_info['Имя']}")
    st.write(f"**Фамилия:** {user_info['Фамилия']}")
    st.write(f"**Email:** {user_info['Email']}")

    # Возможность изменения персональных данных
    if st.button("Изменить персональные данные"):
        new_name = st.text_input("Введите новое имя", user_info["Имя"])
        new_surname = st.text_input("Введите новую фамилию", user_info["Фамилия"])
        new_email = st.text_input("Введите новый email", user_info["Email"])

        # Обновление данных
        user_info["Имя"] = new_name
        user_info["Фамилия"] = new_surname
        user_info["Email"] = new_email

        st.success("Персональные данные успешно обновлены!")

