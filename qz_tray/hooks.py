from . import __version__ as app_version

app_name = "qz_tray"
app_title = "Qz Tray"
app_publisher = "Kishan Panchal"
app_description = "Print using qz tray"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "k.d.panchalofc@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/qz_tray/css/qz_tray.css"
app_include_js = "/assets/qz_tray/js/qz-tray.js"

# include js, css files in header of web template
# web_include_css = "/assets/qz_tray/css/qz_tray.css"
web_include_js = "/assets/qz_tray/js/qz-tray.js"
# web_include_js = "/public/js/qz_tray.js"
# web_include_js = {
#     'frappe/public/js/qz_tray.js': 'QZ Tray'
# }

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "qz_tray/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Invoice" : "public/js/print_qz.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "qz_tray.install.before_install"
# after_install = "qz_tray.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "qz_tray.uninstall.before_uninstall"
# after_uninstall = "qz_tray.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "qz_tray.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"qz_tray.tasks.all"
#	],
#	"daily": [
#		"qz_tray.tasks.daily"
#	],
#	"hourly": [
#		"qz_tray.tasks.hourly"
#	],
#	"weekly": [
#		"qz_tray.tasks.weekly"
#	]
#	"monthly": [
#		"qz_tray.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "qz_tray.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "qz_tray.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "qz_tray.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"qz_tray.auth.validate"
# ]

