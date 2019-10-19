"""
Multimedia Web Databases - Fall 2019: Project Group 17
Authors:
1. Sumukh Ashwin Kamath
2. Rakesh Ramesh
3. Baani Khurana
4. Karishma Joseph
5. Shantanu Gupta
6. Kanishk Bashyam

This is the CLI for task 3 of Phase 2 of the project
"""
from utils.excelcsv import CSVReader
from classes.dimensionreduction import DimensionReduction
from utils.termweight import print_tw
from utils.excelcsv import CSVReader
from utils.model import Model
from utils.inputhelper import get_input_k, get_input_dimensionality_reduction_model, \
    get_input_feature_extractor_model, get_input_image_label

model_interact = Model()
csv_reader = CSVReader()


def main():
    """Main function for the Task3"""
    feature_extraction_model = get_input_feature_extractor_model()
    dimension_reduction_model = get_input_dimensionality_reduction_model()
    k_value = get_input_k()
    label = get_input_image_label()

    excel_reader = CSVReader()
    excel_reader.save_hand_csv_mongo("HandInfo.csv")

    # Performs the dimensionality reduction
    dim_reduction = DimensionReduction(feature_extraction_model, dimension_reduction_model, k_value, label)
    obj_lat, feat_lat, model = dim_reduction.execute()

    # Saves the returned model
    filename = "{0}_{1}_{2}_{3}".format(feature_extraction_model, dimension_reduction_model, label.replace(" ", ''),
                                        str(k_value))
    model_interact.save_model(model=model, filename=filename)

    # Printing the term weight pairs
    print_tw(obj_lat, feat_lat)

    # save term weight pairs to csv
    filename = "task3_{}_{}_{}_{}".format(feature_extraction_model, dimension_reduction_model, label, k_value)
    csv_reader.save_to_csv(obj_lat, feat_lat, filename)


if __name__ == "__main__":
    main()
