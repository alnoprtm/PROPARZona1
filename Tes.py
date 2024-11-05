import streamlit as st
import pandas as pd
from datetime import datetime

# Judul aplikasi
st.title("Input Data Harian Produksi Minyak - PROPAR dan Low & Off")

# Membuat input untuk bagian PROPAR
st.subheader("PROPAR")

# Bagian 1: Pilihan WK/Field
wk_field = st.selectbox("WK/Field", ["Jambi", "Kampar", "Lirik", "Pangkalan Susu", "Rantau", "Siak"])

# Bagian 2: Structure/PF, berubah sesuai WK/Field yang dipilih
structure_choices = {
    "Jambi": ["BBT", "BJG", "BTJ", "KAS", "KTB", "KTT", "PPS", "SG", "SGL", "SKB", "STT", "TPN"],
    "Kampar": ["Binio", "EKA", "Gemuruh", "Kerumutan", "Merbau", "North Merbau", "Panduk", "Parum", "Pekan"],
    "Lirik": ["Andan/Ukui", "Lirik", "Molek", "North Pulai", "Sago", "South Pulai"],
    "Pangkalan Susu": ["Benggala", "Gebang", "Paluh Tabuhan Timur", "Pantai Pakam Timur", "Pulau Panjang"],
    "Rantau": ["Kuala Dalam", "Kuala Simpang Barat", "Pematang Panjang", "Rantau", "Serang Jaya", "Sungai Buluh"],
    "Siak": ["Batang", "Lindai"]
}
structure = st.selectbox("Structure/PF", structure_choices[wk_field])

# Event Date
event_date = st.date_input("Event Date", datetime.now())

# System Source dan Equipment Source
system_source = st.selectbox("System Source", ["Plant", "Reservoir", "Terminal", "Well"])
equipment_source_options = {
    "Plant": ["Piping", "Pipeline", "Central Power Generator", "Gas Compressors", "Air Compressor", 
              "Fin Fan Cooler", "Heat Exchanger", "Tanks", "Pressure Vessel", "Pig Receiver Launcher", 
              "Instrumentation and Controls", "Pre-Production", "Safety System", "Total Assets", 
              "Structure / Platform and Civil", "Main Pump", "Pump Others", "Third Party Equipment"],
    "Reservoir": ["Gas Zone", "Oil Zone"],
    "Terminal": ["Floating Storage and Offloading", "Single Point Mooring", "Onshore Terminal", "Onshore Receiving Facility"],
    "Well": ["Progressive Cavity Pump", "Electrical Submersible Pump", "Oil Natural Flow", "Gas Natural Flow", 
             "Gas Lift", "Hydraulic Jet Pump", "Sucker Rod Pump", "Hydraulic Pumping Unit", "Plunger Lift", 
             "Injection Well", "Other Artificial Lift", "Pre-Production"]
}
equipment_source = st.selectbox("Equipment Source", equipment_source_options[system_source])

# Type Cause, Family Cause, dan Parent Cause
type_cause = st.radio("Type Cause", ["Planned", "Unplanned"])

family_cause_options = [
    "Reservoir Intervention", "Reservoir Issues", "Well Program & Surveillance", "Well Integrity", 
    "External Issue", "Artificial Lift & Downhole Problem", "Rotating & Machinery Integrity", 
    "Inspection & Maintenance", "Static & Facility Integrity", "Process Issues", "Power & Electrical Integrity", 
    "Turn Around & Modification"
]
family_cause = st.selectbox("Family Cause", family_cause_options)

parent_cause_options = {
    "Reservoir Intervention": ["Well Surveillance / Data Acquisition / Survey / Inspection"],
    "Reservoir Issues": ["Reservoir Properties", "Formation Damage", "Pressure Depletion", "Water Cut Increase", 
                         "Gas Oil Ratio (GOR) Increase", "Formation Integrity", "Production Fluctuation", 
                         "Condensate Gas Ratio (CGR) Increase"],
    "Well Program & Surveillance": ["Well Surveillance / Data Acquisition / Survey / Inspection", "Optimization / Construction",
                                    "Project Schedule Delays", "Wells Schedule Delays", "Facilities Schedule Delays"],
    "Well Integrity": ["Well Integrity", "Flow Assurance"],
    "External Issue": ["Natural Events", "Security & Regulation", "Material Availability issue", 
                       "Curtailment / Top Tank"],
    "Artificial Lift & Downhole Problem": ["Artificial Lift Downhole Problem", "Artificial Lift Surface Equipment Problem"],
    "Rotating & Machinery Integrity": ["General Machinery Problem", "Fuel System Problem", "Optimization / Construction",
                                       "Project Schedule Delays", "Facilities Schedule Delays", "Turbomachinery Problem"],
    "Inspection & Maintenance": ["Inspection & Maintenance", "Static/Dynamic Measurement & Calculation"],
    "Static & Facility Integrity": ["Optimization / Construction", "Facility Integrity Problem", 
                                    "Project Schedule Delays", "Facilities Schedule Delays", 
                                    "Static Measurement & Calculation", "Dynamic Measurement & Calculation", 
                                    "General Machinery Problem", "Gas Measurements & Calculations"],
    "Process Issues": ["Bottle Neck", "Flow Assurance", "Water Handling Problem"],
    "Power & Electrical Integrity": ["Optimization / Construction", "Instrument & Control Systems", 
                                     "Electrical Distribution & Transmission Problem", 
                                     "Project Schedule Delays", "Facilities Schedule Delays"],
    "Turn Around & Modification": ["Turnaround"]
}
parent_cause = st.selectbox("Parent Cause", parent_cause_options.get(family_cause, ["N/A"]))

child_cause_options = {
    "Artificial Lift Downhole Problem": [
        "Abrasives", "Ball And Seat", "Bumper Spring (Broken / Failure)", "Cable Problem", "Coupling / Centralizer",
        "Elastomer", "ESP Packer (Gas Tube Plugging / Leak)", "Fishing", "Gas / Liquid Lock / Pound", "Gas Lock",
        "Leak / Plugging on Nozzle (Fluid Deposit)", "Leak on Barrel Pump", "Leak on Standing / Traveling Valve",
        "Motor (Burned, Overload, High Temperature, Underload, Stall)", "Operating Valve Leaked / Plugged",
        "Others Downhole Problem", "Plunger Pump Problem (Stuck)", "Pump Problem (Corrosion, Abrasive, Scale, Stuck, Up/Downtrust)",
        "Pump Spacing", "Rod (Broken, Unscrew) Problem", "Rod String", "Rotor (Broken, Stuck, Rubbing, Etc)",
        "Stator (Wear Out, Oversize, Abrasive, Corrosion)", "Sucker Rod (Broken, Unscrew) Problem", "Unloading Valve Leaked / Plugged"
    ],
    "Artificial Lift Surface Equipment Problem": [
        "Catcher Damage", "Controller Problem", "Electrical and Instrument Problem", "Fluid Injection Pump Problem",
        "Gearbox Problem", "High Ampere", "High Pressure Hose Leak", "Indirect Impact After Power Outage", "Junction Box Problem",
        "Leak on BOP Rubber", "Leak on Stuffing Box", "Line Gas Injection Leaked / Plugged", "Low Reading", "Lubricator Problem",
        "Motor Valve Problem (Pneumatic, Leak, Valve Size, Etc)", "Others Surface Equipment Problem", "Overload",
        "Pneumatic Instrumentation Problem", "Polished Rod Problem", "Primover Problem", "Problem in Hydraulic System",
        "Sensor Problem (Velocity / Arrival Sensor)", "Switch Box Problem", "Unbalanced Counter Weight", "Unbalanced Reading",
        "Under Load", "Variable Frequency Drive (VFD) Problem", "Variable Speed Drive (VSD) Problem", "Vibration Switch Problem",
        "Wellhead Drive Problem"
    ],
    "Bottle Necking": [
        "Capacitation Limit in Facility", "Capacity Limitation in Facilities", "Others Bottle Necking",
        "Process Upset / Overcapacity"
    ],
    "Condensate Gas Ratio (CGR) Increase": [
        "Change of Bottom Hole Temperature", "Condensate Banking"
    ],
    "Curtailment / Top Tank": [
        "Buyer Low Demand", "Inaccurate Metering System Operation", "OPEC",
        "Process Disruption at Buyer / Customer Facilities", "Regulatory Change / Other", "Transportation Delay"
    ],
    "Dynamic Measurement & Calculation": [
        "Fail on Reading ASTM Table and Oil Volume Calculation", "Oil Analysis is Not Accurate"
    ],
    "Electrical Distribution & Transmission Problem": [
        "Disturbance on Offshore Transmission (Underwater Transmission Cable)",
        "Disturbance on Onshore Transmission (Electrical Pole, Transmission Cable, Etc)",
        "Disturbance on Power Supply (Internal / Eksternal)", "Electrical System Problem (Supply / Connect / Panel / Cable / Switch / JB)",
        "Electrical and Instrument Problem", "Gas Shortage", "Others Electrical Distribution & Transmission Problem"
    ],
    "Facilities Schedule Delays": [
        "Facilities Schedule Day"
    ],
    "Facility Integrity Problem": [
        "Construction Activity (SIMOPS)", "Corrosion / Thinning / Fatigue / Crack",
        "Erosion / Abrasive Prevention", "Leaks at Facility Equipment", "Others Facility Integrity Problem",
        "Problem on Hose Connection", "Structural Damage (Foundation / Skid / Frame / Shelter)"
    ],
    "Flow Assurance": [
        "Anorganic Scale (CaCO3, Mg2CO3, BaSO4)", "Fine Solids (Sand, Salt)", "Fluid not Support", "Free Water in Tanks",
        "Hydrates", "Liquid (Condensate / Hydrate)", "Not Pumping", "Organic Scale (Paraffin, Wax, Asphaltene)",
        "Others Flow Assurance Problem", "Problem on Hose Connection", "Sand Problem in Tank", "Scale / Deposit / Plugging In Production Pipeline",
        "Sludge / Wax in Tank", "Solid Particles in Pipeline", "Water handling problem"
    ],
    "Formation Damage": [
        "Anorganic Scale (CaCO3, Mg2CO3, BaSO4)", "Drilling Damage (Clay Swelling, Mud Filtrate Skin)",
        "Fine Solids (Sand, Salt)", "Organic Scale (Paraffin, Wax, Asphaltene)"
    ],
    "Formation Integrity": [
        "Cap Rock Failure", "Fault Failure", "Induced Fracture"
    ],
    "Fuel System Problem": [
        "Gas Shortage", "High Impurities Composition", "Low Calorific / Heat Gas Value", "Others Fuel System Problem"
    ],
    "Gas Measurements & Calculations": [
        "Fail on Reading TABLE AGA-3, AGA-7, AGA-9, Gas Rate Calculation", "Gas Analysis is Not Accurate",
        "Inaccurate Metering System Operation"
    ],
    "Gas Oil Ratio (GOR) Increase": [
        "Gas Breakthrough", "Gas Cap Expansion", "Gas Coning", "Poor Cement Bonding", "Saturated Reservoir (Pr below Pb)"
    ],
    "General Machinery Problem": [
        "Anomaly Temperature", "Electrical and Instrument Problem", "High Vibration", "Others General Machinery Problem",
        "Problem in Lubrication System", "Problem in Mechanical System", "Problem on Hose Connection",
        "Problem on Process Supply (Water / Air / Rate / Volume / Pressure / Temperature / Density)",
        "Problem with Cooling & Sealing Air System", "Vibration Monitoring"
    ],
    "Inspection & Maintenance": [
        "Fail on Reading TABLE AGA-3, AGA-7, AGA-9, Gas Rate Calculation", "Failure in Control Room Building",
        "Modifications / Upgrade", "New Installation", "Others Inspection & Maintenance",
        "Planned Repair Work (TAR)", "PM / Inspection / Testing / Recertification Jobs",
        "Predictive Maintenance (PdM) Jobs", "Safety Testing", "Solid / Debris / Plug", "Well Testing"
    ],
    "Instrument & Control Systems": [
        "Air Supply (Engine Starting) Problem", "Automation Control / Safety Device problem",
        "Field Instrument (PI, TI, PT, TT, FT, meter unit) Problem", "Malfunction Fire Gas System (False Alarm, Fire Gas Detector)",
        "Metering System Problem & Expired", "Others Instrument & Control System Problem", "Pneumatic Instrumentation Problem",
        "Tubing Instrument & Connection Problem", "Wiring Instrumentation System Problem"
    ],
    "Material Availability Issue": [
        "Contract Issue", "Material / Tools / Equipment / Transport, etc", "Supply Gas Limitation", "Support Boat Problem"
    ],
    "Natural Events": [
        "Earthquake / Landslide / Subsidence", "Lightning", "Others Natural Event", "Safety and Environmental",
        "Seas / Waves", "Weather / Storms / Floods", "Wild Fires", "Wildlife / Animal Disturbance"
    ],
    "Optimization / Construction": [
        "Capacity Change", "Change of Choke / Bean size", "Corrosion / Thinning / Fatigue / Crack",
        "Erosion / Abrasive Prevention", "Fishing", "Modifications / Upgrade", "New Installation", "Replacement Artificial Lift",
        "Replacement Tubular", "SIMOPS On Well Work", "Treating - Emulsion", "Treating - Hydrates", "Treating - Paraffin",
        "Treating - Scale", "Well Services", "Workover"
    ],
    "Pressure Depletion": [
        "Change of Reservoir Drive Mechanism", "Gas Shortage", "Injectivity Problems",
        "Reservoir Pressure Decline", "Small Compartmentalization"
    ],
    "Production Fluctuation": [
        "Production Fluctuation"
    ],
    "Project Schedule Delays": [
        "Project Schedule Delays"
    ],
    "Reservoir Properties": [
        "Heavy Oil / Highly Viscous Oil / Congealing", "Low Permeability / Low Influx"
    ],
    "Security & Regulation": [
        "Authority Restrictions", "Environmental Permits / Limits", "Leaks at Facility Equipment",
        "Material / Tools / Equipment / Transport, etc", "Others Security & Regulation",
        "Sabotage / Security Breach / Stealing / Fire", "Social Problem", "Support Boat Problem"
    ],
    "Static / Dynamic Measurement & Calculation": [
        "Fail on Reading ASTM Table and Oil Volume Calculation", "Inaccurate Measurement of Level & Oil Temperature in Tanks",
        "Inaccurate Metering System Operation", "Inaccurate Vessel Positioning (Draft, Inclination)",
        "Inappropriate Oil Sampling in Floating Tanks", "Measuring Instrument in Tanks and Labs Below The Standard",
        "Oil Analysis is not Accurate", "Problem on Measurement / Instrument Tools in Tank & Labs / Expired"
    ],
    "Static Measurement & Calculation": [
        "Inaccurate Measurement of Level & Oil Temperature in Tanks", "Inaccurate Vessel Positioning (Draft, Inclination)",
        "Inappropriate Oil Sampling in Floating Tanks"
    ],
    "Turbomachinery Problem": [
        "Air Inlet System Problem",
        "Anomaly Temperature",
        "High Vibration",
        "Problem in Hydraulic System",
        "Problem in Lubrication System",
        "Problem in Mechanical System",
        "Problem on Process Supply (Water / Air / Rate / Volume / Pressure / Temperature / Density)",
        "Problem with Cooling & Sealing Air System"
    ],
    "Turnaround & Modification": [
        "Turnaround"
    ],
    "Water Cut Increase": [
        "Liquid Hold Up / Liquid Loading",
        "Poor Cement Bonding",
        "Water Blocking",
        "Water Breakthrough",
        "Water Channeling",
        "Water Coning"
    ],
    "Water Handling Problem": [
        "Problem on Oil dehydration process",
        "Wastewater Quality Below The Standard"
    ],
    "Well Integrity": [
        "Anorganic Scale (CaCO3, Mg2CO3, BaSO4)",
        "Fine Solids (Sand, Salt)",
        "Hydrates",
        "Leak / Corroded On Production Pipe (RPP, Packer, SSDV, Tubing Liner, Downhole Central Line)",
        "Leak / Corrosion on Casing (Surface / Intermediate / Production Casing / Liner)",
        "Leak / Corrosion on Wellhead & XM Tree (C / W Accessories)",
        "Maximum Allowable Annulus Surface Pressure (MAASP)",
        "Maximum Allowable Surface Pressure (MASP)",
        "Maximum Allowable Wellhead Operating Pressure (MAWOP)",
        "Organic Scale (Paraffin, Wax, Asphaltene)",
        "Poor Cement Bonding"
    ],
    "Well Surveillance / Data Acquisition / Survey / Inspection": [
        "Caliper / Corrosion / Restriction",
        "Compliance Testing",
        "Depth / Fill",
        "Logging",
        "Others Log or Survey",
        "PLT / Temperature / Tracer",
        "Pressure Survey",
        "Saturation",
        "Static, Flowing, Temperature, Bottom Hole Pressure (BHP Survey) Measurement",
        "Temperature Survey",
        "Vertical Seismic Profile Log",
        "Well Testing"
    ],
    "Wells Schedule Delays": [
        "Wells Schedule Delays"
    ]
}

child_cause = st.selectbox("Child Cause", child_cause_options.get(parent_cause, ["N/A"]))

# Diagnostic Status, Priority, Remedial Status
diagnostic_status = st.selectbox("Diagnostic Status", ["Approved", "Blanks"])
priority = st.selectbox("Priority", ["Drop", "High", "Medium"])
remedial_status = st.selectbox("Remedial Status", ["Approved", "Blanks"])

# Additional fields for PROPAR
pi_percent = st.number_input("PI%", min_value=0.0)
prod_struc_oil = st.number_input("Prod Struc Oil (BOPD)", min_value=0.0)
# Tambahkan variabel lain sesuai dengan rincian input yang Anda inginkan

# Button untuk menyimpan data
if st.button("Simpan Data"):
    data = {
        "WK/Field": wk_field,
        "Structure/PF": structure,
        "Event Date": event_date,
        "System Source": system_source,
        "Equipment Source": equipment_source,
        "Type Cause": type_cause,
        "Family Cause": family_cause,
        "Parent Cause": parent_cause,
        "Child Cause": child_cause,
        "Diagnostic Status": diagnostic_status,
        "Priority": priority,
        "Remedial Status": remedial_status,
        "PI%": pi_percent,
        "Prod Struc Oil (BOPD)": prod_struc_oil,
        # Tambahkan variabel lain sesuai dengan rincian input
    }
    # Mengubah data ke dalam format DataFrame
    df = pd.DataFrame([data])
    # Simpan data ke dalam file Excel
    with pd.ExcelWriter("data_produksi.xlsx", mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
        df.to_excel(writer, index=False, header=False, startrow=writer.sheets["Sheet1"].max_row)
    st.success("Data berhasil disimpan!")