
frappe.ui.form.on('Sales Invoice', {
  refresh: function(frm) {
    console.log(frm.doc.docstatus)
    if (frm.doc.docstatus == 1 && !frm.doc.__islocal) {
      frm.add_custom_button(__('Print'), function() {
        frappe.require('/assets/qz_tray/js/qz-tray.js', function() {
          
          frappe.call({
            method: 'qz_tray.print_doc.print_sales_invoice',
            args: {
              docname: frm.docname
            },
            callback: function(r) {
              if (r.message) {
                // connect to QZ Tray
                qz.websocket.connect().then(function() {
                  // send the PDF to QZ Tray
                  qz.printers.find('Microsoft Print to PDF').then(function(printer) {
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
                }).catch(function(e) {
                  console.error(e);
                });
              }
            }
          });
        });
      }).addClass('btn-primary');
    }
  }
});

