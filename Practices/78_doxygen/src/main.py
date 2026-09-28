"""@file main.py
@brief Example Doxygen documentation for a simple Python module.

This module demonstrates how to document a basic function using
Doxygen-style comments in Python.
"""

from classes.processor import Processor

def add_numbers(a, b):
    """! @Add two numbers and return the result.

    @param a First number to add.
    @param b Second number to add.
    @return Sum of a and b.
    """
    return a + b

def calculate_velocity(mass, acceleration, time_delta):
    """! @brief Calculates the final velocity of an object.

    This function applies the basic kinematic equation v = u + at,
    assuming initial velocity (u) is zero.

    @param mass The mass of the object (not used in calculation, for demo).
    @param acceleration The constant acceleration in m/s^2.
    @param time_delta The time elapsed in seconds.
    @return The final velocity in m/s.
    """
    return acceleration * time_delta

def count_test_results(source_path, output_format):
    """! @brief Process test results and return summary

    This functuin can be applied to all test results to get
    summary 
    
    @param source_path Where the source is stored
    @param output_format Desired output format

    @returns string summary of all test results 
    """
    return "This test result"

if __name__ == "__main__":
    result = add_numbers(3, 4)
    calculate_velocity(3, 4, 5)
    process = Processor("Roy")
    process.launch("Fast run")
    