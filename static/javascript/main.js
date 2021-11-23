// When the DOM has finished loading, start loading the basics for the game.
document.addEventListener("DOMContentLoaded", function () {

    // Add events to form elements
    $('#ingredients_plus').click(function(){add_field("ingredients");});
    $('#ingredients_minus').click(function(){remove_field("#ingredients_div");});
    $('#cookingSteps_plus').click(function(){add_field("cookingSteps");});
    $('#cookingSteps_minus').click(function(){remove_field("#cookingSteps_div");});
    $('#tipsTricks_plus').click(function(){add_field("tipsTricks");});
    $('#tipsTricks_minus').click(function(){remove_field("#tipsTricks_div");});
    $(window).resize(check_overflow);

    check_overflow();

    $('#carouselNewlyAdded').bind('slide.bs.carousel', function () {
        // Use a delay after the event is fired
        // else you don't have the scrollwidth
        setTimeout(function(){
            check_overflow();
        }, 200);
    });

});

function add_field(field) {
    // Set the div name, create the new input field and add it to the dom
    const FORM_FIELD = "#" + field + "_div";
    let children = $(FORM_FIELD).children().length -1;

    let new_field = (`
        <input type="text" name="${field}[]" id="${field}${children}" 
                     class="form-control" required>
    `);
        
    $(FORM_FIELD).append(new_field);
}

function remove_field(field) {
    // Remove the last child of the passed in div
    $(field).children().last().remove();
}

function check_overflow() {
    // Loop through all elements with the check-overflow mark
    // See if they have overflow active, and if so
    // make the ... visible
    let elements = $('.check-overflow');
    for (let i = 0;i < elements.length; i++) {
        let element = elements[i];
        if (element.scrollWidth > element.clientWidth) {
            console.log("wider then client");
            console.log(element.scrollWidth, element.clientWidth);
            $(element).siblings().removeClass('d-none');
        } else {    
            $(element).siblings().addClass('d-none');
        }
    }
}

