"""
Q8. Log File Analyzer
Read a log file, count ERROR/WARNING/INFO, and write a summary to a new file.
"""


def analyze_log_file(input_path, output_path):
    counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}
    with open(input_path, "r", encoding="utf-8") as log_file:
        for line in log_file:
            if "ERROR" in line:
                counts["ERROR"] += 1
            elif "WARNING" in line:
                counts["WARNING"] += 1
            elif "INFO" in line:
                counts["INFO"] += 1

    summary = [
        f"Log summary for {input_path}",
        f"ERROR: {counts['ERROR']}",
        f"WARNING: {counts['WARNING']}",
        f"INFO: {counts['INFO']}",
    ]

    with open(output_path, "w", encoding="utf-8") as summary_file:
        summary_file.write("\n".join(summary))

    return counts


if __name__ == "__main__":
    counts = analyze_log_file("sample_log.txt", "log_summary.txt")
    print("Log analyzer completed.")
    print(counts)
