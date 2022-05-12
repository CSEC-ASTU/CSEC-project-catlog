/*
 Template Name: Agroxa - Responsive Bootstrap 4 Admin Dashboard
 Author: Themesbrand
 File: Xeditable js
 */

$(function () {

    //modify buttons style
    $.fn.editableform.buttons =
        '<button type="submit" class="btn btn-success editable-submit btn-sm waves-effect waves-light"><i class="mdi mdi-check"></i></button>' +
        '<button type="button" class="btn btn-danger editable-cancel btn-sm waves-effect waves-light"><i class="mdi mdi-close"></i></button>';


    //inline

    console.log("i was here")
    $('#inline-username').editable({
        type: 'text',
        pk: 1,
        name: 'username',
        title: 'Enter username',
        mode: 'inline',
        inputclass: 'form-control-sm'
    });

    $('#inline-firstname').editable({
        validate: function (value) {
            if ($.trim(value) == '') return 'This field is required';
        },
        mode: 'inline',
        inputclass: 'form-control-sm',
    });

    $('#inline-lastname').editable({
        validate: function (value) {
            if ($.trim(value) == '') return 'This field is required';
        },
        mode: 'inline',
        inputclass: 'form-control-sm',
    });

    $('#inline-phonenumber').editable({
        validate: function (value) {
            if ($.trim(value) == '') return 'This field is required';
        },
        mode: 'inline',
        inputclass: 'form-control-sm',
    });

    // Facebook
    $('#inline-facebook').editable({
        validate: function (value) {
            if ($.trim(value) == '') return 'This field is required';  
            // Validate if the value is valid facebook url
            var facebook_regex = /^(https?:\/\/)?(www\.)?facebook.com\/.+$/;
            if (!facebook_regex.test(value)) {
                return 'Please enter a valid Facebook URL';
            }
        },
        mode: 'inline',
        inputclass: 'form-control-sm',
    });
    // instagram 
    $('#inline-instagram').editable({
        validate: function (value) {
            if ($.trim(value) == '') return 'This field is required';
            // Validate if the value is valid instagram url
            var instagram_regex = /^(https?:\/\/)?(www\.)?instagram.com\/.+$/;
            if (!instagram_regex.test(value)) {
                return 'Please enter a valid Instagram URL';
            }
        },
        mode: 'inline',
        inputclass: 'form-control-sm',
    });
    // Linkedin
    $('#inline-linkedin').editable({
        validate: function (value) {
            if ($.trim(value) == '') return 'This field is required';
            // Validate if the value is valid linkedin url
            var linkedin_regex = /^(https?:\/\/)?(www\.)?linkedin.com\/.+$/;
            if (!linkedin_regex.test(value)) {
                return 'Please enter a valid Linkedin URL';
            }
        },
        mode: 'inline',
        inputclass: 'form-control-sm',
    });
    // github
    $('#inline-github').editable({
        validate: function (value) {
            if ($.trim(value) == '') return 'This field is required';
            // Validate if the value is valid github url
            var github_regex = /^(https?:\/\/)?(www\.)?github.com\/.+$/;
            if (!github_regex.test(value)) {
                return 'Please enter a valid Github URL';
            }
        },
        mode: 'inline',
        inputclass: 'form-control-sm',
    });
    // Valid website
    $('#inline-website').editable({
        validate: function (value) {
            if ($.trim(value) == '') return 'This field is required';
            // Validate url either http or https
            var website_regex = /^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/;
            if (!website_regex.test(value)) {
                return 'Please enter a valid website URL';
            }
        },
        mode: 'inline',
        inputclass: 'form-control-sm',
    });



    $('#inline-sex').editable({
        mode: 'inline',
        inputclass: 'form-control-sm',
        source: [
            {value: 1, text: 'male'},
            {value: 2, text: 'female'}
        ],
        display: function (value, sourceData) {
            var colors = {"": "#98a6ad", 1: "#5fbeaa", 2: "#5d9cec"},
                elem = $.grep(sourceData, function (o) {
                    return o.value == value;
                });

            if (elem.length) {
                $(this).text(elem[0].text).css("color", colors[value]);
            } else {
                $(this).empty();
            }
        }
    });

    $('#inline-status').editable({
        mode: 'inline',
        inputclass: 'form-control-sm'
    });

    $('#inline-group').editable({
        showbuttons: false,
        mode: 'inline',
        inputclass: 'form-control-sm'
    });

    $('#inline-dob').editable({
        mode: 'inline',
        inputclass: 'form-control-sm'
    });

    $('#inline-comments').editable({
        showbuttons: 'bottom',
        mode: 'inline',
        inputclass: 'form-control-sm'
    });


});