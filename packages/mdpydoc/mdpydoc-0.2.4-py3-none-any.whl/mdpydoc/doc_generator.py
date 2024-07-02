import logging
from pathlib import Path
from typing import Union, Optional, List
from concurrent.futures import ThreadPoolExecutor, as_completed
from .markdown_generator import MarkdownGenerator
from .file_processor import FileProcessor
from logger import AppLogger

class DocGenerator:
    """
    Main class for generating documentation from Python source files.

    This class orchestrates the process of generating documentation by processing
    Python source files in a given directory and its subdirectories.

    Attributes:
        show_code (bool): Flag to include source code in the documentation.
        log_level (str): Logging level for the DocGenerator.
        max_workers (Optional[int]): Maximum number of worker threads for parallel processing.
        logger (logging.Logger): Logger instance for this class.
        markdown_generator (MarkdownGenerator): Instance to generate Markdown documentation.
        file_processor (FileProcessor): Instance to process individual Python files.

    Example:
        doc_gen = DocGenerator(show_code=True, log_level='INFO', max_workers=4)
        doc_gen.process_directory('/path/to/source', '/path/to/docs')

    Note:
        The DocGenerator uses ThreadPoolExecutor for parallel processing of files,
        which can significantly speed up documentation generation for large projects.

    TODO:
        - Add support for different output formats (e.g., HTML, reStructuredText).
        - Implement caching to avoid re-processing unchanged files.
        - Add progress reporting for long-running documentation generation.
    """

    def __init__(self, show_code: bool = True, log_level: str = 'INFO', max_workers: Optional[int] = None):
        """
        Initialize the DocGenerator.

        Args:
            show_code (bool): Flag to include source code in the documentation. Defaults to True.
            log_level (str): Logging level for the DocGenerator. Defaults to 'INFO'.
            max_workers (Optional[int]): Maximum number of worker threads. Defaults to None.

        Raises:
            ValueError: If an invalid log_level is provided.
        """
        self.show_code: bool = show_code
        self.log_level: str = log_level
        self.max_workers: Optional[int] = max_workers
        self.logger = AppLogger(__name__).get_logger()
        self.setup_logging()
        self.markdown_generator: MarkdownGenerator = MarkdownGenerator(show_code=self.show_code)
        self.file_processor: FileProcessor = FileProcessor(self.markdown_generator, self.logger)
        self.logger.info("DocGenerator initialized")

    def setup_logging(self) -> None:
        """
        Set up logging for the DocGenerator.

        This method configures the logging level based on the log_level attribute.

        Raises:
            ValueError: If an invalid log_level is provided.
        """
        try:
            numeric_level = getattr(logging, self.log_level.upper())
            if not isinstance(numeric_level, int):
                raise ValueError(f"Invalid log level: {self.log_level}")
            self.logger.setLevel(numeric_level)
            self.logger.info(f"Logging level set to {self.log_level}")
        except AttributeError:
            raise ValueError(f"Invalid log level: {self.log_level}")

    def process_directory(self, src_dir: Union[str, Path], docs_dir: Union[str, Path]) -> None:
        """
        Process a directory of Python files and generate documentation.

        This method walks through the source directory, processes each Python file,
        and generates corresponding documentation in the target directory.

        Args:
            src_dir (Union[str, Path]): Source directory containing Python files.
            docs_dir (Union[str, Path]): Target directory for generated documentation.

        Raises:
            FileNotFoundError: If the source directory does not exist.
            PermissionError: If there's no write permission for the target directory.

        Note:
            This method uses ThreadPoolExecutor for parallel processing of files.
        """
        self.logger.info(f"Processing directory: {src_dir}")
        src_path = Path(src_dir)
        docs_path = Path(docs_dir)

        if not src_path.exists():
            self.logger.error(f"Source directory does not exist: {src_path}")
            raise FileNotFoundError(f"Source directory does not exist: {src_path}")

        docs_path.mkdir(parents=True, exist_ok=True)

        python_files: List[Path] = list(src_path.rglob("*.py"))
        self.logger.info(f"Found {len(python_files)} Python files to process")

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_file = {executor.submit(self.process_file, file, docs_path): file for file in python_files}
            for future in as_completed(future_to_file):
                file = future_to_file[future]
                try:
                    future.result()
                except Exception as exc:
                    self.logger.error(f"Error processing file {file}: {exc}")

        self.logger.info(f"Documentation generation complete. Output directory: {docs_path}")

    def process_file(self, file: Path, docs_path: Path) -> None:
        """
        Process a single Python file and generate its documentation.

        Args:
            file (Path): Path to the Python file to process.
            docs_path (Path): Base path for the generated documentation.

        Note:
            This method is called by process_directory for each Python file.
        """
        self.logger.info(f"Processing file: {file}")
        relative_path = file.relative_to(file.parents[1])
        output_file = docs_path / relative_path.with_suffix('.md')
        output_file.parent.mkdir(parents=True, exist_ok=True)

        try:
            content = self.file_processor.process_file(file)
            output_file.write_text(content)
            self.logger.info(f"Documentation generated for {file} -> {output_file}")
        except Exception as e:
            self.logger.error(f"Error processing file {file}: {e}")

# Example usage:
if __name__ == "__main__":
    doc_gen = DocGenerator(show_code=True, log_level='INFO', max_workers=4)
    doc_gen.process_directory('/path/to/source', '/path/to/docs')