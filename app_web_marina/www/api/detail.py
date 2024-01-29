import frappe

@frappe.whitelist(allow_guest=True)
def todo_escuelas():
    return []