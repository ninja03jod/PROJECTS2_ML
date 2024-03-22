import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Define the Streamlit app
def main():
    st.title('Fastag Fraud Detection')
    
    # Display the form for user input
    with st.form(key='fraud_detection_form'):
        st.header('Fastag Fraud Detection Prediction')
        
        # Add dropdowns for categorical features
        hour = st.selectbox('Hour', [11, 14, 18, 2, 6, 10, 15, 20, 1, 7, 12, 17, 22, 4, 8, 13, 16, 21, 3, 23, 5, 9, 19, 0])
        month = st.selectbox('Month', [1, 2, 3, 4, 5, 6, 8, 9, 10, 7, 11, 12])
        day_of_week = st.selectbox('Day of Week', [4, 5, 6, 0, 1, 2, 3])
        vehicle_type = st.selectbox('Vehicle Type', ['Bus', 'Car', 'Motorcycle', 'Truck', 'Van', 'Sedan', 'SUV'])
        toll_booth_id = st.selectbox('TollBooth ID', ['A-101', 'B-102', 'D-104', 'C-103', 'D-105', 'D-106'])
        lane_type = st.selectbox('Lane Type', ['Express', 'Regular'])
        vehicle_dimensions = st.selectbox('Vehicle Dimensions', ['Large', 'Small', 'Medium'])

        geographical_location_options = [
            '13.059816123454882, 77.77068662374292',
            '13.042660878688794, 77.47580097259879',
            '12.84197701525119, 77.67547528176169',
            '12.936687032945434, 77.53113977439017',
            '13.21331620748757, 77.55413526894684'
        ]
        geographical_location = st.selectbox('Geographical Location', geographical_location_options)
        
        # Add input fields for numeric features
        fastag_id = st.number_input('Fastag ID', min_value=0)
        transaction_amount = st.number_input('Transaction Amount', min_value=0)
        amount_paid = st.number_input('Amount Paid', min_value=0)
        vehicle_speed = st.number_input('Vehicle Speed', min_value=0)
        
        # Add submit button
        submit_button = st.form_submit_button(label='Predict')
                   
    # Process the form submission
    if submit_button:
        data = CustomData(
            Hour=hour,
            Month=month,
            DayOfWeek=day_of_week,
            Vehicle_Type=vehicle_type,
            FastagID=fastag_id,
            TollBoothID=toll_booth_id,
            Lane_Type=lane_type,
            Vehicle_Dimensions=vehicle_dimensions,
            Transaction_Amount=transaction_amount,
            Amount_paid=amount_paid,
            Geographical_Location=geographical_location,
            Vehicle_Speed=vehicle_speed
        )
        
        pred_df = data.get_data_as_data_frame()
        st.write(pred_df)  # Display the DataFrame
        
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        st.write(f'The prediction is {results[0]}')
        if results == 0:
            st.write('The Transaction is Fradulent')
        else:
            st.write("The Transaction is is not Fradulent")

# Run the app
if __name__ == '__main__':
    main()

    
