import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def get_product(prod_id):
    """Fetch a single product by prod_id."""
    resp = sb.table("products").select("*").eq("prod_id", prod_id).execute()
    return resp.data[0] if resp.data else None

def update_stock(prod_id, new_stock):
    resp = sb.table("products").update({"stock": new_stock}).eq("prod_id", prod_id).execute()
    return bool(resp.data)


if __name__ == "__main__":
    pid = int(input("Enter the product id to update: ").strip())
    product = get_product(pid)
    
    if not product:
        print(f"No product found with prod_id {pid}")
    else:
        print(f"Selected product: {product}")
        new_stock = int(input("Enter the new stock value: ").strip())
        if update_stock(pid, new_stock):
            print(f"Stock for product {pid} updated to {new_stock} successfully!")
        else:
            print("Failed to update stock.")