# How to resolve the validation error which has come while running the code involving Docling which has been configured

Curated at: `2026-08-27T09:48:58.423936+00:00`
Model: `Public Q&A`
Author: `NullDev`
Tags: `public-q&a, Stack Overflow, python, langchain`
Source: https://stackoverflow.com/questions/79996703/how-to-resolve-the-validation-error-which-has-come-while-running-the-code-involv


## Why It Is Good

- Public Q&A from Stack Overflow.
- Question score: 2; answer score: 2.
- Viewed 64 times on the source site.

## Question

Unable to inspect the data present in the respective pdf files. After resolving the cv2 dependency issue and diagnosed the Docling/PyTorch cl.exe[Microsoft C++ compiler] compiler error by installing the required Microsoft C++ build tools and simplifying the Docling configuration. Even through the error has been resolved, the PDF processing takes considerable time owing to its layout/model processing capabilities. [code omitted]

## Answer

It seems like DoclingLoader treats convert_kwargs as keyword arguments to DocumentConverter.convert() . But by the docs , format_options belongs to the DocumentConverter constructor. Not DocumentConverter.convert() . So instead of doing DoclingLoader( ... convert_kwargs={ "format_options": {...} } ) just do converter = DocumentConverter( format_options={...} ) DoclingLoader( ..., converter=converter, ) pipeline_options = PdfPipelineOptions( do_ocr=False, do_table_structure=False, do_picture_classification=False, do_picture_description=False, do_chart_extraction=False, do_code_enrichment=False, do_formula_enrichment=False, generate_page_images=False, generate_picture_images=False, generate_table_images=False, ) # configure the converter here, not in convert_kwargs converter = DocumentConverter( format_options={ InputFormat.PDF: PdfFormatOption( pipeline_options=pipeline_options ) } ) for file_path in pdf_files: print(f"\nProcessing: {file_path.name}") loader = DoclingLoader( file_path=str(file_path), converter=converter, export_type="markdown", ) docs = loader.load() print(f"Documents loaded: {len(docs)}") for d in docs[:3]: print(d.page_content[:500])
