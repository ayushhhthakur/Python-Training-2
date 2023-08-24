

# def fill_water_tanks(buildings, r, unit_capacity):
#     building_list = [(i, water) for i, water in enumerate(buildings)]
    
#     building_list.sort(key=lambda x: x[1], reverse=True)
    
#     tanks_filled = 0
#     filled_buildings = []
    
#     for building, water in building_list:
#         tanks_needed = (water + unit_capacity - 1) // unit_capacity 
#         tanks_to_fill = min(r - tanks_filled, tanks_needed) 
        
#         if tanks_to_fill > 0:
#             tanks_filled += tanks_to_fill
#             filled_buildings.append(building)
        
#         if tanks_filled >= r:
#             break
    
#     return filled_buildings

# # Example usage
# n = 5
# water_availabilities = [10, 8, 15, 7, 12]
# r = 3
# unit_capacity = 5

# result = fill_water_tanks(water_availabilities, r, unit_capacity)
# print("Buildings to fill tanks:", result)