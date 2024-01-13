import frappe


def get_context(context):
    try:

       context.student = frappe.get_doc("Estudiantes", {"user": frappe.session.user}, ["user","carrera"])

    except:
       frappe.local.flags.redirect_location = "login"
       raise frappe.Redirect

    context.semestres = frappe.get_list("Semestre", filters = {"carrera": context.student.carrera}, fields=["semester","name"], order_by="semester ASC",  ignore_permissions = True)