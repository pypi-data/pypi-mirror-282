import ast
from pathlib import Path
from typing import Optional, List, Union
from .docstring_parser import DocStringParser
from .ast_parser import ASTParser
from logger import AppLogger

class MarkdownGenerator:
    """
    Generates markdown documentation from Abstract Syntax Tree (AST) nodes.

    This class is responsible for converting AST nodes representing Python code
    into formatted Markdown documentation.

    Attributes:
        show_code (bool): Flag to determine whether to include source code in the documentation.
        logger (logging.Logger): Logger instance for this class.
        docstring_parser (DocStringParser): Instance of DocStringParser for parsing docstrings.
        ast_parser (ASTParser): Instance of ASTParser for parsing AST nodes.

    Example:
        generator = MarkdownGenerator(show_code=True)
        module_ast = ast.parse(Path('example.py').read_text())
        markdown_doc = generator.generate_module_doc(Path('example.py'), module_ast)

    TODO:
        - Add support for generating documentation for module-level variables and constants.
        - Implement cross-referencing between documented elements.
        - Add option to generate a table of contents for the module documentation.
    """

    def __init__(self, show_code: bool):
        """
        Initialize the MarkdownGenerator.

        Args:
            show_code (bool): Flag to determine whether to include source code in the documentation.
        """
        self.show_code: bool = show_code
        self.logger = AppLogger(__name__).get_logger()
        self.docstring_parser = DocStringParser()
        self.ast_parser = ASTParser()
        self.logger.info("MarkdownGenerator initialized")

    def generate_function_doc(self, func: ast.FunctionDef, index: Optional[int] = None) -> str:
        """
        Generate markdown documentation for a function.

        Args:
            func (ast.FunctionDef): The AST node representing the function.
            index (Optional[int]): The index of the function if it's part of a sequence.

        Returns:
            str: Markdown-formatted documentation for the function.

        Example:
            func_ast = ast.parse("def example_func(): pass").body[0]
            func_doc = generator.generate_function_doc(func_ast)

        Note:
            This method extracts information such as function name, arguments,
            docstring, and optionally the source code.
        """
        self.logger.info(f"Generating documentation for function: {func.name}")
        
        header = f"{'##' if index is None else '###'} Function `{func.name}`\n\n"
        
        signature = f"```python\ndef {func.name}{self.ast_parser.parse_arguments(func.args)}:\n```\n\n"
        
        docstring = self.docstring_parser.parse_docstring(ast.get_docstring(func) or "")
        
        param_table = self.docstring_parser.generate_param_table(docstring)
        
        returns = docstring.get('returns', 'No return value specified.')
        
        source_code = ""
        if self.show_code:
            source_code = f"**Source Code:**\n\n```python\n{self.ast_parser.get_source(func)}\n```\n\n"
        
        return f"{header}{signature}{docstring.get('description', '')}\n\n{param_table}\n\n**Returns:**\n{returns}\n\n{source_code}"

    def generate_class_doc(self, cls: ast.ClassDef) -> str:
        """
        Generate markdown documentation for a class.

        Args:
            cls (ast.ClassDef): The AST node representing the class.

        Returns:
            str: Markdown-formatted documentation for the class.

        Example:
            class_ast = ast.parse("class ExampleClass: pass").body[0]
            class_doc = generator.generate_class_doc(class_ast)

        Note:
            This method documents the class, its methods, and optionally its source code.
        """
        self.logger.info(f"Generating documentation for class: {cls.name}")
        
        header = f"## Class `{cls.name}`\n\n"
        
        bases = ", ".join([self.ast_parser.get_source(base) for base in cls.bases])
        if bases:
            header += f"Inherits from: {bases}\n\n"
        
        docstring = self.docstring_parser.parse_docstring(ast.get_docstring(cls) or "")
        
        methods = [node for node in cls.body if isinstance(node, ast.FunctionDef)]
        method_docs = "\n\n".join([self.generate_function_doc(method, i+1) for i, method in enumerate(methods)])
        
        source_code = ""
        if self.show_code:
            source_code = f"**Source Code:**\n\n```python\n{self.ast_parser.get_source(cls)}\n```\n\n"
        
        return f"{header}{docstring.get('description', '')}\n\n{method_docs}\n\n{source_code}"

    def generate_module_doc(self, file_path: Path, node: ast.Module) -> str:
        """
        Generate markdown documentation for a module.

        Args:
            file_path (Path): The path to the Python file.
            node (ast.Module): The AST node representing the module.

        Returns:
            str: Markdown-formatted documentation for the module.

        Example:
            module_ast = ast.parse(Path('example.py').read_text())
            module_doc = generator.generate_module_doc(Path('example.py'), module_ast)

        Note:
            This method documents the module, its functions, classes, and optionally its source code.
        """
        self.logger.info(f"Generating documentation for module: {file_path}")
        
        header = f"# Module `{file_path.stem}`\n\n"
        
        docstring = self.docstring_parser.parse_docstring(ast.get_docstring(node) or "")
        
        functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
        classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
        
        function_docs = "\n\n".join([self.generate_function_doc(func) for func in functions])
        class_docs = "\n\n".join([self.generate_class_doc(cls) for cls in classes])
        
        source_code = ""
        if self.show_code:
            source_code = f"## Full Source Code\n\n```python\n{file_path.read_text()}\n```\n\n"
        
        return f"{header}{docstring.get('description', '')}\n\n{function_docs}\n\n{class_docs}\n\n{source_code}"

    def generate_markdown(self, file_path: Union[str, Path], content: str) -> str:
        """
        Generate markdown documentation for a Python file.

        Args:
            file_path (Union[str, Path]): The path to the Python file.
            content (str): The content of the Python file.

        Returns:
            str: Markdown-formatted documentation for the entire Python file.

        Example:
            content = Path('example.py').read_text()
            markdown_doc = generator.generate_markdown('example.py', content)

        Note:
            This method serves as the main entry point for generating documentation
            for a Python file, including its module, functions, and classes.
        """
        self.logger.info(f"Generating markdown documentation for file: {file_path}")
        
        try:
            file_path = Path(file_path)
            tree = ast.parse(content)
            return self.generate_module_doc(file_path, tree)
        except SyntaxError as e:
            self.logger.error(f"Syntax error in file {file_path}: {str(e)}")
            return f"# Error in module `{file_path.stem}`\n\nUnable to generate documentation due to syntax error:\n\n```\n{str(e)}\n```"
        except Exception as e:
            self.logger.error(f"Unexpected error while generating documentation for {file_path}: {str(e)}")
            return f"# Error in module `{file_path.stem}`\n\nAn unexpected error occurred while generating documentation:\n\n```\n{str(e)}\n```"

# Example usage:
if __name__ == "__main__":
    logger = AppLogger(__name__).get_logger()
    generator = MarkdownGenerator(show_code=True)
    
    example_code = """
    def example_function(param1: int, param2: str = "default") -> bool:
        '''
        This is an example function.
        
        Args:
            param1 (int): The first parameter.
            param2 (str, optional): The second parameter. Defaults to "default".
        
        Returns:
            bool: True if successful, False otherwise.
        '''
        return True

    class ExampleClass:
        '''
        This is an example class.
        '''
        
        def __init__(self):
            '''Initialize the ExampleClass.'''
            pass
        
        def example_method(self):
            '''This is an example method.'''
            pass
    """
    
    try:
        markdown_doc = generator.generate_markdown("example.py", example_code)
        logger.info("Documentation generated successfully")
        print(markdown_doc)
    except Exception as e:
        logger.error(f"Error generating documentation: {str(e)}")