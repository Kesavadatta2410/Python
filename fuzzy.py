heights = list(range(130, 201))

def very_short(h):
    return max(0, min(1, (140 - h) / (140 - 130)))

def short(h):
    return max(0, min(1, (h - 130) / (150 - 130), (160 - h) / (160 - 150)))

def normal(h):
    return max(0, min(1, (h - 150) / (160 - 150), (170 - h) / (170 - 160)))

def tall(h):
    return max(0, min(1, (h - 160) / (170 - 160), (185 - h) / (185 - 170)))

def very_tall(h):
    return max(0, min(1, (h - 185) / (200 - 185)))

very_short_membership = [very_short(h) for h in heights]
short_membership = [short(h) for h in heights]
normal_membership = [normal(h) for h in heights]
tall_membership = [tall(h) for h in heights]
very_tall_membership = [very_tall(h) for h in heights]

heights_to_check = [130, 145, 160, 175, 190]
manual_values = {
    'Very Short': [very_short(h) for h in heights_to_check],
    'Short': [short(h) for h in heights_to_check],
    'Normal': [normal(h) for h in heights_to_check],
    'Tall': [tall(h) for h in heights_to_check],
    'Very Tall': [very_tall(h) for h in heights_to_check]
}

print("Manual Membership Values:")
for height, values in zip(heights_to_check, zip(*manual_values.values())):
    print(f"Height {height} cm: Very Short={values[0]:.2f}, Short={values[1]:.2f}, Normal={values[2]:.2f}, Tall={values[3]:.2f}, Very Tall={values[4]:.2f}")
