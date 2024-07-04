# Document Ingesting

This tool allows to index documents for the IP Mind App.

- [Document Ingesting](#document-ingesting)
  - [Supported document formats](#supported-document-formats)
  - [Overview of the indexing process](#overview-of-the-indexing-process)
    - [Chunking](#chunking)
    - [Indexing additional documents](#indexing-additional-documents)
    - [Removing documents](#removing-documents)

## Supported document formats

In order to ingest a document format, we need a tool that can turn it into text. By default, use Azure Document Intelligence (DI in the table below), but we also have local parsers for files text formats.

| Format | Manual indexing              |
| ------ | ---------------------------- |
| PDF    | Yes (DI)                     |
| DOCX   | Yes (DI)                     |
| MD     | Yes (Local)                  |
| TXT    | Yes (Local)                  |

## Overview of the indexing process

The [`main.py`](document_ingesting/main.py) script is responsible for both uploading and indexing documents. The typical usage is to call it using `scripts/docing.sh` (Mac/Linux) or `scripts/docing.ps1` (Windows), as these scripts will set up a Python virtual environment and pass in the required parameters based on the current `azd` environment.

![Diagram of the indexing process](docs/images/diagram_prepdocs.png)

The script uses the following steps to index documents:

1. If it doesn't yet exist, create a new index in Azure AI Search or Pinecone.
2. Analyze documents with prebuilt-layout (formulas add-on and markdown ouput) and upload the result to blob storage
3. Clean and format the result appropriately for the index.
4. Split the PDFs into chunks of text using semantic chunking.
5. Upload the chunks text and embeddings to Azure AI Search or Pinecone.

### Chunking

Chunking allows us to limit the amount of information we send to OpenAI due to token limits. By breaking up the content, it allows us to easily find potential chunks of text that we can inject into OpenAI. You can see the chunking algorithm in `document_ingesting/textsplitter.py`.

### Indexing additional documents

To upload more PDFs, put them in the data/raw/ folder and run `./scripts/docing.sh` or `./scripts/docing.ps1`.

It checks to see what's been uploaded before. The docing script writes an file with an MD5 hash of each file that gets uploaded. Whenever the docing script is re-run, that hash is checked against the current hash and the file is skipped if it hasn't changed.

### Removing documents

You may want to remove documents from the index. For example, if you're using the sample data, you may want to remove the documents that are already in the index before adding your own.

To remove all documents, use the `--removeall` flag. Open either `scripts/docing.sh` or `scripts/docing.ps1` and add `--removeall` to the command at the bottom of the file. Then run the script as usual.

You can also remove individual documents by using the `--remove` flag. Open either `scripts/docing.sh` or `scripts/docing.ps1`, add `--remove` to the command at the bottom of the file, and replace `/data/raw/*` with `/data/raw/YOUR-DOCUMENT-FILENAME-GOES-HERE.pdf`. Then run the script as usual.
