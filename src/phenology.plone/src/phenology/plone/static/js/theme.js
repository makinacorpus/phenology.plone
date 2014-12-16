var phenology = {};

phenology.initialize_phenology = function() {
    phenology.initialize_sections();
}

phenology.initialize_sections = function () {
    $('.subsections-open').click(function() {
        var button = $(this);
        var menu = button.parent().find('.subsections');
        if(menu.hasClass('active')) {
            button.removeClass('active');
            menu.removeClass('active');
        } else {
            $('.subsections-open.active').removeClass('active');
            $('.subsections.active').removeClass('active');
            menu.addClass('active');
            button.addClass('active');
        }
        return false;
    });
};
phenology.equalHeight = function(group) {
    var tallest = 0;
    group.each(function() {
        var thisHeight = $(this).height();
        if(thisHeight > tallest) {
            tallest = thisHeight;
        }
    });
    group.height(tallest);
};

jQuery(phenology.initialize_phenology);
