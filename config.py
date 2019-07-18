##### Configuration settings ########
## This program assumes that you have collected raw laboratory data and aggregated it, grouping by [Lab Test Name, Specimen Type, Units, and LOINC code].
## Using the aggregated groups, the summary measures used as features in the algorithm include [Mean, Minimum, Maximum, 5th Percentile, 25th Percentile, 
## Median, 75th Percentile, 95th percentile, and Count]
## The aggregate source data should be stored in a .txt, .csv, or .xls file

## Enter the directory where you would like the intermediate output files to be stored:
## Example: 'C:/Users/me/Documents/MyFiles/'
out_dir = 'C:/Users/aalei/ml_loinc_mapping/'

## Enter the filepath where your raw source data file is located along with :
## Example: ## Example: 'C:/Users/me/Documents/MyFiles/Data.txt'
in_file = 'C:/Users/aalei/ml_loinc_mapping/paramapc.csv'

## If your data file is delimited by character(s) other than a comma, please indicate the delimeter:
## Example: delimiter = '|'
delim = ';'

## Throughout this data transformation pipeline, intermediate files can be written to disk both for examination and for loading in subsequent model steps to avoid having to recreate them. The following files created while cleaning source data text can be written to file: 
## 1. Cleaned_Lab_Names.csv
## 2. By_Site_Lab_Word_Count.csv
## 3. Discarded_Lab_Names.csv
## 4. Cleaned_Specimen_Names.csv
## 5. By_Site_Specimen_Word_Count.csv
## The default 'False' will NOT write intermediate files to disk. If user wants these files saved to disk, change the following line to write_file_source_data_cleaning = True
write_file_source_data_cleaning = False

## The following files from the LOINC table data parsing step can be written to disk:
## 1. LOINC_Name_map.csv
## 2. LOINC_Parsed_Component_System_Longword.csv
## The default 'False' will NOT write intermediate files to disk. If user wants these files saved to disk, change the following line to write_file_loinc_parsed = True
write_file_loinc_parsed = False

## The following files from the UMLS CUI search can be written to disk:
## 1. UMLS_Mapped_Specimen_Names.csv
## 2. UMLS_Mapped_Test_Names.csv
## The default 'False' will NOT write intermediate files to disk. If user wants these files saved to disk, change the following line to write_file_umls_cuis = True
write_file_umls_cuis = False

## Enter the full filepath to your local loinc.csv file installation:
## Example: 'C:/Users/me/Documents/MyFiles/loinc.csv'
loinc_file_path = 'C:/Users/aalei/ml_loinc_mapping/loinc.csv'

## Enter the full filepath to your local R library file location (where stringdist package is installed)
## Example: 'C:/Program Files/R/R-3.4.1/library'
lib_loc = 'C:/Program Files/R/R-3.5.1/library'

## The program assumes that your raw source data file has a header with the following MANDATORY fields:
##  1. Test Name
##  2. Specimen Type
##  3. Units (some missingness is tolerated by the algorithm)
##  4. LOINC code (some missingness is tolerated by the algorithm)
##  5. Numeric test result minimum
##  6. Numeric test result maximum
##  7. Numeric test result mean
##  8. Numeric test result 5th percentile
##  9. Numeric test result 25th percentile
## 10. Numeric test result median
## 11. Numeric test result 75th percentile
## 12. Numeric test result 95th percentile
## 13. Count (of total number of tests with the same [Test Name, Specimen Type, Units, and LOINC code])
## 14. Site identifier


## Enter the name of the column in your data source that contains the TEST NAME (i.e. Creatinine):
test_col = 'nombre'

## Enter the name of the column in your data source that contains the SPECIMEN TYPE (i.e. urine):
spec_col = 'especimen'

## Enter the name of the column in your data source that contains the UNITS:
units = 'unidades'

## Enter the name of the column in your data source that contains the LOINC CODE:
loinc_col = 'loincode'

## Enter the name of the column in your data source that contains the numeric MINIMUM:
min_col = 'minimo'

## Enter the name of the column in your data source that contains the numeric MAXIMUM:
max_col = 'maximo'

## Enter the name of the column in your data source that contains the numeric MEAN:
mean_col = 'media'

## Enter the name of the column in your data source that contains the numeric 5th PERCENTILE:
perc_5 = 'percentil5'

## Enter the name of the column in your data source that contains the numeric 25th PERCENTILE:
perc_25 = 'percentil25'

## Enter the name of the column in your data source that contains the numeric MEDIAN:
median_col = 'mediana'

## Enter the name of the column in your data source that contains the numeric 75th PERCENTILE:
perc_75 = 'percentil75'

## Enter the name of the column in your data source that contains the numeric 95th PERCENTILE:
perc_95 = 'percentil95'

## Enter the name of the column in your data source that contains the COUNT:
count = 'count'

## Enter the name of the column in your data source that contains the SITE IDENTIFIER:
site = 'localcode'

## If missing data is denoted by anything other than a NULL field, please indicate special strings
## Example: missings = ["*MISSING", 'UNKNOWN', '-1']
missing = ["ENTER", "YOUR", "MISSING", "VALUES"]

## Please enter a numeric rejection threshold (example: 4.0) for eliminating high frequency tokens from source data test names. 
## Default will not remove any tokens during source data pre-processing.
rejection_threshold = None

## Status updates on segments of code being executed will be provided to the user by default. If you do NOT wish to have status updates on code execution, change print_status = 'N'
print_status = 'Y'

## This program uses the UMLS API to generate features by obtaining CUIs for test names and specimen types. To access the UMLS, the user is required to enter an API key.
## To obtain this information, the user may create or login to their UMLS account at https://uts.nlm.nih.gov/home.html. After logging in to UMLS, click on 'My Profile'.
## The API key is listed beneath the user. Paste the API KEY into the field below:
api_key = "EfAQWNc.W89Dz:A"

## Enter the integer number of CUIs to retain for each UMLS search. Default setting will return up to 3 CUIs for each test name and each specimen type
num_cuis = 3

## Enter the integer number for minimum number of sites at which a LOINC key must be used to be retained in the labeled dataset (Default is 1, meaning that LOINC keys occurring at only 1 site are filtered out and combined with the unlabeled data for reclassification)
min_sites_per_loinc_key = 1

## Enter the minimum number of cumulative test instances per LOINC group to be retained in the labeled training data (Default is 9)
min_tests_per_loinc_group = 9

## Enter the minimum number of data instances allowed per LOINC key group in the labeled training data (Default is 2)
min_row_count_per_loinc_group = 2

## Default program setting is to fit Random Forest and One-Versus-Rest models during cross-validation, to obtain predicted labels from each model, and to provide model performance metrics obtained during cross-validation. If you do NOT want to perform CV, change the code below to "run_cv = 'N'"
run_cv = 'Y'

## Enter the integer number of cross-validation folds (default is 5-fold)
n_splits = 5

## Enter the integer number of trials for hyperparameter tuning (default is 200)
tuning_evals = 200

## Values for hyperopt model hyperparameter tuning. User has the option to customize the search space for the following random forest parameters: max_features, max_depth, min_samples_split, and n_estimators.

## Default setting is for max_features to be tested in increments of 2 over the space from 2 features to N - 3 features (where N is the number of columns in the training dataset), represented in the code by np.arange(2, (X0.shape[1] - 3), 2). If the user wants to modify the search space, please change the following line of code to:  max_features = [MINIMUM NUMBER, MAXIMUM NUMBER, INCREMENT]
## Example: max_features = [2, 24, 2]
max_features = None

## Default setting is for max_depth to be tested in increments of 5 over the space from 5 to 25, represented programatically as np.arange(5, 35, 5). If the user wants to modify the search space, please change the following line of code to: max_depth = [MINIMUM DEPTH, MAXIMUM DEPTH, INCREMENT]
## Example: max_depth = [5, 50, 5]
max_depth = None

## Default setting is for min_samples_split to be tested in increments of 2 over the space from 2 to 20, represented programatically as np.arange(2, 20, 2). If the user wants to modify the search space, please change the following line of code to: min_samples_split = [MINIMUM SAMPLES, MAXIMUM SAMPLES, INCREMENT]
## Example: min_samples_split = [2, 16, 1]
min_samples_split = None

## Default setting is for n_estimators to be tested in increments of 25 over the space from 10 to 250, represented programatically as np.arange(10, 250, 25). If the user wants to modify the search space, please change the following line of code to: n_estimators = [MINIMUM ESTIMATORS, MAXIMUM ESTIMATORS, INCREMENT]
## Example: n_estimators = [10, 250, 25]
n_estimators = None

