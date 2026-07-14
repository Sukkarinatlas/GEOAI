import pandas as pd

# Transcribed from data/Gistda_Price_List.pdf (7 pages)
# Columns:
#   Category            - section / satellite group from the PDF
#   Item                 - satellite name or radar acquisition mode
#   Resolution           - ground resolution
#   Polarization         - radar polarization (blank for optical)
#   Price_Label_1 /
#   Price_Value_1        - first price column as labeled in the PDF for that section
#   Price_Label_2 /
#   Price_Value_2        - second price column as labeled in the PDF for that section
#   Unit                 - pricing unit
#   Notes                - min. order area, contract terms, band count, etc.

ARCHIVE = "ข้อมูลในคลัง (Standard Archive)"
TASKING = "ข้อมูลชนิดสั่งถ่าย (Standard Tasking)"

rows = [
    # Page 1: very high resolution optical (30-50 cm), บาท/ตร.กม.
    dict(Category="ดาวเทียมรายละเอียดสูงมาก (30–50 ซม.)", Item="Pléiades NEO", Resolution="30 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="880", Price_Label_2=TASKING, Price_Value_2="1,270",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูงมาก (30–50 ซม.)", Item="WorldView-4", Resolution="30 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="920", Price_Label_2=TASKING, Price_Value_2="1,560",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูงมาก (30–50 ซม.)", Item="SuperView-2", Resolution="42 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="700", Price_Label_2=TASKING, Price_Value_2="1,100",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูงมาก (30–50 ซม.)", Item="WorldView-1", Resolution="50 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="700", Price_Label_2=TASKING, Price_Value_2="1,100",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูงมาก (30–50 ซม.)", Item="WorldView-2", Resolution="50 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="700", Price_Label_2=TASKING, Price_Value_2="1,100",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูงมาก (30–50 ซม.)", Item="WorldView-3", Resolution="50 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="700", Price_Label_2=TASKING, Price_Value_2="1,100",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูงมาก (30–50 ซม.)", Item="GeoEye-1", Resolution="50 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="700", Price_Label_2=TASKING, Price_Value_2="1,100",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูงมาก (30–50 ซม.)", Item="Pléiades", Resolution="50 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="490", Price_Label_2=TASKING, Price_Value_2="830",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูงมาก (30–50 ซม.)", Item="EarthScanner", Resolution="50 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="400", Price_Label_2=TASKING, Price_Value_2="800",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูงมาก (30–50 ซม.)", Item="SuperView-1", Resolution="50 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="500", Price_Label_2=TASKING, Price_Value_2="900",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูงมาก (30–50 ซม.)", Item="KOMPSAT-3", Resolution="50 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="400", Price_Label_2=TASKING, Price_Value_2="700",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูงมาก (30–50 ซม.)", Item="SKYSAT", Resolution="50 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="300", Price_Label_2=TASKING, Price_Value_2="560",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 1,250 ตร.กม.; Tasking โปรดติดต่อเจ้าหน้าที่; เข้าดูผ่าน API/Explorer"),

    # Page 2: high resolution optical (60cm-2m), บาท/ตร.กม.
    dict(Category="ดาวเทียมรายละเอียดสูง (60 ซม.–2 ม.)", Item="QuickBird", Resolution="60 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="700", Price_Label_2=TASKING, Price_Value_2="N/A",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูง (60 ซม.–2 ม.)", Item="GaoFen-7", Resolution="65 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="400", Price_Label_2=TASKING, Price_Value_2="700",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูง (60 ซม.–2 ม.)", Item="Jilin", Resolution="75 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="300", Price_Label_2=TASKING, Price_Value_2="600",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูง (60 ซม.–2 ม.)", Item="DailyVision", Resolution="75 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="300", Price_Label_2=TASKING, Price_Value_2="600",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูง (60 ซม.–2 ม.)", Item="GaoFen-2", Resolution="80 cm.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="300", Price_Label_2=TASKING, Price_Value_2="400",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูง (60 ซม.–2 ม.)", Item="IKONOS", Resolution="1 m.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="400", Price_Label_2=TASKING, Price_Value_2="N/A",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 25 ตร.กม. / Tasking 100 ตร.กม.; level Primary (PAN, MS, Pansharpened)"),
    dict(Category="ดาวเทียมรายละเอียดสูง (60 ซม.–2 ม.)", Item="Video Constellation", Resolution="1 m.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="142,500", Price_Label_2=TASKING, Price_Value_2="285,000",
         Unit="บาท/30 วินาที", Notes="ถ่ายวิดีโอ/ภาพกลางคืน ความยาวคลิปจำกัดที่ 30 วินาทีต่อช่วง"),
    dict(Category="ดาวเทียมรายละเอียดสูง (60 ซม.–2 ม.)", Item="Night Imaging", Resolution="1 m.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="800", Price_Label_2=TASKING, Price_Value_2="1,400",
         Unit="บาท/ตร.กม.", Notes="ถ่ายภาพกลางคืน พื้นที่สั่งซื้อขั้นต่ำ (Archive+Tasking) 100 ตร.กม.; ความกว้างแนวถ่ายภาพอย่างน้อย 5 กม."),

    # Page 3: SPOT + Thaichote
    dict(Category="ดาวเทียมรายละเอียดสูง (60 ซม.–2 ม.)", Item="SPOT-6", Resolution="1.5 m.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="190", Price_Label_2=TASKING, Price_Value_2="230",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 100 ตร.กม. / Tasking 500 ตร.กม."),
    dict(Category="ดาวเทียมรายละเอียดสูง (60 ซม.–2 ม.)", Item="SPOT-7", Resolution="1.5 m.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="190", Price_Label_2=TASKING, Price_Value_2="230",
         Unit="บาท/ตร.กม.", Notes="พื้นที่สั่งขั้นต่ำ Archive 100 ตร.กม. / Tasking 500 ตร.กม."),
    dict(Category="ดาวเทียมรายละเอียดสูง (60 ซม.–2 ม.)", Item="ไทยโชต (Thaichote)", Resolution="2 m.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="700", Price_Label_2=TASKING, Price_Value_2="6,500",
         Unit="บาท/ภาพ", Notes="ราคาที่รับ Orthorectification แล้ว 910 บาท/ภาพ"),

    # Page 4: medium resolution (>2m) + PlanetScope
    dict(Category="ดาวเทียมรายละเอียดปานกลาง (>2 เมตร)", Item="LANDSAT-5", Resolution="30 m.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="150", Price_Label_2=TASKING, Price_Value_2="N/A",
         Unit="บาท/ภาพ", Notes="คิดเฉพาะค่าดำเนินการผลิตข้อมูลจากคลังข้อมูล; level 1T, 7 Bands"),
    dict(Category="ดาวเทียมรายละเอียดปานกลาง (>2 เมตร)", Item="LANDSAT-7", Resolution="30 m.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="150", Price_Label_2=TASKING, Price_Value_2="N/A",
         Unit="บาท/ภาพ", Notes="คิดเฉพาะค่าดำเนินการผลิตข้อมูลจากคลังข้อมูล; level 1T, 8 Bands"),
    dict(Category="ดาวเทียมรายละเอียดปานกลาง (>2 เมตร)", Item="LANDSAT-8", Resolution="30 m.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="150", Price_Label_2=TASKING, Price_Value_2="N/A",
         Unit="บาท/ภาพ", Notes="level 1T, 11 Bands; ค่าดำเนินการดาวน์โหลด 150 บาท/ภาพ หากให้ สทอภ. ดำเนินการ"),
    dict(Category="ดาวเทียมรายละเอียดปานกลาง (>2 เมตร)", Item="LANDSAT-9", Resolution="30 m.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="150", Price_Label_2=TASKING, Price_Value_2="N/A",
         Unit="บาท/ภาพ", Notes="level 1T, 11 Bands; ค่าดำเนินการดาวน์โหลด 150 บาท/ภาพ หากให้ สทอภ. ดำเนินการ"),
    dict(Category="ดาวเทียมรายละเอียดปานกลาง (>2 เมตร)", Item="PLANETSCOPE", Resolution="3 m.",
         Polarization="", Price_Label_1=ARCHIVE, Price_Value_1="180", Price_Label_2="การติดตาม (Monitoring)", Price_Value_2="240",
         Unit="บาท/ตร.กม./ปี", Notes="Access+Download; พื้นที่สั่งขั้นต่ำ 100 ตร.กม.; สัญญา 1 ปี; เข้าถึงผ่าน Planet Explorer, Planet API, Desktop GIS"),

    # Page 5: RADARSAT-2 (C band) - price columns are Single Look Complex / Path Image
    *[
        dict(Category="ดาวเทียมระบบเรดาร์ - RADARSAT-2 (C band)", Item=item, Resolution=res, Polarization="",
             Price_Label_1="Single Look Complex (บาท)", Price_Value_1=slc,
             Price_Label_2="Path Image (บาท)", Price_Value_2=path,
             Unit="บาท/ภาพ", Notes="")
        for item, res, slc, path in [
            ("Standard", "25 m.", "57,600", "57,600"),
            ("Spotlight A", "1 m.", "134,400", "134,400"),
            ("Utra-Fine", "3 m.", "86,400", "86,400"),
            ("Wide Utra-Fine", "3 m.", "124,800", "124,800"),
            ("Multi-Look Fine", "8 m.", "67,200", "67,200"),
            ("Wide Multi-Look Fine", "8 m.", "120,000", "120,000"),
            ("Fine", "8 m.", "57,600", "57,600"),
            ("Wide", "30 m.", "57,600", "57,600"),
            ("ScanSAR Narrow", "50 m.", "N/A", "57,600"),
            ("ScanSAR Wide", "100 m.", "N/A", "57,600"),
            ("Extended High, Low", "25 m.", "57,600", "57,600"),
            ("Fine Quad-Pol", "8 m.", "86,400", "N/A"),
            ("Wide Fine Quad-Pol", "8 m.", "124,800", "N/A"),
        ]
    ],

    # Page 6: TerraSar X (X band) - standard Archive/Tasking columns
    *[
        dict(Category="ดาวเทียมระบบเรดาร์ - TerraSar X (X band)", Item=item, Resolution=res, Polarization="",
             Price_Label_1=ARCHIVE, Price_Value_1=archive, Price_Label_2=TASKING, Price_Value_2=tasking,
             Unit="บาท/ภาพ", Notes="")
        for item, res, archive, tasking in [
            ("Staring Spotlight (ST)", "0.25 m.", "162,630", "325,260"),
            ("High Res Spotlight (HS)", "1 m.", "139,230", "278,460"),
            ("Spotlight", "2 m.", "99,450", "198,900"),
            ("StripMap", "3 m.", "69,030", "138,060"),
            ("ScanSAR", "18.5 m.", "40,950", "81,900"),
            ("Wide ScanSAR", "40 m.", "40,950", "81,900"),
        ]
    ],

    # Page 6: COSMO SkyMed (X band) - only "New Acquisition" price
    dict(Category="ดาวเทียมระบบเรดาร์ - COSMO SkyMed (X band)", Item="Spotlight-2", Resolution="1x1 m.",
         Polarization="HH, VV", Price_Label_1="New Acquisition (บาท)", Price_Value_1="180,000",
         Price_Label_2="", Price_Value_2="", Unit="บาท/ภาพ", Notes=""),
    dict(Category="ดาวเทียมระบบเรดาร์ - COSMO SkyMed (X band)", Item="StripMap Himage", Resolution="3 x 3 – 5 x 5 m.",
         Polarization="HH, HV, VH, VV", Price_Label_1="New Acquisition (บาท)", Price_Value_1="93,000",
         Price_Label_2="", Price_Value_2="", Unit="บาท/ภาพ", Notes=""),
    dict(Category="ดาวเทียมระบบเรดาร์ - COSMO SkyMed (X band)", Item="StripMap PingPong", Resolution="10 x 12 – 20 x 20 m.",
         Polarization="2 ช่องสัญญาณ polarimetric: HH,VV หรือ HH,HV หรือ VV,VH",
         Price_Label_1="New Acquisition (บาท)", Price_Value_1="68,000",
         Price_Label_2="", Price_Value_2="", Unit="บาท/ภาพ", Notes=""),
    dict(Category="ดาวเทียมระบบเรดาร์ - COSMO SkyMed (X band)", Item="ScanSAR Wide", Resolution="14 x 22 – 30 x 30 m.",
         Polarization="HH, HV, VH, VV", Price_Label_1="New Acquisition (บาท)", Price_Value_1="78,000",
         Price_Label_2="", Price_Value_2="", Unit="บาท/ภาพ", Notes=""),
    dict(Category="ดาวเทียมระบบเรดาร์ - COSMO SkyMed (X band)", Item="ScanSAR Huge", Resolution="14 x 38 – 100 x 100 m.",
         Polarization="HH, HV, VH, VV", Price_Label_1="New Acquisition (บาท)", Price_Value_1="78,000",
         Price_Label_2="", Price_Value_2="", Unit="บาท/ภาพ", Notes=""),

    # Page 7: GaoFen-3 (C band) - Archive/Tasking with Polarization
    *[
        dict(Category="ดาวเทียมระบบเรดาร์ - GaoFen-3 (C band)", Item=item, Resolution=res, Polarization=pol,
             Price_Label_1=ARCHIVE, Price_Value_1=archive, Price_Label_2=TASKING, Price_Value_2=tasking,
             Unit="บาท/ภาพ", Notes="")
        for item, res, pol, archive, tasking in [
            ("Spotlight (SL)", "1 m.", "HH, VV", "116,400", "180,500"),
            ("Ultra-fine Stripmap (UFS)", "3 m.", "HH, VV", "68,900", "118,800"),
            ("Fine Stripmap (FSI)", "5 m.", "HH, VV", "64,200", "95,000"),
            ("Wide Fine Stripmap (FSII)", "10 m.", "HH, HV / VV, VH", "64,200", "90,300"),
            ("Standard Stripmap (SS)", "25 m.", "HH, HV / VV, VH", "54,700", "85,500"),
            ("Narrow ScanSAR (NSC)", "50 m.", "HH, HV / VV, VH", "32,100", "42,800"),
            ("Wide ScanSAR (WSC)", "100 m.", "HH, HV / VV, VH", "32,100", "45,800"),
            ("Quad-pol Stripmap (QPSI)", "8 m.", "HH, HV / VV, VH", "71,300", "137,800"),
            ("Wide Quad-pol Stripmap (QPSII)", "25 m.", "HH, HV / VV, VH", "71,300", "137,800"),
            ("Wave (WAV)", "10 m.", "HH, HV / VV, VH", "10,700", "14,300"),
            ("Global Observation (GLO)", "500 m.", "HH, HV / VV, VH", "10,700", "14,300"),
            ("Extended Incidence Angle (EXT)", "25 m.", "HH, HV / VV, VH", "42,800", "57,000"),
        ]
    ],
]

df = pd.DataFrame(rows, columns=[
    "Category", "Item", "Resolution", "Polarization",
    "Price_Label_1", "Price_Value_1", "Price_Label_2", "Price_Value_2",
    "Unit", "Notes",
])

df.to_csv("Gistda_Price_List.csv", index=False, encoding="utf-8-sig")
df.to_excel("Gistda_Price_List.xlsx", index=False, sheet_name="Price List")
df.to_html("Gistda_Price_List.html", index=False, escape=False,
           table_id="price-list", border=0)

print(f"Rows written: {len(df)}")
