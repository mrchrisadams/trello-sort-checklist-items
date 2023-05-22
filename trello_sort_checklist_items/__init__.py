import os

import trello


class ChecklistSorter:
    def __init__(self, api_key: str, token: str):

        self.chk = trello.Checklists(api_key, token=token)

    def sort_items_in_checklist(self, checklist_id: str):
        """
        Accept a checklist if for a checkist to sort the items on sort them alphabetically.
        """
        checklist = self.chk.get_checkItem(checklist_id)

        names = [item["name"] for item in checklist]
        ids = [item["id"] for item in checklist]

        sorted_names = sorted([name.lower() for name in names])

        # delete all the items
        for id in ids:
            self.chk.delete_checkItem_idCheckItem(id, checklist_id)

        # add them back in, in alphabetical order
        for name in sorted_names:
            self.chk.new_checkItem(checklist_id, name)
