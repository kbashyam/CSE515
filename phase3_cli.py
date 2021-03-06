"""
Multimedia Web Databases - Fall 2019: Project Group 17
Authors:
1. Sumukh Ashwin Kamath
2. Rakesh Ramesh
3. Baani Khurana
4. Karishma Joseph
5. Shantanu Gupta
6. Kanishk Bashyam

This is the CLI for Phase3 of the Project
"""
import importlib
import sys
import warnings

from task5 import task5a, task5b
from utils.inputhelper import get_input_k, get_input_image, get_bool

warnings.filterwarnings('ignore')


def get_task_number():
    choices = ["0", "1", "2", "3", "4a", "4b", "4c", "5a", "5b", "6a", "6b", "6c", "6d"]
    input_string = "0.  Load Metadata\n1.  Labelling\n2.  Clustering\n3.  PPR\n4a. SVM Classifier\n" \
                   "4b. Decision Tree Classifier\n4c. PPR classifier\n5a. LSH\n5b. LSH search\n" \
                   "6a. SVM Relevance Feedback\n6b. Decision Tree Relevance feedback\n6c. PPR Relevance Feedback\n" \
                   "6d. Probabilistic Relevance feedback\n"
    choice = input(input_string)
    if choice not in choices:
        print("Invalid choice")
        return get_task_number()
    return choice


def main():
    """Main function for the script"""
    number_of_tasks = 6
    print("Welcome to Phase 3!")
    choice = get_task_number()
    if choice == "0":
        module_name = "phase3.load_csv"
    elif choice == "1":
        module_name = "phase3.task1"
    elif choice == "2":
        module_name = "p3task2"
    elif choice == "3":
        module_name = "phase3.task3"
    elif choice == "5a":
        l = get_input_k("L")
        k = get_input_k("K")
        comb = get_bool("Combine Models")
        task5a(l, k, comb)
        sys.exit(0)
    elif choice == "5b":
        query = get_input_image("Hands")
        top = get_input_k("K")
        comb = get_bool("Combine Models")
        task5b(query, top, visualize=True, combine_models=comb)
        sys.exit(0)
    elif choice == "6a":
        module_name = "task6_svm"
    elif choice == "6b":
        module_name = "task6_dt"
    elif choice == "6c":
        module_name = "task6_ppr"
    elif choice == "4c":
        module_name = "phase3.task4_ppr"
    elif choice == "4b":
        module_name = "task4_dt"
    elif choice == "4a":
        module_name = "task4_svm"
    else:
        module_name = "task{}".format(choice)
    module = importlib.import_module('{0}'.format(module_name))
    module.main()


if __name__ == "__main__":
    main()


