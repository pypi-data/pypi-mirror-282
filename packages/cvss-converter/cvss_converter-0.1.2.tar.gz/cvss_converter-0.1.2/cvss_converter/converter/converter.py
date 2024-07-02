from cvss import CVSS3


def cvss2_to_cvss3(cvssv2_string: str) -> tuple[str, float]:
    # Remove CVSS2# prefix
    cvssv2_string = cvssv2_string.replace("CVSS2#", "")

    # Mapping of CVSS v2 to CVSS v3 metrics
    v2_to_v3 = {
        "AV": {
            "L": "AV:L",
            "A": "AV:A",
            "N": "AV:N",
        },  # One to one mapping - except AC:P
        "AC": {
            "L": "AC:L",
            "M": "AC:L",
            "H": "AC:H",
        },  # If Medium, it will be treated a Low
        "Au": {"N": "PR:N", "S": "PR:L", "M": "PR:H"},  # One to one mapping
        "C": {"N": "C:N", "P": "C:L", "C": "C:H"},  # One to one mapping
        "I": {"N": "I:N", "P": "I:L", "C": "I:H"},  # One to one mapping
        "A": {"N": "A:N", "P": "A:L", "C": "A:H"},  # One to one mapping
    }

    # Default values for CVSS v3 - to err on the side of caution, thus choosing the more severe option
    v3_defaults = {
        "S": "C",  # Scope: Changed
        "UI": "N",  # User Interaction: None
    }

    # Parse the CVSS v2 vector
    cvssv2_metrics = cvssv2_string.split("/")
    cvssv3_metrics = {}

    for metric in cvssv2_metrics:
        key, value = metric.split(":")
        if key in v2_to_v3:
            v3_key, v3_value = v2_to_v3[key][value].split(":")
            cvssv3_metrics[v3_key] = v3_value

    # Add default values for Scope and User Interaction (missing in V2)
    cvssv3_metrics["S"] = v3_defaults["S"]
    cvssv3_metrics["UI"] = v3_defaults["UI"]

    # Create ordered CVSS v3 vector string
    v3_vector_order = ["AV", "AC", "PR", "UI", "S", "C", "I", "A"]
    sorted_cvssv3_string = "CVSS:3.0"
    for key in v3_vector_order:
        sorted_cvssv3_string += f"/{key}:{cvssv3_metrics[key]}"

    # cvssv3_string = "CVSS:3.0/" + "/".join(sorted_cvssv3_metrics)
    cvssv3_object = CVSS3(sorted_cvssv3_string)
    cvssv3_basescore = cvssv3_object.base_score

    # Return the normalized CVSS v3 vector string
    return sorted_cvssv3_string, cvssv3_basescore
