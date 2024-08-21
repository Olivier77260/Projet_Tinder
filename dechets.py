rdv = df.date.value_counts()
def Frequence(x):
    if x == 1.0:
        size = "Several times a week"
    elif x == 2.0:
        size = "Twice a week"
    elif x == 3.0:
        size = "Once a week"
    elif x == 4.0:
        size = "Twice a month"
    elif x == 5.0:
        size = "Once a month"
    elif x == 6.0:
        size = "Several times a year"
    else:
        size = "Almost never"
    return size
rdv.index = rdv.index.map(Frequence)
labels = rdv.index
explode = (0.1, 0.1, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig2, ax2 = plt.subplots()
ax2.pie(rdv, explode=explode, labels=labels, autopct='%0.0f%%', shadow=True, startangle=180)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

go_out = df.go_out.value_counts()
go_out.index = go_out.index.map(Frequence)
labels = go_out.index
explode = (0.1, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig3, ax3 = plt.subplots()
ax3.pie(go_out, explode=explode, labels=labels, autopct='%0.0f%%', shadow=True, startangle=60)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

size = pd.DataFrame(df['date'] - df['go_out'])
size = size.value_counts().reset_index(name='index')
size = size.rename(columns={'o': 'value', 'index': 'Rdv'})
st.dataframe(size)
st.scatter_chart(df, x='date', y='go_out', use_container_width=True, color="#dec1ff")
# st.bar_chart(df, x="go_out", y='date', stack='normalize', use_container_width=True, color="#dec1ff")
st.line_chart(size, x='Rdv')

age = df.age.value_counts()
st.scatter_chart(age, x_label='age', color='#e80e0e', size=200)

# race féminine
race_female = race[race.gender == 0].set_index('imprace')
race_female = race_female.drop('gender', axis=1)
race_female = race_female.drop(race_female[race_female.index==0].index)
race_female.sort_values(by="count", ascending=False, inplace=True)

# religion féminine
religion_female = religion[religion.gender == 0].set_index('imprelig')
religion_female = religion_female.drop('gender', axis=1)
religion_female.sort_values(by="count", ascending=False, inplace=True)

# Nuage de point
    import altair as alt

    c = (
        alt.Chart(happy_gender)
        .mark_circle()
        .encode(x="exphappy", y="count", size='count', color="count", tooltip=["count", "exphappy", "colors"])
    )

    st.altair_chart(c, theme=None, use_container_width=True)

:mailbox_with_mail:
:iphone: