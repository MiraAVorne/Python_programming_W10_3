########################################################
# Task A10_T3
# Developer Sami Viljanen
# Date 2025-10-26
########################################################


def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if PAsc:
                if PValues[j] > PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
                    swapped = True

            else:
                if PValues[j] < PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
                    swapped = True

        if not swapped:
            break

    return None


def readValues(PFilename: str) -> list[int]:    # Read integer values from a file, one per line
    values = []
    try:
        with open(PFilename, 'r') as file:    # Read values from the file
            for line in file:
                line = line.strip()

                if line:  # Skip empty lines
                    values.append(int(line))

    except FileNotFoundError:   # FileNotFound Error handling
        print(f"Error: File '{PFilename}' not found.")

    except ValueError:    # ValuError handling
        print(f"Error: File contains non-integer values.")

    return values


def displayValues(PFilename: str, PValues: list[int], PLabel: str = "Raw") -> None:    # Display values in a formatted string
    values_str = ", ".join(str(val) for val in PValues)
    print(f"{PLabel} '{PFilename}' -> {values_str}")


