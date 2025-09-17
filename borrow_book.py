import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)


def borrow_book(member_id: int, book_id: int):
    """Borrow a book using Supabase RPC transaction."""
    try:
        response = sb.rpc(
            "borrow_book_tx",
            {"p_member_id": member_id, "p_book_id": book_id}
        ).execute()

        if response.data:
            print(" Result:", response.data)
        else:
            print(" No response from transaction.")
    except Exception as e:
        print(" Error borrowing book:", e)

if __name__ == "__main__":
    borrow_book(1, 2)
