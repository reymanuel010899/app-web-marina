import frappe

no_cache = 1
def get_context(context):
    context.student = frappe.get_doc("Estudiantes", {"user": frappe.session.user}, ["user"])
    context.escuela = frappe.get_doc("Escuela", context.student.escuela)