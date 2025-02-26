import streamlit as st
import pandas as pd

class ML_prepare_viewset:
    def __init__(self):
        pass

    def tabs_manager(self):
        st.session_state.current_page = "ML Preparations"
        st.title("Machine Learning Preparations")
        st.markdown('---')
        menu = st.tabs(["🌐การเตรียมข้อมูล","🗳️ขั้นตอนการเทรน Model SVM","🗳️ขั้นตอนการเทรน Model K-Mean Clustering"])
        with menu [0]:
            self.dataset_preparation()
        with menu [1]:
            self.svm_model_training()
        with menu [2]:
            self.kmean_model_training()

    def dataset_preparation(self):
        st.header("🔍 Data Preparation")
        st.write("สำหรับขั้นตอนการเตรียมข้อมูลในการเทรน models ผมได้ค้นหา datasets ใน kraggle และ archive.ics.uci.edu ผมได้เลือกข้อมูล \"Census Income\"")


        with st.expander("📊 รายละเอียดชุดข้อมูล (Dataset Details)"):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**แหล่งที่มา:** UCI Machine Learning Repository")
                st.write("**จำนวนตัวอย่าง:** 48,842 instances")
            with col2:
                st.write("**จำนวนคุณลักษณะ:** 14 attributes")
                st.write("**เป้าหมาย:** ทำนายรายได้มากกว่า/น้อยกว่า $50K")
        
        st.header("🤖 Model Selection")
        st.markdown("เพื่อทำการเทรนในโมเดล **SVM และ K-Mean Clustering** เพื่อทำนายเงินเดือนจาก input ที่รับมาว่าจะได้มากกว่ารายได้มากกว่า 50k หรือไม่")
        

        st.header("📋 รายละเอียดชุดข้อมูล Census Income")
        

        feature_data = {
            'ชื่อ': [
                'อายุ (age)', 
                'ประเภทการจ้างงาน (workclass)', 
                'น้ำหนักประชากร (fnlwgt)', 
                'การศึกษา (education)', 
                'ระดับการศึกษา-ตัวเลข (education-num)', 
                'สถานภาพสมรส (marital-status)', 
                'อาชีพ (occupation)', 
                'ความสัมพันธ์ (relationship)', 
                'เชื้อชาติ (race)', 
                'เพศ (sex)', 
                'กำไรจากทุน (capital-gain)', 
                'ขาดทุนจากทุน (capital-loss)', 
                'ชั่วโมงทำงานต่อสัปดาห์ (hours-per-week)', 
                'ประเทศที่เกิด (native-country)'
            ],
            'ประเภท': [
                'Continuous', 
                'Categorical', 
                'Continuous', 
                'Categorical', 
                'Continuous', 
                'Categorical', 
                'Categorical', 
                'Categorical', 
                'Categorical', 
                'Categorical', 
                'Continuous', 
                'Continuous', 
                'Continuous', 
                'Categorical'
            ],
            'รายละเอียด': [
                'อายุของบุคคลเป็นปี', 
                'ประเภทของนายจ้างหรือการจ้างงาน', 
                'น้ำหนักตัวอย่างที่สำรวจโดยสำมะโนประชากร แสดงถึงจำนวนคนที่มีคุณลักษณะคล้ายคลึงกัน', 
                'ระดับการศึกษาสูงสุดที่สำเร็จ', 
                'ตัวเลขที่แทนระดับการศึกษา (1-16)', 
                'สถานะการสมรสปัจจุบัน', 
                'ประเภทงานหรืออาชีพที่ทำ', 
                'ความสัมพันธ์ภายในครอบครัว', 
                'กลุ่มเชื้อชาติที่ระบุ', 
                'เพศของบุคคล', 
                'รายได้จากการลงทุนหรือขายทรัพย์สิน', 
                'การขาดทุนจากการลงทุนหรือขายทรัพย์สิน', 
                'จำนวนชั่วโมงทำงานต่อสัปดาห์', 
                'ประเทศที่เกิดหรือมีสัญชาติ'
            ],
            'ค่าที่เป็นไปได้': [
                'ตัวเลขต่อเนื่อง (Continuous)', 
                'เอกชน, รับจ้างตัวเอง, รัฐบาลกลาง, รัฐบาลท้องถิ่น, รัฐบาลมลรัฐ, ไม่ได้รับค่าจ้าง, ไม่เคยทำงาน', 
                'ตัวเลขต่อเนื่อง', 
                'ปริญญาตรี, วิทยาลัย, มัธยมศึกษา, บัณฑิตวิชาชีพ, อนุปริญญา, ปริญญาโท, ปริญญาเอก, ฯลฯ', 
                'ตัวเลขต่อเนื่อง (Continuous)', 
                'แต่งงาน, หย่าร้าง, โสด, แยกกันอยู่, หม้าย, คู่สมรสไม่อยู่', 
                'สนับสนุนด้านเทคนิค, งานช่าง, งานบริการ, ขาย, ผู้บริหาร, ผู้เชี่ยวชาญ, เสมียน, เกษตรกรรม, ฯลฯ', 
                'ภรรยา, บุตร, สามี, ไม่อยู่ในครอบครัว, ญาติอื่นๆ, โสด', 
                'เอเชีย-หมู่เกาะแปซิฟิก, อเมริกันอินเดียน-เอสกิโม, อื่นๆ', 
                'หญิง, ชาย', 
                'ตัวเลขต่อเนื่อง (Continuous)', 
                'ตัวเลขต่อเนื่อง (Continuous)', 
                'ตัวเลขต่อเนื่อง (Continuous)', 
                'สหรัฐอเมริกา, กัมพูชา, อังกฤษ, เปอร์โตริโก, แคนาดา, เยอรมนี, อินเดีย, ญี่ปุ่น, จีน, ไทย, ฯลฯ'
            ]
        }

        df_features = pd.DataFrame(feature_data)
        st.dataframe(df_features, use_container_width=True, height=550)
        

        st.info("""
        **หมายเหตุ:** 
        * ตารางด้านบนถูกแปลงจากไฟล์ `adult.names` เพื่อให้ง่ายต่อการเข้าใจความหมายของแต่ละ Features
        * ข้อมูลชุดนี้ใช้สำหรับทำนายว่ารายได้ของบุคคลจะมากกว่า 50,000 ดอลลาร์ต่อปีหรือไม่
        * ชุดข้อมูลแบ่งเป็น `adult.data` สำหรับการเทรนโมเดล และ `adult.test` สำหรับการทดสอบโมเดล
        * โมเดล SVM และ K-Mean Clustering จะถูกเทรนด้วยข้อมูลชุดนี้
        """)

        st.header("⚙️ ขั้นตอนการเตรียมข้อมูล (Data Preparation Process)")
        
        code_tabs = st.tabs(["1️⃣ การอ่านข้อมูล", "2️⃣ การตรวจสอบข้อมูล", "3️⃣ การอ่านข้อมูลพร้อม Label"])
        st.markdown("""
        <style>
            .stTabs [data-baseweb="tab"] {
                font-size: 28px; 
                font-weight: bold;
            }
            
            .stTabs [data-baseweb="tab-list"] {
                gap: 1.5rem;
            }
        </style>
        """, unsafe_allow_html=True)
        with code_tabs[0]:
            st.code(
                """
                    import pandas as pd
                    df = pd.read_csv('../data/income/adult.data')
                    df.shape
                """)
            
        with code_tabs[1]:
            st.code("""
                    # ตรวจสอบข้อมูลเบื้องต้น
                    df.info()
                    df.head()
                    #Output:
                    <class 'pandas.core.frame.DataFrame'>
                    RangeIndex: 32560 entries, 0 to 32559
                    Data columns (total 15 columns):
                    #   Column          Non-Null Count  Dtype 
                    ---  ------          --------------  ----- 
                    0   39              32560 non-null  int64 
                    1    State-gov      32560 non-null  object
                    2    77516          32560 non-null  int64 
                    3    Bachelors      32560 non-null  object
                    4    13             32560 non-null  int64 
                    5    Never-married  32560 non-null  object
                    6    Adm-clerical   32560 non-null  object
                    7    Not-in-family  32560 non-null  object
                    8    White          32560 non-null  object
                    9    Male           32560 non-null  object
                    10   2174           32560 non-null  int64 
                    11   0              32560 non-null  int64 
                    12   40             32560 non-null  int64 
                    13   United-States  32560 non-null  object
                    14   <=50K          32560 non-null  object
                    dtypes: int64(6), object(9)
                    memory usage: 3.7+ MB
                """)
            
        with code_tabs[2]:
            st.code("""
                    # เนื่องจากข้อมูลก่อนหน้าไม่มี feature label (สังเกตได้จากชื่อ column) จะทำการเรียกข้อมูลใหม่โดยใส่ feature label จาก adult.name
                    def read_adult_names_file(file_path):
                        with open(file_path, 'r') as file:
                            content = file.read()
                        
                        feature_section = content.split('>50K, <=50K.')[1].strip()
                        
                        features = []
                        
                        for line in feature_section.split('\\n'):
                            if line.strip():
                                parts = line.split(': ')
                                if len(parts) == 2:
                                    feature_name = parts[0].strip()
                                    features.append(feature_name)
                        
                        features.append('income')
                        
                        return features

                    column_names = read_adult_names_file('../data/income/adult.names')
                    df = pd.read_csv('../data/income/adult.data', 
                                    header=None,  
                                    names=column_names, 
                                    sep=', ',
                                    engine='python')
                    df.head()
        """)
        second_code_tabs = st.tabs(["4️⃣ การตรวจสอบข้อมูลอีกครั้ง", "5️⃣ การทำความสะอาดข้อมูล (Cleaning datasets)", "6️⃣ การแปลงข้อมูลให้เป็น numeric ทั้งหมด"])
        
        with second_code_tabs[0]:
            st.code("""
                    # เช็คว่าข้อมูลมี `null` หรือ `NaN` มั้ย
                    df.isnull().sum()
                    # Output:
                    age               0
                    workclass         0
                    fnlwgt            0
                    education         0
                    education-num     0
                    marital-status    0
                    occupation        0
                    relationship      0
                    race              0
                    sex               0
                    capital-gain      0
                    capital-loss      0
                    hours-per-week    0
                    native-country    0
                    income            0
                    dtype: int64
                    \n
                    # df.dropna(inplace = True) หากมี
                    # ทำการเช็คข้อมูลแต่ละ column จะสังเกตได้ว่ามี '?' ปนมาในข้อมูล
                    for column in df.columns:
                        j = df[column].value_counts(dropna=False)
                        print(column,':',j)
                        print('----------------------------------------')
                    # Output:
                    age : age
                    36    898
                    31    888
                    34    886
                    23    877
                    35    876
                        ... 
                    83      6
                    88      3
                    85      3
                    86      1
                    87      1
                    Name: count, Length: 73, dtype: int64
                    ----------------------------------------
                    workclass : workclass
                    Private             22696
                    Self-emp-not-inc     2541
                    Local-gov            2093
                    ?                    1836
                    State-gov            1298
                    Self-emp-inc         1116
                    Federal-gov           960
                    Without-pay            14
                    Never-worked            7
                    Name: count, dtype: int64
                    ...
                    <=50K    24720
                    >50K      7841
                    Name: count, dtype: int64
                    ----------------------------------------
            """)
        with second_code_tabs[1]:
            st.code("""
                    # ดรอป row ที่มี '?' อยู่
                    for column in df.columns:
                        df.drop(df[df[column] == '?'].index, inplace=True)  
                    
            """)
        with second_code_tabs[2]:
            st.code("""
                    # ทำการเตรียมข้อมูลโดยแปลงข้อมูลที่เป็นข้อความ (string) เป็นตัวเลข
                    # เพื่อที่จะทำให้่สามารถนำมาเทรน AI ได้
                    def map_data(x):
                        convert = x.unique()
                        return x.map(dict(zip(convert, range(1,len(convert) + 1))))
                    for column in df.columns:
                        if df[column].dtype == 'object':
                            df[column] = map_data(df[column])
                    df.astype(int)
            """)
        st.info("""
                **เนื่องจาก dataset ถูกแบ่งเป็น 2 ไฟล์**
                * `adult.data` สำหรับการเทรน
                * `adult.test` สำหรับผลลัพธ์\n
                ผมเลยสามารถที่จะข้ามการใช้ train_test_split และใช้ `adult.test` โดยตรงได้เลยเพียงแต่\n
                ต้องทำการ clean data ของ `adult.test` ตามขั้นตอนด้านบนอีกรอบหนึ่ง
                """)
        st.subheader("🎯จัดเตรียมชุดข้อมูลที่จะใช้เทรนและทดสอบ")    
        st.markdown("---")
        st.code("""
                df_test = pd.read_csv('../data/income/adult.test',
                      header=None,  
                      names=column_names, 
                      sep=', ',
                      engine='python')
                df_test.isnull().sum()
                #Output
                age               0
                workclass         1
                fnlwgt            1
                education         1
                education-num     1
                marital-status    1
                occupation        1
                relationship      1
                race              1
                sex               1
                capital-gain      1
                capital-loss      1
                hours-per-week    1
                native-country    1
                income            1
                dtype: int64
                # เนื้่องจากชุดข้อมูล test มี null value ทำการดรอปทิ้ง
                df_test.dropna(inplace=True)

                for column in df_test.columns:
                    df_test.drop(df_test[df_test[column] == '?'].index, inplace=True)  
                for column in df_test.columns:
                    if df_test[column].dtype == 'object':
                        df_test[column] = map_data(df_test[column])
                df_test.astype(int)

                X_train = df.drop('income', axis=1)
                y_train = df['income']

                X_test = df_test.drop('income',axis=1)
                y_test = df['income']
        """)
        st.markdown("---")
        st.subheader("🎉🎉🎉 เรียบร้อยครับสำหรับขั้นตอนการเตรียมพร้อม")

        
    def svm_model_training(self):
        st.header("🌟 การเทรน Model SVM")
    def kmean_model_training(self):
        st.header("🌟 การเทรน Model K-Mean Clustering")