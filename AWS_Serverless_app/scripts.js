// Add your API endpoint here
// Example: "https://abc123.execute-api.us-east-2.amazonaws.com/prod/books"
var API_ENDPOINT = "API_ENDPOINT_PASTE_HERE";

// Handle "Save Book" button click (POST)
document.getElementById("savebook").onclick = function() {
    var inputData = {
        "bookid": $('#bookid').val(),   // optional
        "title": $('#title').val(),
        "author": $('#author').val(),
        "year": $('#year').val()
    };

    $.ajax({
        url: API_ENDPOINT,
        type: 'POST',
        data: JSON.stringify(inputData),
        contentType: 'application/json; charset=utf-8',
        success: function (response) {
            document.getElementById("bookSaved").innerHTML = "Book Data Saved!";
            // Clear inputs if you want
            $('#bookid').val('');
            $('#title').val('');
            $('#author').val('');
            $('#year').val('');
        },
        error: function (xhr) {
            alert("Error saving book data.");
            console.log(xhr);
        }
    });
}

// Handle "View all Books" button click (GET)
document.getElementById("getbooks").onclick = function() {  
    $.ajax({
        url: API_ENDPOINT,
        type: 'GET',
        contentType: 'application/json; charset=utf-8',
        success: function (response) {

            // If using proxy integration, response might be a string -> parse it
            if (typeof response === "string") {
                try {
                    response = JSON.parse(response);
                } catch (e) {
                    console.log("Error parsing response JSON", e);
                }
            }

            $('#bookTable tr').slice(1).remove();  // remove old rows except header

            $.each(response, function(i, data) {
                $("#bookTable").append(
                    "<tr>" +
                        "<td>" + (data['bookid'] || '') + "</td>" +
                        "<td>" + (data['title'] || '') + "</td>" +
                        "<td>" + (data['author'] || '') + "</td>" +
                        "<td>" + (data['year'] || '') + "</td>" +
                    "</tr>"
                );
            });
        },
        error: function (xhr) {
            alert("Error retrieving book data.");
            console.log(xhr);
        }
    });
}
