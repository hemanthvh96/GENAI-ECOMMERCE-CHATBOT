import pandas as pd
from langchain_core.documents import Document

def dataconverter():
    data_url="C:\\VHS\\Courses\\AI\\Projects\\ECommerce Chatbot\\data\\flipkart_product_review.csv"
    product_data = pd.read_csv(data_url)
    data = product_data[["product_title", "review"]]

    products_list = []

    for index, row in data.iterrows():
        products_list.append({
            "product_name": row.product_title,
            "review": row.review
        })
    
    docs = []

    for entry in products_list:
        metadata = {"product_name": entry["product_name"]}
        doc = Document(page_content=entry["review"], metadata=metadata)
        docs.append(doc)
    
    return docs
