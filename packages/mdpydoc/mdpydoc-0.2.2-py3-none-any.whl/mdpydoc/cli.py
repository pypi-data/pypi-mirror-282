import argparse
from typing import Optional
from .doc_generator import DocGenerator
from logger import AppLogger

def main() -> None:
    """
    Main entry point for the documentation generator.

    This function sets up the command-line argument parser, processes the arguments,
    and initializes the DocGenerator to generate documentation for Python code.

    Command-line Arguments:
        src_directory (str): Source directory containing Python files to document.
        docs_directory (str): Target directory for generated documentation.
        --show-code (flag): If set, include source code in the documentation.
        --log-level (str): Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        --max-workers (int): Maximum number of worker threads for parallel processing.

    Returns:
        None

    Example:
        To run the script:
        python script_name.py /path/to/source /path/to/docs --show-code --log-level INFO --max-workers 4

    Note:
        This function uses argparse for command-line argument parsing and
        initializes a DocGenerator instance with the provided configurations.

    TODO: 
        - Add support for custom documentation templates.
        - Implement error handling for invalid directory paths.
        - Consider adding an option to specify output format (e.g., HTML, Markdown).
    """
    logger = AppLogger(__name__).get_logger()
    logger.info("Starting documentation generator")

    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description="Generate documentation for Python code.")
    parser.add_argument("src_directory", type=str, help="Source directory containing Python files")
    parser.add_argument("docs_directory", type=str, help="Target directory for generated documentation")
    parser.add_argument("--show-code", action="store_true", help="Include source code in documentation")
    parser.add_argument("--log-level", type=str, default="INFO", 
                        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], 
                        help="Set the logging level")
    parser.add_argument("--max-workers", type=int, default=None, 
                        help="Maximum number of worker threads")

    # Parse command-line arguments
    args = parser.parse_args()
    logger.info(f"Parsed arguments: {args}")

    # Initialize DocGenerator with parsed arguments
    doc_generator = DocGenerator(
        show_code=args.show_code,
        log_level=args.log_level,
        max_workers=args.max_workers
    )
    logger.info("DocGenerator initialized")

    # Process the specified directory and generate documentation
    logger.info(f"Processing directory: {args.src_directory}")
    doc_generator.process_directory(args.src_directory, args.docs_directory)
    logger.info(f"Documentation generated in: {args.docs_directory}")

if __name__ == "__main__":
    main()