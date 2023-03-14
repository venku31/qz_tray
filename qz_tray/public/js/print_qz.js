frappe.ui.form.on('Sales Invoice', {
  refresh: function(frm) {
      if(frm.doc.docstatus === 1) {
          frm.add_custom_button(__('Print'), function() {
              print_doc(frm.doc, 'Standard');
          });
      }
  }
});

function printPdf(byteArray) {
  // Check if QZ Tray is already connected
  if (qz.websocket.isActive()) {
    // If QZ Tray is already connected, proceed with printing
    printData(byteArray);
  } else {
    var config = qz.configs.create({
      // Set this property to false to avoid certificate errors
      usingSecure: false
    });

    // If QZ Tray is not connected, open a new connection and then print
    qz.websocket
      .connect(config)
      .then(function () {
        printData(byteArray);
      })
      .catch(function (err) {
        console.error(err);
      });
  }
}

function printData(byteArray) {
  // Set the printer name
  var printerName = "SLK-TE322";

  // Create a print job with the PDF data and printer name
  var printJob = qz.printers.getDefault();
  printJob.contentType = "application/pdf";
  printJob.printer = printerName;
  printJob.title = cur_frm.doc.name;
  printJob.data = byteArray;

  // Send the print job to the printer
  qz.print(printJob).catch(function (err) {
    console.error(err);
  });
}

function print_doc(docname, print_format) {
  // Build the API URL
  var api_url = "/api/method/frappe.utils.print_format.download_pdf?";
  api_url += "doctype=" + encodeURIComponent(cur_frm.doctype);
  api_url += "&name=" + encodeURIComponent(docname.name);
  api_url += "&trigger_print=" + 1;
  api_url += "&format=" + encodeURIComponent(print_format);

  // Fetch the PDF data
  fetch(api_url, {
    credentials: "include"
  }).then(function(response) {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.arrayBuffer();
  }).then(function(byteArray) {
    printPdf(byteArray);
  }).catch(function(error) {
    console.error("Error:", error);
  });
}
