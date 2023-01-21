import os

BASE_PATH = "/Users/samehayousef/Desktop/Smartathon/dataset"

IMAGES_PATH = os.path.sep.join([BASE_PATH, "images"])
ANNOTS_PATH = os.path.sep.join([BASE_PATH, "annotations"])

# define the path to the base output directory
BASE_OUTPUT = "/Users/samehayousef/Desktop/Smartathon/dataset/output"
# define the path to the output model, label binarizer, plots output
# directory, and testing image paths

MODEL_PATH = os.path.sep.join([BASE_OUTPUT, "detector.h5"])
LB_PATH = os.path.sep.join([BASE_OUTPUT, "lb.pickle"])
PLOTS_PATH = os.path.sep.join([BASE_OUTPUT, "plots"])
TEST_PATHS = os.path.sep.join([BASE_OUTPUT, "test2.csv"])


INIT_LR = 1e-4
NUM_EPOCHS = 20
BATCH_SIZE = 32