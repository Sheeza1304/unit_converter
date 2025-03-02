import streamlit as st#type: ignore

def main():
    st.title("Unit Converter🚀")
    
    # Select conversion type
    conversion_type = st.selectbox(
        "Select Conversion Type",
        ["Weight", "Length", "Temperature"]
    )
    
    # Input value
    input_value = st.number_input("Enter value to convert:", value=1.0)
    
    # Define conversion dictionaries
    weight_conversion = {
        "Kilogram": 1.0,
        "Gram": 0.001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }
    
    length_conversion = {
        "Meter": 1.0,
        "Centimeter": 0.01,
        "Kilometer": 1000.0,
        "Mile": 1609.34,
        "Foot": 0.3048,
        "Inch": 0.0254
    }
    
    # Set up appropriate units based on conversion type
    if conversion_type == "Weight":
        from_unit = st.selectbox("From:", list(weight_conversion.keys()))
        to_unit = st.selectbox("To:", list(weight_conversion.keys()))
        
        if st.button("Convert"):
            result = input_value * (weight_conversion[from_unit] / weight_conversion[to_unit])
            st.success(f"{input_value} {from_unit} = {result:.6f} {to_unit}")
            
    elif conversion_type == "Length":
        from_unit = st.selectbox("From:", list(length_conversion.keys()))
        to_unit = st.selectbox("To:", list(length_conversion.keys()))
        
        if st.button("Convert"):
            result = input_value * (length_conversion[from_unit] / length_conversion[to_unit])
            st.success(f"{input_value} {from_unit} = {result:.6f} {to_unit}")
            
    elif conversion_type == "Temperature":
        temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
        from_unit = st.selectbox("From:", temp_units)
        to_unit = st.selectbox("To:", temp_units)
        
        if st.button("Convert"):
            # Convert to Celsius first
            if from_unit == "Celsius":
                celsius = input_value
            elif from_unit == "Fahrenheit":
                celsius = (input_value - 32) * 5/9
            else:  # Kelvin
                celsius = input_value - 273.15
                
            # Convert from Celsius to target unit
            if to_unit == "Celsius":
                result = celsius
            elif to_unit == "Fahrenheit":
                result = celsius * 9/5 + 32
            else:  # Kelvin
                result = celsius + 273.15
                
            st.success(f"{input_value} {from_unit} = {result:.6f} {to_unit}")

if __name__ == "__main__":
    main()