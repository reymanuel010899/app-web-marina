import frappe

no_cache = 1
def get_context(context):
   #context.user = ""
    try:

        context.student = frappe.get_doc("Estudiantes", {"user": frappe.session.user}, ["user"])

    except:
        frappe.local.flags.redirect_location = "login"
        raise frappe.Redirect