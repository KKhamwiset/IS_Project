import streamlit as st
import pandas as pd

class ML_prepare_viewset:
    def __init__(self):
        pass
        
    def app(self):
        st.session_state.current_page = "ML Preparations"
        
        # Page title with styling
        st.title("Machine Learning Preparations")
        st.markdown('---')
        
        # Introduction section
        st.header("🔍 Data Preparation")
        st.write("สำหรับขั้นตอนการเตรียมข้อมูลในการเทรน models ผมได้ค้นหา datasets ใน kraggle และ archive.ics.uci.edu ผมได้เลือกข้อมูล \"Census Income\"")

        # Dataset details in a collapsible section
        with st.expander("📊 รายละเอียดชุดข้อมูล (Dataset Details)"):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**แหล่งที่มา:** UCI Machine Learning Repository")
                st.write("**จำนวนตัวอย่าง:** 48,842 instances")
            with col2:
                st.write("**จำนวนคุณลักษณะ:** 14 attributes")
                st.write("**เป้าหมาย:** ทำนายรายได้มากกว่า/น้อยกว่า $50K")
        
        # Model Selection section
        st.header("🤖 Model Selection")
        st.markdown("**เพื่อทำการเทรนในโมเดล SVM** เพื่อทำนายเงินเดือนจาก input ที่รับมาว่าจะได้มากกว่ารายได้มากกว่า 50k หรือไม่")
        
        # Dataset features table (wider display)
        st.header("📋 รายละเอียดชุดข้อมูล Census Income")
        
        # Create feature data dictionary
        feature_data = {
            'คุณลักษณะ': [
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
                'ต่อเนื่อง (continuous)', 
                'หมวดหมู่ (categorical)', 
                'ต่อเนื่อง (continuous)', 
                'หมวดหมู่ (categorical)', 
                'ต่อเนื่อง (continuous)', 
                'หมวดหมู่ (categorical)', 
                'หมวดหมู่ (categorical)', 
                'หมวดหมู่ (categorical)', 
                'หมวดหมู่ (categorical)', 
                'หมวดหมู่ (categorical)', 
                'ต่อเนื่อง (continuous)', 
                'ต่อเนื่อง (continuous)', 
                'ต่อเนื่อง (continuous)', 
                'หมวดหมู่ (categorical)'
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
                'ตัวเลขต่อเนื่อง', 
                'เอกชน, รับจ้างตัวเอง, รัฐบาลกลาง, รัฐบาลท้องถิ่น, รัฐบาลมลรัฐ, ไม่ได้รับค่าจ้าง, ไม่เคยทำงาน', 
                'ตัวเลขต่อเนื่อง', 
                'ปริญญาตรี, วิทยาลัยบางส่วน, มัธยมศึกษา, บัณฑิตวิชาชีพ, อนุปริญญา, ปริญญาโท, ปริญญาเอก, ฯลฯ', 
                'ตัวเลขต่อเนื่อง', 
                'แต่งงาน, หย่าร้าง, โสด, แยกกันอยู่, หม้าย, คู่สมรสไม่อยู่', 
                'สนับสนุนด้านเทคนิค, งานช่าง, งานบริการ, ขาย, ผู้บริหาร, ผู้เชี่ยวชาญ, เสมียน, เกษตรกรรม, ฯลฯ', 
                'ภรรยา, บุตร, สามี, ไม่อยู่ในครอบครัว, ญาติอื่นๆ, โสด', 
                'คนผิวขาว, เอเชีย-หมู่เกาะแปซิฟิก, อเมริกันอินเดียน-เอสกิโม, อื่นๆ, คนผิวดำ', 
                'หญิง, ชาย', 
                'ตัวเลขต่อเนื่อง', 
                'ตัวเลขต่อเนื่อง', 
                'ตัวเลขต่อเนื่อง', 
                'สหรัฐอเมริกา, กัมพูชา, อังกฤษ, เปอร์โตริโก, แคนาดา, เยอรมนี, อินเดีย, ญี่ปุ่น, จีน, ไทย, ฯลฯ'
            ]
        }

        # Create DataFrame
        df_features = pd.DataFrame(feature_data)

        # Use dataframe instead of table for better width control
        st.dataframe(df_features, use_container_width=True, height=550)
        

        st.info("""
        **หมายเหตุ:** 
        * ข้อมูลชุดนี้ใช้สำหรับทำนายว่ารายได้ของบุคคลจะมากกว่า 50,000 ดอลลาร์ต่อปีหรือไม่
        * ชุดข้อมูลแบ่งเป็น `adult.data` สำหรับการเทรนโมเดล และ `adult.test` สำหรับการทดสอบโมเดล
        * โมเดล SVM จะถูกเทรนด้วยข้อมูลเหล่านี้เพื่อทำนายระดับรายได้
        """)

        st.header("⚙️ ขั้นตอนการเตรียมข้อมูล (Data Preparation Process)")
        
        code_tabs = st.tabs(["1️⃣ การอ่านข้อมูล", "2️⃣ การตรวจสอบข้อมูล", "3️⃣ การอ่านข้อมูลพร้อม Label"])
        
        with code_tabs[0]:
            st.code(
                """
                    # Data preprocessing steps
                    import pandas as pd
                    df = pd.read_csv('../data/income/adult.data')
                    df.shape
                """)
            
        with code_tabs[1]:
            st.code("""
                    # ตรวจสอบข้อมูลเบื้องต้น
                    df.info()
                    df.head()
                """)
            
        with code_tabs[2]:
            st.code("""
                    # เนื่องจากข้อมูลก่อนหน้าไม่มี feature label จะทำการเรียกข้อมูลใหม่โดยใส่ feature label จาก adult.name
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