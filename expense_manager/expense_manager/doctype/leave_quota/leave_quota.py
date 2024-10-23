# Copyright (c) 2024, Mayuri Tupe and contributors
# For license information, please see license.txt

# import frappe
# your_app/your_app/doctype/leave_quota/leave_quota.py
# leave_quota.py
# leave_quota.py


# import frappe
# from frappe.model.document import Document

# class LeaveQuota(Document):
#     def before_insert(self):
#         # Set Leave Taken to 0 and Leave Balance to Maximum Allowed upon creation
#         self.leave_taken = 0
#         self.leave_balance = self.maximum_allowed

#     def update_leave_balance(self, leave_days):
#         # Update Leave Taken and Leave Balance
#         self.leave_taken += leave_days
#         self.leave_balance = self.maximum_allowed - self.leave_taken

#         # Ensure Leave Balance does not go negative
#         if self.leave_balance < 0:
#             frappe.throw("Leave balance cannot be negative.")

#         self.save()

import frappe
from frappe.model.document import Document

class LeaveQuota(Document):
    
    def before_insert(self):
        # Set Leave Taken to 0 and Leave Balance to Maximum Allowed upon creation
        self.leave_taken = 0
        self.leave_balance = self.maximum_allowed

    def validate(self):
        # Always ensure Leave Balance is updated correctly
        self.leave_balance = self.maximum_allowed - self.leave_taken

        # Ensure Leave Balance does not go negative
        if self.leave_balance < 0:
            frappe.throw("Leave balance cannot be negative.")
