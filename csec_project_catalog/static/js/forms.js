$(document).ready(function () {
  console.log("i was here");
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

    const facebook = $("#inline-facebook")[0].outerText;
    const instagram = $("#inline-instagram")[0].outerText;
    const twitter = $("#inline-twitter")[0].outerText;
    const linkedin = $("#inline-linkedin")[0].outerText;
    const github = $("#inline-github")[0].outerText;
    const website = $("#inline-website")[0].outerText;

    const form = new FormData(this);
    form.append("first_name", firstname);
    form.append("last_name", lastname);
    form.append("phone_number", phonenumber);
    form.append("csrfmiddlewaretoken", csrf_token);
    form.append("birth_date", dob_join);
    form.append("gender", gender);
    form.append("facebook", facebook);
    form.append("instagram", instagram);
    form.append("twitter", twitter);
    form.append("linkedin", linkedin);
    form.append("github", github);
    form.append("website", website);

    console.log(form);
    $.ajax({
      url: "/auth/profile/edit/",
      type: "POST",
      data: form,
      processData: false,
      contentType: false,
      success: function (data) {
        swal({
          title: "Good job!",
          text: "Successfully Updated!",
          type: "success",
          confirmButtonClass: "btn btn-success",
          cancelButtonClass: "btn btn-danger m-l-10",
        });
      },
      error: function (data) {
        console.log(data);
        swal({
          title: "Error!",
          text: "Error Happened!",
          type: "warning",
          confirmButtonClass: "btn btn-danger m-l-10",
        });
      },
    });
  });
});
