// When the DOM has finished loading, start loading the basics for the game.
document.addEventListener("DOMContentLoaded", function () {

    // Add events to form elements
    $('#ingredients_plus').click(function(){add_field("ingredients");});
    $('#ingredients_minus').click(function(){remove_field("#ingredients_div");});
    $('#cookingSteps_plus').click(function(){add_field("cookingSteps");})
    $('#cookingSteps_minus').click(function(){remove_field("#cookingSteps_div");});
    $('#tipsTricks_plus').click(function(){add_field("tipsTricks");})
    $('#tipsTricks_minus').click(function(){remove_field("#tipsTricks_div");});

});

function add_field(field) {
    // Set the div name, create the new input field and add it to the dom
    const FORM_FIELD = "#" + field + "_div";
    let children = $(FORM_FIELD).children().length -1;

    let new_field = (`
        <input type="text" name="${field}[]" id="${field}${children}" class="form-control" required>
    `);
        
    $(FORM_FIELD).append(new_field);
}

function remove_field(field) {
    // Remove the last child of the passed in div
    $(field).children().last().remove();
}