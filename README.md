# auto_mapeo

Antes de ejecutar el código es necesario revisar el archivo 
config.py
El programa asume que los datos crudos se encuentran agrupados y normalizados en formato you have collected raw laboratory data and aggregated it, grouping by [Site, Lab Test Name, Specimen Type, Units (missingness allowed), and locally-recorded LOINC code (missingness allowed)].
.txt, .csv, o .xls.

Los siguientes campos del archivo config.py requieren que el usuario los complete:

- out_dir
- in_file
- loinc_file_path
- lib_loc (for R strindist package)
- test_col (see config.py file)
- spec_col (see config.py file)
- units (see config.py file)
- loinc_col (see config.py file)
- min_col (see config.py file)
- max_col (see config.py file)
- mean_col (see config.py file)
- perc_5 (see config.py file)
- perc_25 (see config.py file)
- median_col (see config.py file)
- perc_75 (see config.py file)
- perc_95 (see config.py file)
- count (see config.py file)
- site (see config.py file)
- missing (see config.py file)
- api_key

Los siguientes pueden ser opcionalmente configurados:
- delim
- write_file_source_data_cleaning
- write_file_loinc_parsed
- write_file_umls_cuis
- rejection_threshold
- num_cuis
- min_sites_per_loinc_key
- min_tests_per_loinc_group
- min_row_count_per_loinc_group
- run_cv
- n_splits
- tuning_evals
- max_features 
- max_depth
- min_samples_split
- n_estimators 


Posterior a la configuración:
Se ejecuta el archivo Analysis.py, el cual contiene los modelos de machine learning, hace las predicciones en datos etiquetados y
datos no etiquetados y genera los outputs labeled_data_predictions.csv y unlabeled_data_predictions.csv.
