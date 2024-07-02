import logging
from pathlib import Path
from functools import lru_cache
import hashlib
from typing import Optional
from .markdown_generator import MarkdownGenerator
from logger import AppLogger

class FileProcessor:
    """
    Processes Python files and generates documentation.

    This class handles the processing of individual Python files,
    generating documentation using a MarkdownGenerator instance.

    Attributes:
        markdown_generator (MarkdownGenerator): Instance to generate Markdown documentation.
        logger (logging.Logger): Logger instance for this class.

    Example:
        markdown_gen = MarkdownGenerator(show_code=True)
        logger = AppLogger(__name__).get_logger()
        processor = FileProcessor(markdown_gen, logger)
        processor.process_file(Path('example.py'), Path('docs'))

    Note:
        This class uses caching to avoid unnecessary reprocessing of unchanged files.

    TODO:
        - Add support for processing non-Python files (e.g., README.md).
        - Implement parallel processing for large files.
        - Add option to customize output file naming convention.
    """

    def __init__(self, markdown_generator: MarkdownGenerator, logger: logging.Logger):
        """
        Initialize the FileProcessor.

        Args:
            markdown_generator (MarkdownGenerator): Instance to generate Markdown documentation.
            logger (logging.Logger): Logger instance for logging.
        """
        self.markdown_generator: MarkdownGenerator = markdown_generator
        self.logger: logging.Logger = logger
        self.logger.info("FileProcessor initialized")

    @lru_cache(maxsize=None)
    def get_file_hash(self, file_path: Path) -> str:
        """
        Calculate and cache the MD5 hash of a file.

        This method is cached to improve performance for repeated calls
        on the same file.

        Args:
            file_path (Path): Path to the file to hash.

        Returns:
            str: MD5 hash of the file contents.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            PermissionError: If there's no read permission for the file.

        Example:
            processor = FileProcessor(markdown_gen, logger)
            file_hash = processor.get_file_hash(Path('example.py'))
            print(f"File hash: {file_hash}")

        Note:
            The LRU cache is set to None, which means it will cache an unlimited
            number of file hashes. Adjust this if memory usage becomes a concern.
        """
        self.logger.info(f"Calculating hash for file: {file_path}")
        
        if not file_path.exists():
            self.logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"File not found: {file_path}")

        try:
            with open(file_path, "rb") as file:
                file_hash = hashlib.md5()
                chunk = file.read(8192)
                while chunk:
                    file_hash.update(chunk)
                    chunk = file.read(8192)
            
            hash_value = file_hash.hexdigest()
            self.logger.debug(f"Hash calculated for {file_path}: {hash_value}")
            return hash_value
        except PermissionError:
            self.logger.error(f"Permission denied: Unable to read {file_path}")
            raise PermissionError(f"Permission denied: Unable to read {file_path}")
        except Exception as e:
            self.logger.error(f"Error calculating hash for {file_path}: {str(e)}")
            raise

    def process_file(self, file_path: Path, target_dir: Path) -> None:
        """
        Process a single Python file and generate documentation.

        This method reads a Python file, generates documentation using
        the MarkdownGenerator, and writes the output to the target directory.

        Args:
            file_path (Path): Path to the Python file to process.
            target_dir (Path): Directory to write the generated documentation.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            PermissionError: If there's no read permission for the file.

        Example:
            processor = FileProcessor(markdown_gen, logger)
            processor.process_file(Path('example.py'), Path('docs'))

        Note:
            This method checks if the file has been modified since the last
            processing by comparing file hashes.

        TODO:
            - Implement diff checking to update only changed sections of documentation.
            - Add option to specify custom output filename.
        """
        self.logger.info(f"Processing file: {file_path}")

        if not file_path.exists():
            self.logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"File not found: {file_path}")

        try:
            current_hash = self.get_file_hash(file_path)
            output_file = target_dir / f"{file_path.stem}.md"
            
            # Check if file has been modified
            if output_file.exists():
                with open(output_file, "r") as f:
                    first_line = f.readline().strip()
                    if first_line.startswith(f"<!-- File Hash: {current_hash}"):
                        self.logger.info(f"File {file_path} unchanged, skipping processing")
                        return

            with open(file_path, "r") as file:
                content = file.read()

            doc_content = self.markdown_generator.generate_markdown(file_path.name, content)
            
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, "w") as out_file:
                out_file.write(f"<!-- File Hash: {current_hash} -->\n\n")
                out_file.write(doc_content)

            self.logger.info(f"Documentation generated for {file_path} -> {output_file}")
        except PermissionError:
            self.logger.error(f"Permission denied: Unable to read {file_path}")
            raise PermissionError(f"Permission denied: Unable to read {file_path}")
        except Exception as e:
            self.logger.error(f"Error processing file {file_path}: {str(e)}")
            raise

# Example usage:
if __name__ == "__main__":
    logger = AppLogger(__name__).get_logger()
    markdown_gen = MarkdownGenerator(show_code=True)
    processor = FileProcessor(markdown_gen, logger)

    try:
        processor.process_file(Path('example.py'), Path('docs'))
    except Exception as e:
        logger.error(f"Error in file processing: {str(e)}")