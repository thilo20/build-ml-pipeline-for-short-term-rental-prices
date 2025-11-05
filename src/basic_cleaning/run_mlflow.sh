mlflow run . \
    -P input_artifact=sample.csv:latest \
    -P output_artifact=clean_sample.csv \
    -P output_type=clean_sample \
    -P output_description="Data with outliers and null values removed" \
    -P min_price=10 \
    -P max_price=350
