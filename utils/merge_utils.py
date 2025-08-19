def merge_all_files(uploaded_files, target_upload):
    dataframes = []
    
    for file in uploaded_files:
        df = pd.read_csv(file)
        df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
        dataframes.append(df)

    if target_upload:
        df = pd.read_csv(target_upload)
        df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
        dataframes.append(df)

    merged_df = reduce(lambda left, right: pd.merge(left, right, on='customer_no', how='outer'), dataframes)
    return merged_df