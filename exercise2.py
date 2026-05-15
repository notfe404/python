import pandas as pd

def main():
    # 1. Create a DataFrame with columns: id, name, price, quantity
    # 2. Add at least 5 products.
    data = {
        'id': [1, 2, 3, 4, 5],
        'name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
        'price': [1200.0, 25.0, 80.0, 250.0, 150.0],
        'quantity': [10, 50, 30, 15, 20]
    }
    df = pd.DataFrame(data)
    
    # 3. Save data to products.csv.
    csv_filename = 'products.csv'
    df.to_csv(csv_filename, index=False)
    print(f"Data successfully saved to {csv_filename}")
    
    # 4. Read the CSV file
    df_read = pd.read_csv(csv_filename)
    
    # Display all products
    print("\n--- All Products ---")
    print(df_read)
    
    # Display products with price > 100
    print("\n--- Products with price > 100 ---")
    expensive_products = df_read[df_read['price'] > 100]
    print(expensive_products)
    
    # Calculate the total inventory value
    # The total value of the inventory is the sum of (price * quantity) for all items.
    total_inventory_value = (df_read['price'] * df_read['quantity']).sum()
    print(f"\n--- Total Inventory Value ---")
    print(f"${total_inventory_value:,.2f}")
    
    # 5. Add a new column: total = price * quantity
    df_read['total'] = df_read['price'] * df_read['quantity']
    print("\n--- DataFrame with new 'total' column ---")
    print(df_read)

if __name__ == "__main__":
    main()
