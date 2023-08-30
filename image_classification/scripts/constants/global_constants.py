TEMPLATE_FOLDER = "/templates/"
STATIC_FOLDER = "image_classification\static"
STATIC_FOLDER_IMAGES = "static\images"
global_dimension = ""

def set_global(val):
    global global_dimension
    global_var = val
    # return "Value set!"

def get_global():
    return global_dimension
