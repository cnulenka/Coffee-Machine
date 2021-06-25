from Constants import RESULTS

def get_empty_results() -> RESULTS:
    return RESULTS

def print_results(results: RESULTS) -> None:
    error_list = results["Errors"]
    if len(error_list) > 0:
        for error in error_list:
            print("Error: " + error)

    warnings_list = results["Warnings"]
    if len(warnings_list) > 0:
        for warning in warnings_list:
            print("Warning: " + warning)

    info_list = results["Info"]
    if len(info_list) > 0:
        for info in info_list:
            print("Info: " + info)

def aggregate_results( final_results: RESULTS, results_to_add: RESULTS) -> RESULTS:
    error_list = results_to_add["Errors"]
    if len(error_list) > 0:
        for error in error_list:
            final_results["Errors"].append(error)

    warnings_list = results_to_add["Warnings"]
    if len(warnings_list) > 0:
        for warning in warnings_list:
            final_results["Warnings"].append(warning)

    info_list = results_to_add["Info"]
    if len(info_list) > 0:
        for info in info_list:
            final_results["Info"].append(info)
