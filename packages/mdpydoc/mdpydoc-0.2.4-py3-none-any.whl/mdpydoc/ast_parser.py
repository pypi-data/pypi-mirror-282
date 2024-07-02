import ast
from typing import List, Optional
from logger import AppLogger

class ASTParser:
    """
    Provides utility methods for parsing Abstract Syntax Trees (AST).

    This class offers static methods to extract information from AST nodes,
    such as docstrings, function arguments, and source code. It's useful
    for static code analysis, documentation generation, and other
    AST-based operations.

    Attributes:
        logger (logging.Logger): Logger instance for this class.

    Example:
        parser = ASTParser()
        node = ast.parse("def example_function():\n    '''This is a docstring.'''\n    pass")
        docstring = parser.get_docstring(node.body[0])
        print(docstring)  # Output: This is a docstring.

    Note:
        This class assumes that the AST nodes are generated from valid Python code.
        Unexpected node types may lead to errors or unexpected behavior.

    TODO: Consider adding methods for more complex AST operations, such as
          finding specific node types or traversing the AST.
    """

    def __init__(self):
        self.logger = AppLogger(__name__).get_logger()
        self.logger.info("ASTParser initialized")

    @staticmethod
    def get_docstring(node: ast.AST) -> str:
        """
        Get the docstring of an AST node.

        Args:
            node (ast.AST): The AST node to extract the docstring from.

        Returns:
            str: The docstring of the node, or "No docstring provided" if none exists.

        Example:
            parser = ASTParser()
            node = ast.parse("def example():\n    '''This is an example.'''\n    pass")
            docstring = parser.get_docstring(node.body[0])
            print(docstring)  # Output: This is an example.

        Note:
            This method works for module, class, and function nodes.
            For other node types, it will return "No docstring provided".
        """
        logger = AppLogger(__name__).get_logger()
        logger.info(f"Getting docstring for node: {type(node).__name__}")
        docstring = ast.get_docstring(node) or "No docstring provided"
        logger.debug(f"Extracted docstring: {docstring[:50]}...")  # Log first 50 chars
        return docstring

    @staticmethod
    def parse_arguments(arguments: List[ast.arg]) -> str:
        """
        Parse function arguments from AST.

        Args:
            arguments (List[ast.arg]): List of AST arg nodes representing function arguments.

        Returns:
            str: A comma-separated string of argument names.

        Example:
            parser = ASTParser()
            node = ast.parse("def example(a, b, c): pass")
            args = parser.parse_arguments(node.body[0].args.args)
            print(args)  # Output: a, b, c

        Warning:
            This method only returns argument names. It doesn't include type annotations
            or default values. For a more comprehensive argument parsing, consider
            enhancing this method.

        TODO: Extend this method to include type annotations and default values.
        """
        logger = AppLogger(__name__).get_logger()
        logger.info("Parsing function arguments")
        arg_names = [arg.arg for arg in arguments if isinstance(arg, ast.arg)]
        logger.debug(f"Parsed arguments: {', '.join(arg_names)}")
        return ', '.join(arg_names)

    @staticmethod
    def get_source(node: ast.AST) -> str:
        """
        Get the source code of an AST node.

        Args:
            node (ast.AST): The AST node to extract the source code from.

        Returns:
            str: The source code representation of the AST node.

        Example:
            parser = ASTParser()
            node = ast.parse("x = 1 + 2")
            source = parser.get_source(node.body[0])
            print(source)  # Output: x = 1 + 2

        Note:
            This method uses ast.unparse, which is available in Python 3.9+.
            For earlier versions, consider using the astor library or a custom unparsing method.

        TODO: Add compatibility for Python versions earlier than 3.9.
        """
        logger = AppLogger(__name__).get_logger()
        logger.info(f"Getting source for node: {type(node).__name__}")
        source = ast.unparse(node)
        logger.debug(f"Extracted source: {source[:50]}...")  # Log first 50 chars
        return source

# Example usage:
if __name__ == "__main__":
    logger = AppLogger(__name__).get_logger()
    logger.info("Running ASTParser example")

    parser = ASTParser()
    
    # Example: Parse a simple function
    code = """
    def example_function(a, b):
        '''This is an example function.'''
        return a + b
    """
    
    tree = ast.parse(code)
    function_def = tree.body[0]
    
    logger.info("Parsing example function")
    docstring = parser.get_docstring(function_def)
    arguments = parser.parse_arguments(function_def.args.args)
    source = parser.get_source(function_def)
    
    logger.info(f"Docstring: {docstring}")
    logger.info(f"Arguments: {arguments}")
    logger.info(f"Source: {source}")