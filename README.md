# trello-sort-checklist-items

A toy module for sorting checklists items on cards in trello.

Created out of frustration at using trello loads, but never finding an elegant way to sort checklists in the web app, or any of the mobile apps, or free power ups.

## Usage

First of all make sure you have these set as environment variables:

- `TRELLO_CHECKLIST_SORT_API_KEY` - this is issued to you by Trello when you register an app. It's ok for this to be public.
- `TRELLO_CHECKLIST_SORT_API_TOKEN` - treat this as a secret only you should have access to. Anyone with the API Key and API Token can act as you!

See more [about Trello authentication on their documentation site](https://developer.atlassian.com/cloud/trello/guides/rest-api/authorization/)

- `TRELLO_CHECKLIST_SORT_CHECKLIST_ID` - this is the ID of the checklist on a given card. Add `.json` to the end the url for a trello card to see it the card represented as json, and to see the checklist IDs on a card 

Next, use the module like so:.

```python
import os
from dotenv import load_dotenv

from trello_sort_checklist_items import ChecklistSorter

TRELLO_CHECKLIST_SORT_API_KEY = os.getenv("TRELLO_CHECKLIST_SORT_API_KEY")
TRELLO_CHECKLIST_SORT_API_TOKEN = os.getenv("TRELLO_CHECKLIST_SORT_API_TOKEN")
TRELLO_CHECKLIST_SORT_CHECKLIST_ID = os.getenv("TRELLO_CHECKLIST_SORT_CHECKLIST_ID")

load_dotenv()

sorter = ChecklistSorter(
    TRELLO_CHECKLIST_SORT_API_KEY, 
    TRELLO_CHECKLIST_SORT_API_TOKEN
)

sorter.sort_items_in_checklist(
    TRELLO_CHECKLIST_SORT_CHECKLIST_ID
)

```
