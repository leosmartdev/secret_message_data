import requests

def decode_secret_message(url):
    response = requests.get(url)
    data = response.text.splitlines()
    
    grid = {}
    
    start_index = 3
    for i in range(start_index, len(data), 3):
        try:
            x = int(data[i])            # x-coordinate
            char = data[i + 1]          # Character
            y = int(data[i + 2])        # y-coordinate
            
            grid[(x, y)] = char
        except (ValueError, IndexError) as e:
            print(f"Error processing data at index {i}: {e}")
            continue
    
    if grid:
        max_x = max(x for x, y in grid.keys())
        max_y = max(y for x, y in grid.keys())
    else:
        print("No valid data found.")
        return
    
    for y in range(max_y, -1, -1):
        row = ""
        for x in range(max_x + 1):
            row += grid.get((x, y), " ")
        print(row)


# url = "https://docs.google.com/document/d/1TpradsynqnLl7HA-EAjFYzDg9nGJY7453ypN3jPP-QA"
# url = "https://easyfeel.it/test/documenti/secret_message_data.txt"
url = "https://easyfeel.it/test/documenti/secret_message_live.txt"
decode_secret_message(url)
