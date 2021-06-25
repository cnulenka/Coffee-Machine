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

