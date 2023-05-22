import os
from dotenv import load_dotenv

from trello_sort_checklist_items import ChecklistSorter

TRELLO_CHECKLIST_SORT_API_KEY = os.getenv("TRELLO_CHECKLIST_SORT_API_KEY")
TRELLO_CHECKLIST_SORT_API_TOKEN = os.getenv("TRELLO_CHECKLIST_SORT_API_TOKEN")
TRELLO_CHECKLIST_SORT_CHECKLIST_ID = os.getenv("TRELLO_CHECKLIST_SORT_CHECKLIST_ID")

load_dotenv()

sorter = ChecklistSorter(TRELLO_CHECKLIST_SORT_API_KEY, TRELLO_CHECKLIST_SORT_API_TOKEN)
sorter.sort_items_in_checklist(TRELLO_CHECKLIST_SORT_CHECKLIST_ID)
