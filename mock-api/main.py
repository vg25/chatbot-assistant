from fastapi import FastAPI
import pandas as pd

DATASET_PATH = "Order_Data_Dataset.csv"
df = pd.read_csv(DATASET_PATH)
df.fillna(value="", inplace=True)

app = FastAPI()

@app.get("/data")
def get_all_data():
    return df.to_dict(orient="records")

@app.get("/data/customer/{customer_id}")
def get_customer_data(customer_id: int):
    filtered_data = df[df["Customer_Id"] == customer_id]
    if filtered_data.empty:
        return {"error": f"No data found for Customer ID {customer_id}"}
    return filtered_data.to_dict(orient="records")
