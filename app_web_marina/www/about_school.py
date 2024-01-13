import frappe

def get_context(context):
    context.student = frappe.get_doc("Estudiantes", {"user": frappe.session.user}, ["user"])
    semestres = frappe.get_all("Semestre")