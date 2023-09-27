TEMPLATE_FOLDER = "/templates/"
STATIC_FOLDER = "image_classification\static"
STATIC_FOLDER_IMAGES = "image_classification\static\images"
STATIC_FOLDER_IMAGES_SPLITIMAGES = "image_classification\static\images\split_images"
RECONSTRUCTED_IMAGES_FOLDER =  'static\images\Reconstructed_Images'
JSON_MODEL = 'image_classification\static\cnn_models\model.json'
CNN_MODEL = 'image_classification\static\cnn_models\model.h5'
# CNN_PREDICTION_MODEL = 'image_classification\static\cnn_models\cnn.h5'
CNN_PREDICTION_MODEL = 'image_classification\static\cnn_models\cnn3.h5'
CLASSIFIED_IMAGES = 'image_classification\static\images\classified_images'
global_dimension = ""

def set_global(val):
    global global_dimension
    global_var = val
    # return "Value set!"

def get_global():
    return global_dimension
