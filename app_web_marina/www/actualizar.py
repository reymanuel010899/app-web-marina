import frappe
no_cache = 1
@frappe.whitelist(allow_guest=True)
def get_context(context):
    context.student = frappe.get_doc("Estudiantes", {"user": frappe.session.user}, ["user"])
    if frappe.request.method == "POST":
        context.student.nombre = frappe.form_dict.get('nombre')
        context.student.apellido = frappe.form_dict.get('apellido')
        context.student.fecha = frappe.form_dict.get('nacimiento')
        context.student.nacionalidad = frappe.form_dict.get('nacionalidad')
        context.student.estado = frappe.form_dict.get('estado-civil')
        context.student.cedula_o_pasaporte = frappe.form_dict.get('cedula')
        context.student.celular = frappe.form_dict.get('celular')
        context.student.tipo_sambre = frappe.form_dict.get('samgre')
        context.student.direcion = frappe.form_dict.get('direcion')
        context.student.rango = frappe.form_dict.get('rango')
        context.student.fecha_ingreso = frappe.form_dict.get('ingreso')
        context.student.old_ascenso = frappe.form_dict.get('ultimo')
        context.student.institucion = frappe.form_dict.get('institucion')
        context.student.gmail = frappe.form_dict.get('correo')
        context.student.flags.ignore_permissions = True
        context.student.save()
  