from utils.model_imputation import clean_and_impute
from utils.merge_utils import merge_all_files

def train_and_save_stacked_model(uploaded_files, model_choices, model_name, final_estimator_str, category_names, target_upload):
    try:
        df = merge_all_files(uploaded_files, target_upload)
        df = clean_and_impute(df)


