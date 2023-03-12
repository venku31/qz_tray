frappe.ui.form.on('Sales Invoice', {
  refresh: function(frm) {
    if (frm.doc.docstatus == 1 && !frm.doc.__islocal) {
      frm.add_custom_button(__('Print'), function() {
        frappe.call({
          method: 'qz_tray.print_doc.print_sales_invoice',
          args: {
            docname: frm.docname
          },
          callback: function(r) {
            if (r.message) {
              console.log(r);
              // send the PDF to QZ Tray
              frappe.require('assets/qz_tray/public/js/qz-tray.js', function() {
                qz.printers.find('PrinterName').then(function(printer) {
                  var config = qz.configs.create(printer);
                  var data = [
                    { type: 'raw', format: 'pdf', data: r.message }
                  ];
                  qz.print(config, data).catch(function(e) {
                    console.error(e);
                  });
                }).catch(function(e) {
                  console.error(e);
                });
              });
            }
          }
        });
      }).addClass('btn-primary');
    }
  }
});
