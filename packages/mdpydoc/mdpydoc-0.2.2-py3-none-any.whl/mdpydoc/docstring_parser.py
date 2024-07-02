from typing import Optional, List, Dict
from logger import AppLogger

class DocStringParser:
    """
    Parses docstrings and generates formatted documentation.

    This class provides static methods to extract information from docstrings
    and format them into structured documentation.

    Attributes:
        logger (logging.Logger): Logger instance for this class.

    Example:
        parser = DocStringParser()
        docstring = '''
        This is a sample function.

        Args:
            param1 (int): The first parameter.
            param2 (str): The second parameter.

        Returns:
            bool: True if successful, False otherwise.

        Raises:
            ValueError: If param1 is negative.
        '''
        args_section = parser.parse_section(docstring, "Args")
        param_table = parser.generate_param_table(docstring)

    Note:
        This class assumes that docstrings follow a consistent format.
        Unexpected formatting may lead to parsing errors.

    TODO:
        - Add support for parsing more complex docstring formats (e.g., NumPy, Google style).
        - Implement caching to improve performance for repeated parsing of the same docstring.
        - Add method to generate full formatted documentation from a docstring.
    """

    def __init__(self):
        self.logger = AppLogger(__name__).get_logger()
        self.logger.info("DocStringParser initialized")

    @staticmethod
    def parse_section(docstring: str, section: str) -> Optional[str]:
        """
        Parse a specific section from a docstring.

        Args:
            docstring (str): The full docstring to parse.
            section (str): The name of the section to extract (e.g., "Args", "Returns").

        Returns:
            Optional[str]: The content of the specified section if found, None otherwise.

        Example:
            parser = DocStringParser()
            docstring = '''
            This is a sample function.

            Args:
                param1 (int): The first parameter.
                param2 (str): The second parameter.

            Returns:
                bool: True if successful, False otherwise.
            '''
            args_section = parser.parse_section(docstring, "Args")
            print(args_section)
            # Output:
            # param1 (int): The first parameter.
            # param2 (str): The second parameter.

        Note:
            This method assumes that sections in the docstring are denoted by
            the section name followed by a colon (e.g., "Args:").
        """
        logger = AppLogger(__name__).get_logger()
        logger.info(f"Parsing '{section}' section from docstring")

        if f"{section}:" in docstring:
            parts = docstring.split(f"{section}:")
            if len(parts) > 1:
                content = parts[1].split("\n\n")[0].strip()
                logger.debug(f"Found content for '{section}' section")
                return content
        
        logger.warning(f"Section '{section}' not found in docstring")
        return None

    @staticmethod
    def generate_param_table(docstring: str) -> str:
        """
        Generate a markdown table of parameters from a docstring.

        Args:
            docstring (str): The full docstring to parse.

        Returns:
            str: A markdown-formatted table of parameters.

        Example:
            parser = DocStringParser()
            docstring = '''
            This is a sample function.

            Args:
                param1 (int): The first parameter.
                param2 (str): The second parameter.

            Returns:
                bool: True if successful, False otherwise.
            '''
            param_table = parser.generate_param_table(docstring)
            print(param_table)
            # Output:
            # | Parameter | Type | Description |
            # |-----------|------|-------------|
            # | param1    | int  | The first parameter. |
            # | param2    | str  | The second parameter. |

        Note:
            This method assumes that the "Args" section in the docstring
            follows a consistent format of "param_name (type): description".

        TODO:
            - Add support for optional parameters and default values.
            - Improve handling of multi-line parameter descriptions.
        """
        logger = AppLogger(__name__).get_logger()
        logger.info("Generating parameter table from docstring")

        args_section = DocStringParser.parse_section(docstring, "Args")
        if not args_section:
            logger.warning("No 'Args' section found in docstring")
            return "No parameters found."

        params: List[Dict[str, str]] = []
        for line in args_section.split("\n"):
            parts = line.strip().split(":", 1)
            if len(parts) == 2:
                param_info = parts[0].strip().split(" ", 1)
                if len(param_info) == 2:
                    param_name, param_type = param_info
                    param_type = param_type.strip("()")
                    param_desc = parts[1].strip()
                    params.append({
                        "name": param_name,
                        "type": param_type,
                        "description": param_desc
                    })

        if not params:
            logger.warning("No parameters parsed from 'Args' section")
            return "No valid parameters found."

        table = "| Parameter | Type | Description |\n"
        table += "|-----------|------|-------------|\n"
        for param in params:
            table += f"| {param['name']} | {param['type']} | {param['description']} |\n"

        logger.info(f"Generated parameter table with {len(params)} parameters")
        return table

# Example usage:
if __name__ == "__main__":
    logger = AppLogger(__name__).get_logger()
    logger.info("Running DocStringParser example")

    parser = DocStringParser()
    
    sample_docstring = """
    This is a sample function.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        ValueError: If param1 is negative.
    """

    logger.info("Parsing 'Args' section")
    args_section = parser.parse_section(sample_docstring, "Args")
    logger.info(f"Args section:\n{args_section}")

    logger.info("Generating parameter table")
    param_table = parser.generate_param_table(sample_docstring)
    logger.info(f"Parameter table:\n{param_table}")