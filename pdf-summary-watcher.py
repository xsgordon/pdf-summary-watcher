import argparse
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from docling.document_converter import DocumentConverter
from textsum.summarize import Summarizer
import webbrowser

SYSTEM_MODEL="BEE-spoke-data/pegasus-x-base-synthsumm_open-16k"

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None

        if event.src_path.endswith(".pdf"):
            try:

                converter = DocumentConverter()

                # Convert PDF to Markdown
                result = converter.convert(event.src_path)
                markdown_text = result.document.export_to_markdown()

                # Generate Summary
                summarizer = Summarizer(model_name_or_path=SYSTEM_MODEL)
                summary = summarizer.summarize_string(markdown_text)

                # Write to file
                out_file = os.path.splitext(event.src_path)[0] + ".txt"
                with open(out_file, "w") as f:
                    f.write(summary)

                print(f"Processed: {event.src_path}")

            except Exception as e:
                print(f"Error processing {event.src_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Watch directory for new PDFs and generate summaries.")
    parser.add_argument("--directory", required=True, help="Directory to watch")
    parser.add_argument("--model", required=False, help="Model to use for summarization", default=SYSTEM_MODEL)
    args = parser.parse_args()

    SYSTEM_MODEL=args.model

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=args.directory, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()