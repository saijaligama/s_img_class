TEMPLATE_FOLDER = "/templates/"
STATIC_FOLDER = "image_classification\static"
STATIC_FOLDER_IMAGES = "static\images"
STATIC_FOLDER_IMAGES_SPLITIMAGES = "static\images\split_images"
RECONSTRUCTED_IMAGES_FOLDER =  'static\images\Reconstructed_Images'
JSON_MODEL = 'static\cnn_models\model.json'
CNN_MODEL = 'static\cnn_models\model.h5'
CNN_PREDICTION_MODEL = 'static\cnn_models\cnn.h5'
CLASSIFIED_IMAGES = 'static\images\classified_images'
global_dimension = ""

def set_global(val):
    global global_dimension
    global_var = val
    # return "Value set!"

def get_global():
    return global_dimension
