# import logging
# from pathlib import Path

# from azure.ai.documentintelligence.models import AnalyzeResult

# from .azure_helper.container_manager import ContainerManager
# from .doc_intelligence_parser import DocIntelligenceParser
# from .list_file_strategy import File, ListFileStrategy
# from .doc_split import PageSplit
# from .search_manager import SearchManager, Section
# from .strategy import DocumentAction, Strategy
# from .text_splitter import SemanticTextSplitter

# from .openia.vision import OpenAIVision

# logger = logging.getLogger("ingester")


# async def parse_file(
#     file: File,
#     doc_int_parser: DocIntelligenceParser,
#     category: str | None = None,
#     vision_service: OpenAIVision | None = None,
# ) -> list[Section]:
#     to_extract_images = vision_service is not None
#     file_extension = file.file_extension()
#     if file_extension != ".pdf":
#         logger.info("Skipping '%s', no parser found.", file.filename())
#         return []
#     logger.info("Ingesting '%s'", file.filename())
#     if to_extract_images:  # TODO: implement this
#         logger.info("Extracting images '%s''", file.filename())
#         raise NotImplementedError("Image extraction is not implemented yet")
#     pages = [
#         page async for page in doc_int_parser.parse(file.filepath)
#     ]

#     logger.info("Splitting '%s' into sections", file.filename())
#     splitter = SemanticTextSplitter()
#     sections = [
#         Section(split_page, filepath=file.filepath, category=category)
#         for split_page in splitter.split_pages(pages)
#         if split_page.text
#     ]

#     # if provided, use the vision service to create chunk descriptions for the file images
#     # if to_extract_images:
#     #     img_folder = file.filepath + "_images"  # TODO: fix this line
#     #     img_files = []
#     #     for f_path in Path(img_folder).iterdir():
#     #         if f_path.is_file() and f_path.suffix in OpenAIVision.SUPPORTED_EXTENSIONS:
#     #             img_files.append(f_path)
#     #     pages_num = [int(f.stem.split("-")[-2]) for f in img_files]
#     #     img_descriptions: list[str] = await vision_service.create_responses(img_files)
#     #     img_chunks = [
#     #         PageSplit(page_num=p, text=desc)
#     #         for p, desc in zip(pages_num, img_descriptions)
#     #         if desc
#     #     ]
#     #     sections.extend(
#     #         [Section(split_page=c, content=file, category=category) for c in img_chunks]
#     #     )
#     return sections


# class FileStrategy(Strategy):
#     """
#     Strategy for ingesting documents into a search service from files stored locally
#     """

#     def __init__(
#         self,
#         list_file_strategy: ListFileStrategy,
#         search_manager: SearchManager,
#         doc_int_parser: DocIntelligenceParser,
#         document_action: DocumentAction = DocumentAction.add,
#         category: str | None = None,
#         vision_service: OpenAIVision | None = None,
#     ):
#         self.list_file_strategy = list_file_strategy
#         self.doc_int_parser = doc_int_parser
#         self.document_action = document_action
#         self.search_manager = search_manager
#         self.category = category
#         self.vision_service = vision_service

#     async def setup(self):
#         await self.search_manager.create_index()

#     async def run(self):
#         if self.document_action == DocumentAction.add:
#             files = self.list_file_strategy.list()
#             async for f in files:
#                 try:
#                     sections = await parse_file(
#                         f, self.doc_int_parser, self.category, self.vision_service
#                     )
#                     if sections:
#                         await self.search_manager.update_content(sections)
#                 finally:
#                     if f:
#                         f.close()
#         # elif self.document_action == DocumentAction.remove:
#         #     paths = self.list_file_strategy.list_paths()
#         #     async for path in paths:
#         #         await self.blob_manager.remove_blob(path)
#         #         await self.search_manager.remove_content(path)
#         # elif self.document_action == DocumentAction.remove_all:
#         #     await self.blob_manager.remove_blob()
#         #     await self.search_manager.remove_content()
