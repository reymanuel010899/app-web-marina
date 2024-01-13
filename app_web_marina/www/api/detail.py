import frappe

@frappe.whitelist(allow_guest=True)
def todo_escuelas():
    return frappe.get_all("Escuelas")