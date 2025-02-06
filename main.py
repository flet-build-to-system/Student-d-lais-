from flet import *
import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS student(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                stdname TEXT,
                stdmail TEXT,
                stdphon TEXT,
                stdaddress TEXT,
                stdmathmatic INTEGER,
                stdphisiq INTEGER,
                stdsvt INTEGER,
                stdphilosoph INTEGER,
                stdenglish INTEGER,
                stdfranch INTEGER,
                stdarabic INTEGER,
                stdislam INTEGER,
                stdsport INTEGER
)""")
conn.commit()


def main(page: Page):
    page.clean()
    page.title = 'Abd elhaq'
    page.scroll = 'auto'
    page.window.top = 1
    page.window.left = 960
    page.window.width = 390
    page.window.height = 740
    page.bgcolor = 'white'
    page.theme_mode = ThemeMode.LIGHT

    ###################################

    tabe_name = 'student'
    query = f'SELECT COUNT(*) FROM {tabe_name}'
    cursor.execute(query)
    resu = cursor.fetchone()
    row_count = resu[0]

    def add(e):
        cursor.execute(
            "INSERT INTO student (stdname,stdmail,stdphon,stdaddress,stdmathmatic,stdphisiq,stdsvt,stdphilosoph,stdenglish,stdfranch,stdarabic,stdislam,stdsport) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (tname.value, tmail.value, tphon.value, taddrese.value, mathmatic.value, phisiq.value, svt.value,
             philosophia.value, english.value, franch.value, arabic.value, islam.value, sport.value))
        conn.commit()
        page.clean()
        main(page)

    def show(e):
        page.clean()
        c = cursor = conn.cursor()
        c.execute("SELECT * FROM student")
        users = c.fetchall()
        #print(users)
        page.add(Row([ElevatedButton(icon=Icons.ADD,text='إضافةطالب جديد',on_click=lambda e:main(page),expand=True)],alignment=MainAxisAlignment.CENTER,expand=True))

        if not users == "":
            keys = ['id', 'stdname', 'stdmail', 'stdphon', 'stdaddress', 'stdmathmatic', 'stdphisiq', 'stdsvt',
                    'stdphilosoph', 'stdenglish', 'stdfranch', 'stdarabic', 'stdislam', 'stdsport']
            resu = [dict(zip(keys, values)) for values in users]
            for x in resu:

                ################## marks ##################
                m = x['stdmathmatic']
                p = x['stdphisiq']
                s = x['stdsvt']
                ph = x['stdphilosoph']
                e = x['stdenglish']
                f = x['stdfranch']
                a = x['stdarabic']
                i = x['stdislam']
                sp = x['stdsport']
                res = m + p + s + ph + e + f + a + i + sp
                res2 = res / 9
                if res2 < 10:
                    no = Text(f'❌ راسب {res2}', size=19, color=colors.WHITE)
                elif res2 >= 10:
                    no = Text(f'✔ ناجح {res2}', size=19, color=colors.WHITE)

                page.add(
                    Card(
                        color='black',
                        content=Container(
                            border=border.all(3,'black'),
                            border_radius= 25,
                            content=Column([
                                ListTile(
                                    leading=Icon(icons.PERSON),
                                    title=Text('Name : ' + x['stdname'], color='black'),
                                    subtitle=Text('Stdname Email : ' + x['stdmail'], color='black')
                                ),
                                Row([
                                    Text('Phon : ' + x['stdphon'], color='green'),
                                    Text('Address : ' + x['stdaddress'], color='green')
                                ], alignment=MainAxisAlignment.CENTER),

                                Row([
                                    Text('الرياضيات :' + str(x['stdmathmatic']), color='blue'),
                                    Text('الفزياء :' + str(x['stdphisiq']), color='blue'),
                                    Text('علوم الحياة و الأرض :' + str(x['stdsvt']), color='blue')
                                ], alignment=MainAxisAlignment.CENTER),
                                Row([
                                    Text('الفلسفة :' + str(x['stdphilosoph']), color='blue'),
                                    Text('اللإنجلزية :' + str(x['stdenglish']), color='blue'),
                                    Text('الفرنسية :' + str(x['stdfranch']), color='blue')
                                ], alignment=MainAxisAlignment.CENTER),
                                Row([
                                    Text('العربية :' + str(x['stdarabic']), color='blue'),
                                    Text('التربية الإسلامية :' + str(x['stdislam']), color='blue'),
                                    Text('التربية البدنية :' + str(x['stdsport']), color='blue')
                                ], alignment=MainAxisAlignment.CENTER),

                                Row([
                                    no
                                ], alignment=MainAxisAlignment.CENTER)
                            ])
                        )
                    )
                )

    ############## Felids ##############
    tname = TextField(label='إسم الطالب', icon=icons.PERSON, rtl=True, height=55,expand=True)
    tmail = TextField(label='البريد الإلكتروني', icon=icons.MAIL, rtl=True, height=55,expand=True,multiline=True)
    tphon = TextField(label='هاتف الطالب', icon=icons.PHONE, rtl=True, height=55,expand=True)
    taddrese = TextField(label='العنوان أو السكن', icon=icons.LOCATION_CITY, rtl=True, height=55,expand=True,multiline=True)
    ####################################

    #############  marks ###############
    marktext = Text("Mark Student - علامات الطالب", text_align='center', weight='bold',expand=True)
    mathmatic = TextField(label='رياضيات', width=110, rtl=True, height=55,expand=True)
    phisiq = TextField(label='الفزياء', width=110, rtl=True, height=55,expand=True)
    svt = TextField(label='علوم الإحياء', width=110, rtl=True, height=55,expand=True)
    philosophia = TextField(label='الفلسفة', width=110, rtl=True, height=55,expand=True)
    english = TextField(label='اللإنجلزية', width=110, rtl=True, height=55,expand=True)
    franch = TextField(label='الفرنسية', width=110, rtl=True, height=55,expand=True)
    arabic = TextField(label='العربية', width=110, rtl=True, height=55,expand=True)
    islam = TextField(label='التربية الإسلامية', width=110, rtl=True, height=55,expand=True)
    sport = TextField(label='التربية البدنية', width=110, rtl=True, height=55,expand=True)
    ####################################

    addbuttn = ElevatedButton(
        "إضافة طالب جديد",
        width=170,
        height=50,
        expand=True,
        style=ButtonStyle(bgcolor='blue', color='white', padding=0),
        on_click=add
    )

    showbuttn = ElevatedButton(
        text="عرض كل الطلاب",
        width=170,
        height=50,
        expand=True,
        style=ButtonStyle(bgcolor='blue', color='white', padding=0),
        on_click=show
    )

    page.add(
        Row([
            Image(src="images.jpg")
        ], alignment=MainAxisAlignment.CENTER),

        Row([
            Text("تطبيق الطالب و المعلم في جيبك", size=20, font_family="Footlight MT", color='black')
        ], alignment=MainAxisAlignment.CENTER),

        Row([
            Text("عدد الطلاب المسجلين :", size=20, font_family="Footlight MT", color='black'),
            Text(str(row_count), size=20, font_family="Footlight MT", color='black'),
        ], alignment=MainAxisAlignment.CENTER, rtl=True),
        tname,
        tmail,
        tphon,
        taddrese,

        Row([
            marktext
        ], alignment=MainAxisAlignment.CENTER, rtl=True),

        Row([
            mathmatic, phisiq, svt
        ], alignment=MainAxisAlignment.CENTER, rtl=True),

        Row([
            philosophia, english, franch
        ], alignment=MainAxisAlignment.CENTER, rtl=True),

        Row([
            arabic, islam, sport
        ], alignment=MainAxisAlignment.CENTER, rtl=True),

        Row([
            addbuttn, showbuttn
        ], alignment=MainAxisAlignment.CENTER)
    )

    page.update()


app(main)
