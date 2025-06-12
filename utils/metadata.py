def unique_brands(data):
    unique_brands = data["brand"].nunique()
    top_brands = data["brand"].value_counts().head()
    return unique_brands, top_brands


def unique_categories(data):
    unique_categories = data["categories"].nunique()
    sample_categories = data["categories"].sample(5, random_state=42)
    return unique_categories, sample_categories


def unique_primary_categories(data):
    unique_primary_categories = data["primaryCategories"].nunique()
    unique_categories_distribution = data["primaryCategories"].value_counts()
    return unique_primary_categories, unique_categories_distribution


def unique_manufacturers(data):
    unique_manufacturers = data["manufacturer"].nunique()
    top_manufacturers = data["manufacturer"].value_counts().head()
    return unique_manufacturers, top_manufacturers


def unique_product_names(data):
    unique_product_names = data["name"].nunique()
    sample_product_names = data["name"].sample(5, random_state=42)
    return unique_product_names, sample_product_names
 