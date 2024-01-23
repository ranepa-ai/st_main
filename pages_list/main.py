import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
from io import BytesIO
import requests
import base64




def main_page(df_search):
        
    st.header("Лаборатория цифровых компетенций✔️", divider='rainbow')
    st.subheader("Здесь вы найдете инструменты, которые помогут вам освоить навыки анализа данных, машинного обучения и ИИ, стать востребованным специалистом и воплотить идеи в жизнь")


    tab1, tab2, tab3 = st.tabs(["Анализ данных😎📊", "Машинное обучение🚀💻", "Глубокое обучение🧠🤖"])

    data = {
        'Трек 1': [
            'Анализ данных',
            tab1, """Этот трек включает в себя развернутый разделочный анализ данных, где вы освоите методы визуализации и анализа данных. 

Используя различные инструменты, такие как Matplotlib и Seaborn, анализировать структуру и характеристики данных станет проще. 

Вы также научитесь проводить предварительную обработку данных и обнаруживать выбросы и ошибки в них."""
        ],
        'Трек 2': [
            'Машинное обучение',
            tab2, """Этот трек сфокусирован на основах машинного обучения. 
            
Вы изучите понятия, такие как обучение с учителем и без учителя, а также классификацию данных. 

Погрузитесь в анализ данных для бизнеса и методы машинного обучения, применяемые в корпоративной среде.

Разработайте навыки принятия решений на основе данных и их применение в маркетинге."""
        ],
        'Трек 3': [
            'Глубокое обучение (ИИ)',
            tab3, """Этот трек предоставит вам базовое понимание искусственного интеллекта и глубокого обучения.

Вы изучите основы больших языковых моделей, введение в chatgpt, а также применение искусственного интеллекта в бизнесе. 

Работа с естественным языком, анализ настроений и выделение фичей для улучшения моделей - все это будет в вашем распоряжении."""
        ],
    }



    # Для каждого трека создаем экспандер и отображаем информацию
    for track, info in data.items():

        tab = info[1]
        description = info[0]
        info_capt = info[2]


        with tab:
            with st.expander(f"Описание трека⤵️"):
                st.write(info_capt)

            N_cards_per_row = 3
            df_sample = df_search[df_search.Track_main == description]

            track_old = df_sample['Track'].iloc[0]
            st.write("---")
            st.subheader(track_old)

            n_place = 0
            for track_plot in df_sample['Track'].unique().tolist():
                for n_row, row in df_sample[df_sample.Track==track_plot].iterrows():
            

                    if row['Track'] != track_old:
                        st.write("---")
                        st.subheader(row['Track'])
                        n_place = 0
                    track_old = row['Track']
            
                    i = n_place % N_cards_per_row
                    if i == 0 or row['Track'] != track_old:
                        cols = st.columns(N_cards_per_row, gap="large")
                        st.write("")
                    


                    # URL изображения
                    image_cot = f'https://github.com/Chetoff1228/images/blob/main/{row["Picture"]}.png?raw=true'

                    with cols[n_place % N_cards_per_row]:
                    #  st.caption(f"Описание, получаемые скилы")
                        st.markdown(f"**{row['Name']}**")
                        #st.components.v1.html(clickable_image_html(row['Source'], image_cot), height=200)
                        st.markdown(f'<a href="{row["Source"]}"><img src="{image_cot}" alt="Foo" width="275" height="250"/></a>', unsafe_allow_html=True)

                        st.caption(f"**{row['Caption'].strip()}**")

                    n_place += 1
    st.write("---")