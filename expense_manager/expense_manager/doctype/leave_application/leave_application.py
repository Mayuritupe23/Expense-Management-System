# Copyright (c) 2024, Mayuri Tupe and contributors
# For license information, please see license.txt
# your_app/your_app/doctype/leave_application/leave_application.py

# leave_application.py
# leave_application.py


import frappe
from frappe.model.document import Document

class LeaveApplication(Document):
    def before_submit(self):
        # Check Leave Balance before submission
        leave_quota = frappe.get_doc('Leave Quota', {
            'employee': self.employee,
            'leave_type': self.leave_type
        })
        
        # Calculate the total days if not already calculated
        self.total_days = calculate_total_days(self.start_date, self.end_date)

        if leave_quota.leave_balance < self.total_days:
            frappe.throw('You do not have enough leave balance.')

    def on_submit(self):
        leave_quota = frappe.get_doc('Leave Quota', {
            'employee': self.employee,
            'leave_type': self.leave_type
        })
        
        # Update Leave Taken and Leave Balance
        leave_quota.leave_taken += self.total_days  # Increment taken leaves
        leave_quota.leave_balance = leave_quota.maximum_allowed - leave_quota.leave_taken  # Update balance
        leave_quota.save()  # Save the updated leave quota

        # Optionally refresh the fields in Leave Application if needed
        self.leave_taken = leave_quota.leave_taken
        self.leave_balance = leave_quota.leave_balance

    def on_update(self):
        self.total_days = calculate_total_days(self.start_date, self.end_date)

# Utility function to calculate total leave days
def calculate_total_days(start_date, end_date):
    if start_date and end_date:
        start_date = frappe.utils.getdate(start_date)
        end_date = frappe.utils.getdate(end_date)
        return (end_date - start_date).days + 1  # +1 to include the start day
    return 0
