$(document).ready(function () {
    console.log("i was here")
  $("#user_form").submit(function (e) {
    e.preventDefault();

    const csrf_token = $("meta[name=csrf-token]").attr("content");
    const firstname = $("#inline-firstname")[0].outerText;
    const lastname = $("#inline-lastname")[0].outerText;
    const phonenumber = $("#inline-phonenumber")[0].outerText;
    const birthdate = $("#inline-dob")[0].outerText;
    const gender = $("#inline-sex")[0].outerText;
    // split the date into month, day, year
    const dob = birthdate.split("/");
    // reverse the order of the date
    const dob_reverse = dob.reverse();
    // join the date back together
    const dob_join = dob_reverse.join("-");

    const form = new FormData(this);
    form.append("first_name", firstname);
    form.append("last_name", lastname);
    form.append("phone_number", phonenumber);
    form.append("csrfmiddlewaretoken", csrf_token);
    form.append("birth_date", dob_join);
    form.append("gender", gender);

    console.log(form);
    $.ajax({
        url: "/auth/profile/edit/",
        type: "POST",
        data: form,
        processData: false,
        contentType: false,
        success: function (data) {
            swal(
                {
                    title: 'Good job!',
                    text: 'You clicked the button!',
                    type: 'success',
                    showCancelButton: true,
                    confirmButtonClass: 'btn btn-success',
                    cancelButtonClass: 'btn btn-danger m-l-10'
                }
            )
        },
        error: function (data) {
            console.log(data);
            alert("Error Happened");
        },
    });

  });
});
