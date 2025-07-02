# Problem Set Unit 4, Session 2, Version 1 Advanced

#problem 1 -----------------------------------------------------
def filter_sustainable_brands(brands, criterion):
    result = []
    for brands in brands:
        if criterion in brands["criteria"]:
            result.append(brands["name"])
    return result

brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

print(filter_sustainable_brands(brands, "eco-friendly"))
print(filter_sustainable_brands(brands_2, "ethical labor"))
print(filter_sustainable_brands(brands_3, "carbon-neutral"))

# time and spce complexity
# time: O(n) bc of line 3
# space: O(n) bc line 3

#problem 2 -----------------------------------------------------
def count_material_usage(brands):
    result = {}
    for brand in brands:
        for material in brand["materials"]:
            if material in result:
                result[material] += 1
            else:
                result[material] = 1
    return result

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(count_material_usage(brands))
print(count_material_usage(brands_2))
print(count_material_usage(brands_3))

# time and spce complexity
# time: O(n)^2 bc of line 40 and 41
# space: O(n) bc line 39

#problem 3 -----------------------------------------------------
def find_trending_materials(brands):
    freq = {}         # Dictionary to store how often each material appears
    results = []      # List to store materials that appear more than once

    for brand in brands:
        for material in brand["materials"]:
            if material in freq:
                freq[material] += 1
            else:
                freq[material] = 1

    # Loop through the dictionary to find materials that appear more than once
    for key, value in freq.items():
        if value > 1:
            results.append(key)

    return results

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(find_trending_materials(brands))
print(find_trending_materials(brands_2))
print(find_trending_materials(brands_3))

# time and spce complexity
# time: O(n)^2, bc of line 78 and 79
# space: O(n) frew and results are both n

#problem 4 -----------------------------------------------------
def find_best_fabric_pair(fabrics, budget):
    fabrics = sorted(fabrics, key=lambda x: x[1])

    #Initialize two pointers
    left = 0                    # Start pointer
    right = len(fabrics) - 1    # End pointer

    best_pair = ()              # Best fabric pair
    best_sum = 0              # Best total cost found so far

    # Step 3: Move pointers to find best pair under budget
    while left < right:
        if fabrics[left][1] + fabrics[right][1] > best_sum and fabrics[left][1] + fabrics[right][1] <= budget:
            best_sum = fabrics[left][1] + fabrics[right][1]
            best_pair = (fabrics[left][0], fabrics[right][0])

        if fabrics[left][1] + fabrics[right][1] > budget:
            right -= 1
        else:
            left += 1

    return best_pair
        

fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))

# time and spce complexity

# time: O(n log n), bc of the sorting
# space: O(1) aka constant 

#problem 5 -----------------------------------------------------
def organize_fabrics(fabrics):
    # Sort the list by the eco-friendliness rating in descending order
    fabrics = sorted(fabrics, key=lambda x: x[1], reverse=True)

    # Return just the names of the fabrics in that order
    return [fabric[0] for fabric in fabrics]


fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

print(organize_fabrics(fabrics))
print(organize_fabrics(fabrics_2))
print(organize_fabrics(fabrics_3))

# time and spce complexity

# time: O(n log n), bc of the sorting
# space: O(n) because we store a new list of b=fabric nameds in the result