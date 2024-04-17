def gather_store_items():
  
  item_locations = {}
  shopping_list = []

  num_shelves = int(input("Počet regálů: "))
  for shelf_index in range(num_shelves):
    print(f"Zadejte zboží pro regál {shelf_index}:")
    shelf_items = []
    while True:
      item = input().lower()
      if not item:
        break
      shelf_items.append(item)
    for item in shelf_items:
      item_locations[item] = shelf_index 

  print("Zboží, které chcete koupit:")
  while True:
    item = input().lower()
    if not item:
      break
    shopping_list.append(item)

  return item_locations, shopping_list

def find_item_location(item_placements, desired_item):
 
  for item in item_placements:
    if desired_item in item:  
      return item_placements[item]
  return float('inf')

def plan_shopping_trip(item_placements, shopping_list):
  
  optimized_plan = []
  sorted_list = sorted(shopping_list, key=lambda item: find_item_location(item_placements, item))
  for item in sorted_list:
    shelf_number = find_item_location(item_placements, item)
    optimized_plan.append((shelf_number, item))
  return optimized_plan

def main_function():
  
  item_locations, shopping_list = gather_store_items()
  optimized_purchases = plan_shopping_trip(item_locations, shopping_list)

  print("Optimalizovaný nákupní seznam:")
  for i, (shelf, item) in enumerate(optimized_purchases):
    print(f"{i+1}. {item.upper()} -> Regal #{shelf} ({item})") 

if __name__ == "__main__":
  main_function()

