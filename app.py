import streamlit as st


# Conversion Factors dictionary for different categories
conversionFactors = {
    "Length": {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Inch": 39.3701, "Foot": 3.28084, "Yard": 1.09361,
        "Mile": 0.000621371, "Micrometer": 1e6, "Nanometer": 1e9, "Nautical Mile": 0.000539957
        },
    "Mass": {
        "Tonne": 1, "Kilogram": 1000, "Gram": 1e6, "Milligram": 1e9, "Microgram": 1e12, "Imperial Ton": 0.984207, "US Ton": 1.10231,
        "Stone": 157.473, "Pound": 2204.62, "Ounce": 35274
        },
    "Temperature": { },
    "Volume": {
        "US Gallon": 1, "US Quart": 4, "US Pint": 8, "US Cup": 15.7725, "Us ounce": 128, "US Tablespoon": 256, "US Teaspoon": 768,
        "Cubic Meter": 0.00378541, "Liter": 3.78541, "Milliliter": 3785.41, "Imperial Gallon": 0.832674, "Imperial Quart": 1.66535,
        "Imperial Pint": 3.3307, "Imperial Cup": 6.66139, "Imperial Fluid Ounce": 160, "Imperial Tablespoon": 320, "Imperial Teaspoon": 960,
        "Cubic Foot": 0.133681, "Cubic Inch": 231
    },

}

st.markdown(
    """
    <style>
    /* Main container */
    .stApp {
        background-color: #f5f5f5;
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    /* Sidebar */
    .stSidebar {
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
    }
    /* Title */
    .stTitle {
        color: #4a90e2;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }
    /* Headers */
    .stHeader {
        color: #4a90e2;
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    /* Input fields */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #ffffff;
        color: #333333;
        border: 1px solid #cccccc;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .stSelectbox>div>div>div {
        cursor: pointer;  /* Pointer cursor for dropdowns */
    }
    /* Buttons */
    .stButton>button {
        background-color: #4a90e2;
        color: #ffffff;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #357abd;
    }
    /* Success message */
    .stSuccess {
        color: #28a745;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-top: 30px;
    }
    /* Footer */
    .stFooter {
        color: #777777;
        font-size: 16px;
        text-align: center;
        margin-top: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# title of the Assignment
st.markdown("<div class='stTitle'>🔄 Unit Converter</div>", unsafe_allow_html=True)



# Initialize session state for category
if "selected_category" not in st.session_state:
    st.session_state.selected_category = list(conversionFactors.keys())[0]  # Default first category

# Sidebar: Select Category using Radio Buttons
sidebar_category = st.sidebar.radio("Choose a Category", list(conversionFactors.keys()), 
                                    index=list(conversionFactors.keys()).index(st.session_state.selected_category))

# Sync session state with sidebar selection
if sidebar_category != st.session_state.selected_category:
    st.session_state.selected_category = sidebar_category

# Main Content: Select Category using Dropdown (Syncs with Sidebar)
category = st.selectbox("Choose a Category", list(conversionFactors.keys()), 
                        index=list(conversionFactors.keys()).index(st.session_state.selected_category))

# Sync dropdown selection with session state
if category != st.session_state.selected_category:
    st.session_state.selected_category = category

st.write(f"Selected Category: **{st.session_state.selected_category}**")


# Condition for Temperature Conversion if selected category is Temperature then only show the Temperature units in the select box else show all the units of the selected category in the select box
if category == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
else:
    from_unit = st.selectbox("From Unit", list(conversionFactors[category].keys()))
    to_unit = st.selectbox("To Unit", list(conversionFactors[category].keys()))


value = st.number_input("Enter Value", min_value = 0)


def convert_units(category, value, from_unit, to_unit):
    if category == "Temperature":
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    else:
        base_value = value / conversionFactors[category][from_unit]  # Convert to base unit
        return base_value * conversionFactors[category][to_unit]  # Convert to target unit


if st.button("Convert"):
    converted_value = convert_units(category, value, from_unit, to_unit)
    st.markdown(f"<div class='stSuccess'>✅ {value} {from_unit} = {converted_value:.2f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='stFooter'>🔹 Created by Mehmood Fazlani ❤️ using Streamlit</div>", unsafe_allow_html=True)